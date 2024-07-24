# Write your MySQL query statement below
SELECT A.person_name
FROM 
(   
    SELECT person_id, person_name, turn, sum(weight) OVER(ORDER BY turn) AS cumm
    FROM Queue
    ORDER BY turn
) A
WHERE A.cumm<=1000
ORDER BY A.turn DESC
LIMIT 1
