-- USE company;

-- 1
SELECT AirportName, COUNT(RouteID) as num_rutes, airport.NumTerminals
FROM airport
JOIN route ON route.FromAirport = airport.AirportID
WHERE NumTerminals > 2 
GROUP BY AirportName
ORDER BY num_rutes DESC, NumTerminals;

-- 2
SELECT COUNT(flight.FlightID), route.RouteID, route.Distance
FROM flight
JOIN route ON flight.RouteID = route.RouteID
WHERE route.Distance = (SELECT MAX(route.Distance) FROM route);

-- 3
SELECT AircraftName, COUNT(AircraftName) as num_of_airplanes
FROM aircrafttype
LEFT JOIN aircraft ON aircrafttype.aircrafttypeID = aircraft.aircrafttypeID
GROUP BY AircraftName
ORDER BY num_of_airplanes DESC;

-- 4
SELECT AircraftName, COUNT(AircraftName) as num_of_airplanes
FROM aircraft
RIGHT JOIN aircrafttype ON aircrafttype.aircrafttypeID = aircraft.aircrafttypeID
GROUP BY AircraftName
ORDER BY num_of_airplanes DESC;

-- 5
SELECT DepDay, COUNT(FlightID) AS num_of_flights
FROM flightdep
GROUP BY DepDay
HAVING num_of_flights > (
	SELECT COUNT(FlightID)/COUNT(DISTINCT DepDay)
	FROM flightdep);

-- 6
SELECT *
FROM flight
JOIN route ON route.RouteID = flight.RouteID
WHERE FromAirport = (
	SELECT AirportID
	FROM airport
	WHERE AirportName LIKE '%Heathrow%')
    OR ToAirport = (
	SELECT AirportID
	FROM airport
	WHERE AirportName LIKE '%Heathrow%')
ORDER BY FlightID DESC;

-- 7
SELECT route.RouteID, Distance, route.FromAirport, airport_from.AirportCode as FromAirportCode, airport_from.AirportName as FromAirportName, airport_from.CityName as FromCityName, 
route.ToAirport, airport_to.AirportCode as ToAirportCode, airport_to.AirportName as ToAirportName, airport_to.CityName as ToCityName
FROM airport airport_from
JOIN route ON route.FromAirport = airport_from.AirportID
JOIN airport airport_to ON route.ToAirport = airport_to.AirportID
WHERE route.Status = 1
ORDER BY Distance;

-- 8
SELECT flightdep.FlightID, airport_from.AirportID as FromAirportID, airport_from.AirportName as FromAirportName, 
airport_to.AirportID as ToAirportID, airport_to.AirportName as ToAirportName, route.Distance, route.Duration, DepDay, DepTime
FROM flightdep
JOIN route ON flightdep.FlightID = route.RouteID
JOIN airport airport_from ON airport_from.AirportID = route.FromAirport
JOIN airport airport_to ON airport_to.AirportID = route.ToAirport
WHERE airport_from.AirportName LIKE '%Heathrow%'
	AND 
    ((DepDay IN (1, 3, 5) AND DATE('08:00:00') <= DepTime <= DATE('19:00:00')) 
    OR
    (DepDay IN (2, 4, 6) AND DATE('10:00:00') <= DepTime <= DATE('16:00:00')))
    AND route.Status = 1
ORDER BY DepDay DESC, DepTime;

-- 9
SELECT flight.FlightID, route.RouteID, a_from.AirportName as FromAirport, a_to.AirportName as ToAirport, 
route.Distance, DepDay, DepTime, aircraft.RegNum
FROM flight
JOIN flightdep ON flight.FlightID = flightdep.FlightID
JOIN route ON flight.RouteID = route.RouteID
JOIN airport a_from ON route.FromAirport = a_from.AirportID
JOIN airport a_to ON route.ToAirport = a_to.AirportID
JOIN aircraft ON flight.AircraftID = aircraft.AircraftID
WHERE route.Status = 1
ORDER BY DepDay, DepTime;

-- 10
SELECT flight.FlightID, route.RouteID, a_from.AirportName as FromAirport, a_to.AirportName as ToAirport, 
route.Distance, DepDay, DepTime, aircraft.RegNum
FROM flight
JOIN flightdep ON flight.FlightID = flightdep.FlightID
JOIN route ON flight.RouteID = route.RouteID
JOIN airport a_from ON route.FromAirport = a_from.AirportID
JOIN airport a_to ON route.ToAirport = a_to.AirportID
JOIN aircraft ON flight.AircraftID = aircraft.AircraftID
WHERE route.Status = 1 
	AND DepDay IN (5, 6, 7) 
    AND (a_from.AirportName LIKE '%Orly%' OR a_from.AirportName LIKE '%Côte d\'Azur%')
    AND DATE('09:00:00') <= DepTime <= DATE('15:00:00')
ORDER BY DepDay, DepTime;




