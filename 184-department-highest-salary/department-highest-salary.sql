# Write your MySQL query statement below
SELECT D.name AS 'Department', A.name AS 'Employee', A.salary AS Salary
FROM
(
    SELECT name,salary,departmentId,
    RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS row_num
    FROM Employee
) A
INNER JOIN
Department D
ON A.departmentId = D.id
WHERE A.row_num=1