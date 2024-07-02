# Write your MySQL query statement below
SELECT DISTINCT(A.num) AS ConsecutiveNums
FROM Logs A, Logs B, Logs C
WHERE A.num = B.num AND A.id+1=B.id
AND A.num = C.num AND B.id+1=C.id