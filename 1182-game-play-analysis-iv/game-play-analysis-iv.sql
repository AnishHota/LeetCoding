# Write your MySQL query statement below

SELECT ROUND(COUNT(*)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM 
(SELECT player_id, min(event_date) AS first_date
FROM Activity
GROUP BY player_id) A
INNER JOIN Activity
ON A.player_id = Activity.player_id
AND A.first_date = DATE_ADD(Activity.event_date, INTERVAL -1 DAY)