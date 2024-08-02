# Write your MySQL query statement below

SELECT A.name AS results FROM
(
    SELECT m.user_id, u.name, COUNT(*) AS CNT
    FROM MovieRating m
    INNER JOIN
    USERS u
    ON m.user_id=u.user_id
    GROUP BY m.user_id, u.name
    ORDER BY CNT DESC, u.name ASC 
    LIMIT 1
) A
UNION ALL
SELECT B.title AS results FROM
(
    SELECT mr.movie_id,m.title,mr.created_at,AVG(rating) AS avg_rating
    FROM MovieRating mr
    INNER JOIN Movies m
    ON mr.movie_id = m.movie_id
    AND YEAR(mr.created_at) = "2020" AND MONTH(mr.created_at)="02"
    GROUP BY mr.movie_id
    ORDER BY avg_rating DESC, m.title ASC
    LIMIT 1
) B




