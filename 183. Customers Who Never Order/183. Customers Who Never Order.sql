1-- Select name as Customers from Customers Where name not in (Select c.name  
2-- from Customers as c 
3-- Right join Orders as o 
4-- on c.id = o.customerId)
5--   ;
6
7SELECT c.name AS Customers
8FROM Customers AS c
9LEFT JOIN Orders AS o
10    ON c.id = o.customerId
11WHERE o.customerId IS NULL;