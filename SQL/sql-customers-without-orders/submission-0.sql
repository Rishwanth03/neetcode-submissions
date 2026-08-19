/*select c.name
from customer as c
left join orders as o
on c.customer_id = o.id
where o.id is null */

SELECT c.name
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE o.id IS NULL;