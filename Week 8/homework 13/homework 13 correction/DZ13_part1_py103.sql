USE company;

-- 1
INSERT INTO class (ClassID, ClassName) 
VALUES (NULL, 'Regular');
UPDATE pax
SET pax.ClassID = (
	SELECT ClassID FROM class 
    WHERE ClassName = 'Regular')
WHERE pax.ClassID IN (
	SELECT ClassID FROM class 
    WHERE ClassName = 'Gold' OR ClassName = 'Silver');

-- 2
UPDATE aircraft
SET AircraftTypeID = (
	SELECT AircraftTypeID FROM aircrafttype 
    WHERE AircraftName LIKE '%330%')
WHERE AircraftTypeID IN (
	SELECT AircraftTypeID FROM aircrafttype 
	WHERE AircraftName LIKE 'Boeing%' 
	OR AircraftName LIKE '%M%' 
	OR AircraftName LIKE '%W%');

-- 3
SELECT RouteID, Distance 
FROM route
WHERE Distance > (
	SELECT AVG(Distance)
    FROM route)
ORDER BY Distance DESC;

-- 4
SELECT flight.FlightID, route.FromAirport, route.ToAirport, airport.AirportName
FROM flight, route, airport
WHERE flight.RouteId = route.RouteId 
AND airport.AirportName LIKE 'Heathrow%' 
AND (airport.AirportID = route.FromAirport 
	OR airport.AirportID = route.ToAirport)
ORDER BY flight.FlightID DESC;

-- 5
SELECT *
FROM route
WHERE Distance > (
	SELECT AVG(Distance)
    FROM route);
    
-- 6
SELECT flight.*
FROM flight
JOIN aircraft ON flight.AircraftID = aircraft.AircraftID
JOIN aircrafttype ON aircraft.AircraftTypeID = aircrafttype.AircraftTypeID
WHERE aircrafttype.aircraftName LIKE '%SW%';
