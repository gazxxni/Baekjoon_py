select ID, FISH_NAME, LENGTH from FISH_INFO a
join FISH_NAME_INFO b on a.FISH_TYPE = b.FISH_TYPE
where (a.FISH_TYPE, a.LENGTH) in (select FISH_TYPE, max(LENGTH) from FISH_INFO
                 group by FISH_TYPE)
order by a.ID