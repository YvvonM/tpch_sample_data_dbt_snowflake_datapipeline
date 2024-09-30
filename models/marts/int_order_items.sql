select
    line_item.order_item_key,
    line_item.part_key,
    line_item.line_number,
    line_item.extended_price,
    orders.order_key,
    orders.customer_key,
    orders.order_date,
    
from
    {{ ref('stag_tpch_order') }} as orders
join
    {{ ref('stag_tpch_lineitems') }} as line_item
    on orders.order_key = line_item.order_key
order by
    orders.order_date
