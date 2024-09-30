
# ELT Pipeline with dbt, Snowflake, and Airflow

This project demonstrates how to build an ELT (Extract, Load, Transform) pipeline using dbt (data build tool), Snowflake, and Airflow. It extracts raw data from Snowflake’s sample datasets, transforms it using dbt models, and orchestrates the transformations using Airflow.

## Project Overview

### 1. **Snowflake Setup**

We set up a dedicated environment in Snowflake to handle the ELT pipeline. The key components created include:

- **Warehouse**: `dbt_wh` – Handles compute resources for the data transformations.
- **Database**: `dbt_db` – Stores the transformed and raw data.
- **Schema**: `dbt_schema` – Stores the transformed tables.
- **Role**: `dbt_role` – Manages access control for the pipeline.

### 2. **dbt Configuration**

We configured dbt to interact with Snowflake by setting up the `profiles.yml` file, ensuring that models are materialized as views or tables depending on their purpose:

- **Staging Models**: Materialized as **views**.
- **Data Marts (Fact Models)**: Materialized as **tables**.

### 3. **Source and Staging Models**

- **Source Models**: Represent raw data from Snowflake's `tpch_sf1` dataset (tables like `orders` and `lineitem`).
- **Staging Models**: Clean and prepare raw data for transformation. These serve as intermediary models that will be used for building the final tables.

### 4. **Macros**

The project uses **dbt macros** to avoid duplicating transformation logic. For example, a macro calculates discounted amounts for line items.

### 5. **Transform Models (Data Marts)**

- **Intermediate Tables**: Join multiple staging models and apply business logic to calculate new metrics


### 6. **Data Quality Testing**

- **Generic Tests**: Ensure key fields are unique, not null, and conform to foreign key relationships.
- **Singular Tests**: Custom SQL tests ensure data integrity (e.g., checking discount amounts and valid date ranges).

### 7. **Airflow Orchestration**

Airflow orchestrates the pipeline by scheduling dbt models to run on a daily basis:

- The **DAG** defines the scheduling logic, with dbt transformations being executed automatically.
- Airflow uses a Snowflake connection (`snowflake_conn`) to communicate with Snowflake and orchestrate the data pipeline.

## Installation

### Prerequisites

- Python 3.10+
- [Snowflake Account](https://www.snowflake.com/)
- [dbt CLI](https://docs.getdbt.com/dbt-cli/installation) installed
- Airflow set up (via Docker, Astronomer, or locally)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YvvonM/tpch_sample_data_dbt_snowflake_datapipeline.git
   cd tpch_sample_data_dbt_snowflake_datapipeline
   ```

2. **Install Dependencies**

   Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Snowflake**

   Create the necessary Snowflake resources (warehouse, database, role, schema) by following the SQL script provided in `Step 1` of the project. This includes creating the warehouse (`dbt_wh`), database (`dbt_db`), and role (`dbt_role`).

4. **Configure dbt Profiles**

   Configure dbt by adding your Snowflake credentials in the `profiles.yml` file. The configuration should look like this:

   ```yaml
   datasn_pipeline:
     target: dev
     outputs:
       dev:
         type: snowflake
         account: <your_account>
         user: <your_username>
         password: <your_password>
         role: dbt_role
         database: dbt_db
         warehouse: dbt_wh
         schema: dbt_schema
         threads: 4
         client_session_keep_alive: False
   ```

5. **Run dbt Models**

   Use dbt to run the models and transform your data in Snowflake:

   ```bash
   dbt run
   ```

   To run tests:

   ```bash
   dbt test
   ```

6. **Set Up Airflow**

   Configure Airflow to orchestrate the pipeline by updating the Airflow **DAG** file (`dbt_dag.py`). Make sure the `snowflake_conn` connection in Airflow UI has the correct Snowflake credentials.

7. **Deploy the DAG**

   Start Airflow and deploy the DAG to run dbt models on a daily basis.

   ```bash
   airflow dags trigger dbt_dag
   ```

## Technologies Used

- **Snowflake**: Cloud-based data warehouse.
- **dbt**: Data build tool for transforming and testing data.
- **Airflow**: Workflow orchestration tool for scheduling data pipelines.

