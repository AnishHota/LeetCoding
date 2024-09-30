# Write your MySQL query statement below
WITH T1 AS
(
    SELECT *,
    id - ROW_NUMBER() OVER(ORDER BY id) AS RNK
    FROM Stadium
    WHERE people>=100
)
SELECT id, visit_date,people
FROM T1
WHERE RNK IN (
    SELECT RNK FROM T1 GROUP BY RNK HAVING COUNT(*)>=3
)