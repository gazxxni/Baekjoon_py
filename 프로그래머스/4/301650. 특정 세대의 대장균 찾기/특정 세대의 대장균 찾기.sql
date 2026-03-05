select c.ID 
from ECOLI_DATA a
join ECOLI_DATA b on a.id = b.parent_id
join ECOLI_DATA c on b.id = c.parent_id
where a.parent_id is null
order by c.id