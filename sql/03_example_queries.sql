-- Row count
SELECT COUNT(*) FROM usgs.earthquakes;

-- Top 5 largest earthquakes
SELECT event_id, time, magnitude, magtype, location
FROM usgs.earthquakes
ORDER BY magnitude DESC NULLS LAST
LIMIT 5;

-- Events by month
SELECT month, COUNT(*) AS events
FROM usgs.earthquakes
GROUP BY month
ORDER BY month;
