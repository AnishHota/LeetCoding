# Write your MySQL query statement below
WITH T1 AS
( 
    SELECT A.pid 
    FROM Insurance A
    INNER JOIN Insurance B
    WHERE A.pid!=B.pid
    AND A.lat = B.lat
    AND A.lon = B.lon
),
T2 AS
(
    SELECT tiv_2015,COUNT(*)
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*)>1
)
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM Insurance
WHERE pid NOT IN
( 
    SELECT pid
    FROM T1
)
AND tiv_2015 IN
(
    SELECT tiv_2015
    FROM T2
)