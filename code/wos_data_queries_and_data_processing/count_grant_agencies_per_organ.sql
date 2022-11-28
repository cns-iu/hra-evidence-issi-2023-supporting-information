\ COPY (
	SELECT
		uid,
		grant_agency 
	FROM
		wos_core21.wos_grant_agency 
	WHERE
		uid IN ( SELECT uid FROM wos_core21.wos_summary WHERE CAST ( pubyear AS INTEGER ) >= 2018 ) 
	) TO '/N/u/yokong/wos_grant_agency.psv' 
	DELIMITER E
	'|' CSV HEADER ENCODING 'SQL-ASCII';
	
INSERT INTO cite_10_organ_grant_agency ( ref_id, organ, grant_agency ) SELECT
ref_id,
organ,
grant_agency 
FROM
	cite_10_organ
	LEFT JOIN id_grant_agency_2018_2022 ON cite_10_organ.ref_id = id_grant_agency_2018_2022.uid INSERT INTO cite_10_organ_grant_agency_clean_edge ( organ, grant_agency, weight ) SELECT
	organ,
	grant_agency,
	COUNT ( * ) AS ct 
FROM
	cite_10_organ_grant_agency_clean 
GROUP BY
	organ,
	grant_agency 
ORDER BY
	ct DESC

INSERT INTO top_50_grant_agency ( grant_agency, ct ) SELECT
grant_agency,
COUNT ( * ) AS ct 
FROM
	"cite_10_organ_grant_agency_clean" 
GROUP BY
	grant_agency 
ORDER BY
	ct DESC 
	LIMIT 51