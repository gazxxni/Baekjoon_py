select count(*) FISH_COUNT, month(TIME) MONTH from FISH_INFO
group by month(TIME)
order by MONTH