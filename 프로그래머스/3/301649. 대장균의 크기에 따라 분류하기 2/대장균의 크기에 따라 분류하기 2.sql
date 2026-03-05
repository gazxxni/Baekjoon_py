select ID, 
    case when per <= 0.25 then 'CRITICAL'
        when per <= 0.5 then 'HIGH'
        when per <= 0.75 then 'MEDIUM'
        else 'LOW'
    end COLONY_NAME 
from 
    (select id, percent_rank() over (order by SIZE_OF_COLONY desc) per
     from ECOLI_DATA) a
order by id