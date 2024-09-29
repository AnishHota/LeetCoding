# Write your MySQL query statement below
SELECT request_at AS 'Day',
ROUND(SUM(IF(t.status LIKE 'cancelled_by%',1,0))/COUNT(t.status),2) AS 'Cancellation Rate'
FROM Trips t
JOIN Users a
ON t.client_id = a.users_id
AND a.banned = 'No'
JOIN Users b
ON t.driver_id = b.users_id
AND b.banned = 'No'
WHERE t.request_at>='2013-10-01' AND t.request_at<='2013-10-03'
GROUP BY t.request_at