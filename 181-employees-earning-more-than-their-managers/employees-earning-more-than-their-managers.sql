# Write your MySQL query statement below
SELECT a.name as 'Employee'
FROM Employee a
INNER JOIN Employee b
WHERE a.managerId = b.id
AND a.salary > b.salary