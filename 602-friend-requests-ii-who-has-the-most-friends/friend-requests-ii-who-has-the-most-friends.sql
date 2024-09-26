# Write your MySQL query statement below
SELECT id, SUM(CNT) AS num
FROM 
(   SELECT requester_id AS id, COUNT(*) AS CNT
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT accepter_id AS id, COUNT(*) AS CNT
    FROM RequestAccepted
    GROUP BY accepter_id
) A
GROUP BY id
ORDER BY num DESC
LIMIT 1