# Write your MySQL query statement below
SELECT A.employee_id, A.name, Count(*) AS reports_count, ROUND(AVG(B.age)) as average_age
FROM Employees A
INNER JOIN Employees B
ON A.employee_id = B.reports_to
GROUP BY A.employee_id
ORDER BY A.employee_id