# Write your MySQL query statement below

WITH CTE AS
(
    SELECT DISTINCT a.id
    FROM Tree a 
    INNER JOIN Tree b
    WHERE a.id = b.p_id
    AND a.p_id IS NOT NULL
)
SELECT id,
IF(p_id IS NULL,'Root',IF(id IN (SELECT id FROM CTE),'Inner','Leaf')) AS type
FROM
Tree

