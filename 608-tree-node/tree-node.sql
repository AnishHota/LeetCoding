# Write your MySQL query statement below
SELECT id,
IF(p_id IS NULL,'Root',IF(id IN (SELECT p_id FROM TREE),'Inner','Leaf')) AS type
FROM
Tree

