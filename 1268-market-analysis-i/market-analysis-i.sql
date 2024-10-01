# Write your MySQL query statement below
SELECT user_id AS 'buyer_id', join_date,count(o.order_date) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
ON u.user_id = o.buyer_id
AND o.order_date LIKE '2019%'
GROUP BY user_id
