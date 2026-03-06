SELECT a.CAR_ID, a.CAR_TYPE, round(a.DAILY_FEE * 30 * (100 - b.DISCOUNT_RATE) / 100) FEE
from CAR_RENTAL_COMPANY_CAR a
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN b on a.CAR_TYPE = b.CAR_TYPE
where a.CAR_ID not in (
    select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE <= '2022-11-30' and END_DATE >= '2022-11-01' 
)
and a.CAR_TYPE in ('세단', 'SUV' )
and DURATION_TYPE = '30일 이상'
having FEE between 500000 and 2000000
order by FEE desc, a.CAR_TYPE, a.CAR_ID desc