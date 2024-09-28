# Write your MySQL query statement below
SELECT d.name AS Department,A.name AS Employee,A.salary
FROM
(
    SELECT departmentId,name,salary,
    DENSE_RANK() OVER(PARTITION BY departmentID ORDER BY salary DESC) AS ROW_NUM
    FROM Employee
) A
INNER JOIN
Department d
ON A.departmentId=d.id
WHERE A.ROW_NUM<4
