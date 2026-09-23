1-- update Salary 
2-- set sex = case
3--     when sex = 'm' then 'f'
4--     when sex = 'f' then 'm'
5-- end;
6
7update Salary 
8set sex = IF(sex = 'f','m','f');
9
10