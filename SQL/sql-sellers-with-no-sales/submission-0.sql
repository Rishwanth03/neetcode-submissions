/* SELECT s.seller_name
FROM seller s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.seller_id = s.seller_id
      AND EXTRACT(YEAR FROM o.sale_date) = 2020
)
ORDER BY s.seller_name; */

select s.seller_name

from seller s

left join orders o

on s.seller_id = o.seller_id

and extract(year from o.sale_date) = 2020

where o.order_id is null

order by s.seller_name