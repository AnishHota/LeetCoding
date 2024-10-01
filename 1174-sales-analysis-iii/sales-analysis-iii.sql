# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s
ON p.product_id = s.product_id
AND sale_date BETWEEN '2019-01-01' AND '2019-03-31'
AND p.product_id NOT IN 
(
    SELECT product_id 
    FROM Sales
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
)
GROUP BY product_id