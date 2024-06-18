# Write your MySQL query statement below
SELECT A.user_id, Round(B.con_cnt/A.tot_cnt,2) AS confirmation_rate
FROM
(
    SELECT s.user_id, COUNT(*) AS tot_cnt
    FROM Signups s 
    LEFT JOIN Confirmations c
    ON s.user_id = c.user_id 
    GROUP BY s.user_id
) A
INNER JOIN
(
    SELECT s.user_id, COUNT(c.action) AS con_cnt
    FROM Signups s 
    LEFT JOIN Confirmations c
    ON s.user_id = c.user_id AND c.action='confirmed'
    GROUP BY s.user_id
) B
ON A.user_id = B.user_id
GROUP BY A.user_id