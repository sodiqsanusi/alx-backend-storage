-- Ranks country origins of bands,
-- Order list by the number of (non-unique) fans
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;

