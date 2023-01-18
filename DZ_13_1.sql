USE company;

-- 3
SELECT RouteID, Distance 
FROM route
WHERE Distance > (
	SELECT AVG(Distance)
    FROM route
)
ORDER BY Distance DESC;


-- 5
SELECT *
FROM route
WHERE Distance > (
	SELECT AVG(Distance)
    FROM route
);
