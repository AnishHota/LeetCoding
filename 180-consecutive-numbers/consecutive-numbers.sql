# Write your MySQL query statement below
SELECT DISTINCT(A.num) AS ConsecutiveNums
FROM Logs A
INNER JOIN Logs B
ON A.num = B.num AND A.id+1=B.id
INNER JOIN Logs C
ON A.num = C.num AND A.id+2=C.id AND B.id+1=C.id