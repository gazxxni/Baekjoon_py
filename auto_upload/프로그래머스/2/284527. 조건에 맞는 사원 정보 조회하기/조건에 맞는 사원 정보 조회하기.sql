select sum(b.SCORE) SCORE, b.EMP_NO, a.EMP_NAME, a.POSITION, a.EMAIL from HR_EMPLOYEES a
join HR_GRADE b on a.EMP_NO = b.EMP_NO
group by YEAR, b.EMP_NO
order by SCORE desc limit 1
