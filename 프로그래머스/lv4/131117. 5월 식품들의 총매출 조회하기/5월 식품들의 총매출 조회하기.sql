-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, SUM(p.PRICE * o.AMOUNT) as TOTAL_SALES
FROM FOOD_PRODUCT p inner join FOOD_ORDER o
ON p.PRODUCT_ID = o.PRODUCT_ID
WHERE YEAR(o.PRODUCE_DATE) = '2022' and MONTH(o.PRODUCE_DATE) = '05'
GROUP BY p.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, p.PRODUCT_ID ASC;