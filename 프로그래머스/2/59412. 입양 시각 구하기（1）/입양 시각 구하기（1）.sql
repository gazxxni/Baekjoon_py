SELECT hour(DATETIME) HOUR, count(*) COUNT from ANIMAL_OUTS
group by hour(DATETIME)
having HOUR >= 9 and HOUR <= 19
order by HOUR