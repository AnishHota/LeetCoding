# Write your MySQL query statement below
WITH T1 AS
(
    SELECT request_at,COUNT(status) AS can_num
    FROM Trips t
    WHERE Status LIKE 'cancelled_by%'
    AND client_id NOT IN
    (SELECT users_id FROM Users WHERE banned='Yes')
    AND driver_id NOT IN
    (SELECT users_id FROM Users WHERE banned='Yes')
    AND request_at>="2013-10-01" AND request_at<="2013-10-03"
    GROUP BY request_at
),
T2 AS
(
    SELECT request_at, COUNT(*) AS tot_num
    FROM Trips
    WHERE client_id NOT IN
    (SELECT users_id FROM Users WHERE banned='Yes')
    AND driver_id NOT IN
    (SELECT users_id FROM Users WHERE banned='Yes')
    AND request_at>="2013-10-01" AND request_at<="2013-10-03"
    GROUP BY request_at
)
SELECT t2.request_at AS 'DAY', ROUND(COALESCE(can_num,0)/tot_num,2) AS 'Cancellation Rate'
FROM t2
LEFT JOIN t1
ON t2.request_at = t1.request_at

