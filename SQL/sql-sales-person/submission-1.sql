/*
select s.name
from sales_person s
where not exists (
    select 1
    from orders o
    join company c
    on o.com_id = c.com_id
    where o.sales_id = s.sales_id
    and c.name = 'CRIMSON'

)
*/
select s.name
from sales_person s
left join (
    select o.sales_id
    from orders o
    join company c
    on c.com_id = o.com_id
    where c.name = 'CRIMSON'
)t
on s.sales_id = t.sales_id
where t.sales_id is null