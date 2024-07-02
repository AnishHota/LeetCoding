# Write your MySQL query statement below
SELECT max(A.num) as num FROM 
(   
    SELECT num,Count(num)
    FROM MyNumbers
    GROUP BY num
    HAVING Count(num)<2
) A