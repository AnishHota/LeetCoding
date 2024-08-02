# Write your MySQL query statement below
SELECT 'High Salary' AS category,COALESCE(COUNT(*),0) AS accounts_count
FROM Accounts
WHERE income>50000
UNION ALL
SELECT 'Low Salary' AS category,COALESCE(COUNT(*),0) AS accounts_count
FROM Accounts
WHERE income<20000
UNION ALL
SELECT 'Average Salary' AS category,COALESCE(COUNT(*),0) AS accounts_count
FROM Accounts
WHERE income>=20000 AND income<=50000
