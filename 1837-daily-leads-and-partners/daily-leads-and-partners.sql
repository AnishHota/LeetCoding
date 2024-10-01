# Write your MySQL query statement below
SELECT A.date_id, A.make_name, A.unique_leads,B.unique_partners
FROM
(SELECT date_id, make_name,COUNT(DISTINCT lead_id) AS unique_leads
FROM DailySales
GROUP BY date_id, make_name
) A
INNER JOIN
( SELECT date_id, make_name,COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name
) B
ON A.date_id = B.date_id
AND A.make_name = B.make_name
