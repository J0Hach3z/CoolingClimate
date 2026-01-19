CREATE TABLE degree_hours_bel AS (
SELECT 
	*,
	CASE 
		WHEN (EXTRACT(HOUR FROM time) < 8 OR EXTRACT(HOUR FROM time) >= 20) 
			 OR EXTRACT(DOW FROM time) > 5 THEN GREATEST(value - 30, 0)
		ELSE GREATEST(value - 25, 0)
	END AS CDH,
	CASE 
		WHEN (EXTRACT(HOUR FROM time) < 8 OR EXTRACT(HOUR FROM time) >= 20) 
			 OR EXTRACT(DOW FROM time) > 5 THEN GREATEST(9 - value, 0)
		ELSE GREATEST(15 - value, 0)
	END AS HDH
FROM belgium_res
WHERE variable = '2m Temperature')
