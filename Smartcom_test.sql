select e.*, dep_summary.sub_departments from employees e
left join (
with recursive dep_CTE (department_id, id, department_name, parent_id) as (
    select id as department_id,
           id,
           name as department_name,
           parent_id
    from departments
    union all
    select dC.department_id,
           d.id,
           dC.department_name,
           d.parent_id
    from departments d
    inner join dep_CTE dC on d.parent_id = dC.id
)
select department_id as id, department_name, group_concat(id) as sub_departments
from dep_CTE
group by department_id, department_name
) as dep_summary
on dep_summary.id = e.department_id;


