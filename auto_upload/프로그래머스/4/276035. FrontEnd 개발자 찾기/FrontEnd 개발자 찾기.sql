select distinct id, EMAIL, FIRST_NAME, LAST_NAME
from SKILLCODES a
join DEVELOPERS b on (a.CODE & b.SKILL_CODE) > 0
where CATEGORY = 'Front End'
order by id