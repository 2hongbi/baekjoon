-- 코드를 작성해주세요
select id, 
case
    when colony_rank = 1 then 'CRITICAL'
    when colony_rank = 2 then 'HIGH'
    when colony_rank = 3 then 'MEDIUM'
    else 'LOW'
end as COLONY_NAME
from (select id, NTILE(4) over (order by size_of_colony desc) colony_rank
     from ecoli_data) sq
 order by id asc;