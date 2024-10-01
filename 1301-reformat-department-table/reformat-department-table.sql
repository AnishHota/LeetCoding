# Write your MySQL query statement below
SELECT ID,
SUM(IF(month='Jan',revenue,Null)) AS Jan_Revenue,
SUM(IF(month='Feb',revenue,Null)) AS Feb_Revenue,
SUM(IF(month='Mar',revenue,Null)) AS Mar_Revenue,
SUM(IF(month='Apr',revenue,Null)) AS Apr_Revenue,
SUM(IF(month='May',revenue,Null)) AS May_Revenue,
SUM(IF(month='Jun',revenue,Null)) AS Jun_Revenue,
SUM(IF(month='Jul',revenue,Null)) AS Jul_Revenue,
SUM(IF(month='Aug',revenue,Null)) AS Aug_Revenue,
SUM(IF(month='Sep',revenue,Null)) AS Sep_Revenue,
SUM(IF(month='Oct',revenue,Null)) AS Oct_Revenue,
SUM(IF(month='Nov',revenue,Null)) AS Nov_Revenue,
SUM(IF(month='Dec',revenue,Null)) AS Dec_Revenue
FROM
Department
GROUP BY id