# Write your MySQL query statement below
SELECT COALESCE(MAX(salary),NULL) AS SecondHighestSalary
FROM Employee
WHERE salary <> (SELECT MAX(salary) FROM Employee)