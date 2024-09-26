# Write your MySQL query statement below
SELECT A.product_name, B.unit
FROM Products A
JOIN (
    SELECT product_id,SUM(unit) AS unit
    FROM Orders
    WHERE order_date LIKE "2020-02%"
    GROUP BY product_id
) B
ON A.product_id = B.product_id
AND B.unit>=100