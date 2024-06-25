# Write your MySQL query statement below
WITH immediate_orders AS (SELECT customer_id, IF(min(order_date)=min(customer_pref_delivery_date),1,0) AS immediate
FROM Delivery
GROUP BY customer_id)
SELECT ROUND((sum(immediate)*100)/count(*),2) AS immediate_percentage
FROM immediate_orders;



