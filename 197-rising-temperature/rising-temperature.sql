# Write your MySQL query statement below
SELECT a.id
FROM Weather a
INNER JOIN Weather b
ON a.recordDate = DATE_SUB(b.recordDate,INTERVAL -1 DAY)
WHERE a.temperature>b.temperature
