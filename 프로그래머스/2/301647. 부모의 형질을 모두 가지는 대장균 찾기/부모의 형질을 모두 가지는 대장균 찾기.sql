-- 코드를 작성해주세요
select c.id, c.genotype, c.parent_genotype
from (
    select a.id, a.parent_id, a.genotype, b.genotype as parent_genotype
    from ecoli_data as a
    left join ecoli_data as b
    on a.parent_id = b.id
) as c
where c.genotype & c.parent_genotype = c.parent_genotype
order by c.id asc;