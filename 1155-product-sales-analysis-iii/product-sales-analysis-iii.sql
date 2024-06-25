# Write your MySQL query statement below
SELECT S.product_id, A.first_year, quantity, price
FROM Sales S
INNER JOIN
(SELECT product_id, MIN(year) AS first_year
FROM Sales
GROUP BY product_id) A
ON S.product_id = A.product_id
AND S.year = A.first_year
