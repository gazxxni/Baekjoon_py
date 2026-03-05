SELECT year(SALES_DATE) YEAR, month(SALES_DATE) MONTH,
    count(DISTINCT b.USER_ID) PURCHASED_USERS,
    round((count(DISTINCT b.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021)), 1) PUCHASED_RATIO
from USER_INFO a
join ONLINE_SALE b on a.USER_ID = b.USER_ID
where year(JOINED) = 2021
group by year, month
order by year, month