-- delete from sensor_data;

WITH RECURSIVE
  date_range(d) AS (
    VALUES(DATE('2023-01-01')) -- Start date (change as needed)
    UNION ALL
    SELECT DATE(d, '+1 day')
    FROM date_range
    WHERE d < DATE('2023-04-30') -- End date (change as needed)
  )
INSERT INTO sensor_data (sensor_id, distance, created_date)
SELECT
    1, -- Sensor ID
    ABS(RANDOM())%(10-0) + 0, -- Random distance between 0 and 10 with 2 decimal places
    d -- Random date within the month's range
FROM date_range;

