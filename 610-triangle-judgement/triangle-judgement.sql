# Write your MySQL query statement below
SELECT x,y,z, IF(x+y>z,IF(x+z>y, IF(y+z>x,'Yes','No'),'No'),'No') AS triangle
FROM Triangle