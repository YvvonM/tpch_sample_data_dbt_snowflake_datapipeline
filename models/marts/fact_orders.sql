select
    orders.*,
    order_item_summary.gross_item_sales_amount
from
    {{ref('stag_tpch_order')}} as orders
join
    {{ref('int_order_items_summary')}} as order_item_summary
        on orders.order_key = order_item_summary.order_key
order by order_date
