select customer_number
from (
    select customer_number,count(order_number) as ordern from Orders group by customer_number  order by ordern desc limit 1)t;
