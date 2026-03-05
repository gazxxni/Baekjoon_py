SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS a 
join ANIMAL_OUTS b on a.ANIMAL_ID = b.ANIMAL_ID
where SEX_UPON_INTAKE like 'Intact%'
and SEX_UPON_OUTCOME not like 'Intact%'
order by a.ANIMAL_ID