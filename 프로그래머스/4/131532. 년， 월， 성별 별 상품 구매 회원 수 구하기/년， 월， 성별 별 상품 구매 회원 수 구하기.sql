-- 코드를 입력하세요
SELECT YEAR(o.SALES_DATE) as YEAR, 
    MONTH(o.SALES_DATE) as MONTH, 
    u.GENDER as GENDER,
    COUNT(DISTINCT o.USER_ID) as USERS
FROM USER_INFO u
JOIN ONLINE_SALE o
ON u.USER_ID = o.USER_ID
WHERE u.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;