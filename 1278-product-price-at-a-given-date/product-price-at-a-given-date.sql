-- # Write your MySQL query statement below
SELECT product_id, price
FROM
(
    SELECT product_id,new_price AS price, RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS R, change_date
    FROM Products
    WHERE change_date<='2019-08-16'
) A
WHERE A.R =1
UNION
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING min(change_date)>'2019-08-16'
