select flavor from (
    SELECT FLAVOR, TOTAL_ORDER from FIRST_HALF
    union all
    SELECT FLAVOR, TOTAL_ORDER from JULY) a
group by FLAVOR
order by sum(TOTAL_ORDER) desc limit 3