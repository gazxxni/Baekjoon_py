with recursive rec as (
    select ID, PARENT_ID, 1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select a.ID, a.PARENT_ID, b.GENERATION + 1
    from ECOLI_DATA a
    join rec b on b.id = a.parent_id

)

select count(id) COUNT, GENERATION from rec
where id not in (
    select distinct parent_id
    from ECOLI_DATA
    where parent_id is not null
)
group by GENERATION
order by GENERATION