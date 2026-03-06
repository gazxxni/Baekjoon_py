select a.APNT_NO, c.PT_NAME, a.PT_NO, a.MCDP_CD, b.DR_NAME, a.APNT_YMD
from APPOINTMENT a
join DOCTOR b on a.MDDR_ID = b.DR_ID
join PATIENT c on a.PT_NO = c.PT_NO
where a.MCDP_CD = 'CS' 
  and a.APNT_CNCL_YN = 'N' 
  and a.APNT_YMD like '2022-04-13%'
order by a.APNT_YMD