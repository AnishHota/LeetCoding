# Write your MySQL query statement below
SELECT visited_on,amount,average_amount
FROM
(SELECT visited_on,
SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
ROUND(SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) / 7,2) AS average_amount
FROM 
Customer) A
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on),INTERVAL 6 DAY)
    FROM Customer
)
GROUP BY visited_on
ORDER BY visited_on