SELECT month(START_DATE) MONTH, CAR_ID, count(*) RECORDS 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between '2022-08-01' and '2022-10-31'
    group by car_id
    having count(*) >= 5)
and 
    START_DATE between '2022-08-01' and '2022-10-31'
group by MONTH, CAR_ID
having RECORDS > 0
order by MONTH, CAR_ID desc