{% macro discounted_amount(extended_price, discount_rate, scale=2) %}
    (-1 * {{extended_price}} * {{discount_rate}})::decimal(16, {{ scale }})
{% endmacro %}
