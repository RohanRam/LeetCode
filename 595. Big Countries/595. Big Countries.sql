select name, population, area
from ( select name, population, area,
    case 
        when area > 3000000 then true
        when population > 25000000 then true 
        else false
        end as is_bigger from world) has_big
where is_bigger >0