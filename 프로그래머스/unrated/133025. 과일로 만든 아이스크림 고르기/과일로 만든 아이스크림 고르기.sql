-- 코드를 입력하세요
SELECT FH.FLAVOR as FLAVOR
FROM FIRST_HALF FH, ICECREAM_INFO ICI
WHERE FH.FLAVOR = ICI.FLAVOR AND FH.TOTAL_ORDER > 3000 and ICI.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;
