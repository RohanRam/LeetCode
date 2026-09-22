1SELECT name
2FROM SalesPerson
3WHERE name NOT IN (
4    SELECT s.name
5    FROM SalesPerson AS s
6    LEFT JOIN Orders AS o
7        ON s.sales_id = o.sales_id
8    LEFT JOIN Company AS c
9        ON o.com_id = c.com_id
10    WHERE c.name = RED
11);