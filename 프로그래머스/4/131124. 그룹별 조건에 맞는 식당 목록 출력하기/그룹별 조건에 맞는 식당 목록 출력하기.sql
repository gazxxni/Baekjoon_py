SELECT MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
from MEMBER_PROFILE a
join REST_REVIEW b on a.MEMBER_ID = b.MEMBER_ID
where a.MEMBER_ID in (
    select MEMBER_ID from REST_REVIEW
    group by MEMBER_ID
    having count(*) = (
        select count(*) from REST_REVIEW
        group by MEMBER_ID
        order by count(*) desc limit 1
    )
)
order by REVIEW_DATE, REVIEW_TEXT