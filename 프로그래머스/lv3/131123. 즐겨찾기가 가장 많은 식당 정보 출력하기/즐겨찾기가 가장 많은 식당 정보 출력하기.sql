-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO a
WHERE favorites = (select max(favorites) from REST_INFO b
                  where a.food_type = b.food_type)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC;