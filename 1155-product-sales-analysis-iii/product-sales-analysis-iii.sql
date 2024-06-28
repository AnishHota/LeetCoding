# Write your MySQL query statement below
SELECT S.product_id, year AS first_year, quantity, price
FROM Sales S
WHERE (product_id, year) IN
(SELECT product_id, MIN(year) AS first_year
FROM Sales
GROUP BY product_id)