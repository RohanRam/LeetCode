1select max(num) as num from MyNumbers where num in (select num from MyNumbers
2group by num 
3having count(*) = 1) ; 