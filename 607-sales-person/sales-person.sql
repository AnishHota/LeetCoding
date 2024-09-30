# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE name NOT IN
(
    SELECT sp.name
    FROM SalesPerson sp
    JOIN Orders o
    ON sp.sales_id = o.sales_id
    JOIN Company c
    ON o.com_id = c.com_id
    AND c.name = 'RED'
)
