select a.ID,  count(b.parent_id) CHILD_COUNT 
from ECOLI_DATA a left join ECOLI_DATA b on a.id = b.parent_id
group by a.id
order by a.id