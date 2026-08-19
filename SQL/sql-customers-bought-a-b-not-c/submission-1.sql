select c.customer_id, c.customer_name
from customers as c
join orders as o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name
having 
   sum(case when product_name = 'A' then 1 else 0 end)>0
   AND
   sum(case when product_name = 'B' then 1 else 0 end)>0
   AND
   sum(case when product_name = 'C' then 1 else 0 end)=0
order by customer_name