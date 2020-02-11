--Player History Query
SELECT  p.first_name || ' ' || p.last_name AS player,
		t.nickname,
		d.*,
		COALESCE(LEAD(d.seasonstart,1) OVER (ORDER BY d.seasonstart), 2019) - d.seasonstart AS full_seasons,
		CASE
			WHEN d.seasonend = LEAD(d.seasonstart,1) OVER (ORDER BY d.seasonstart)
				THEN 'Finished remainder of season with: ' || LEAD(t.nickname,1) OVER (ORDER BY d.seasonstart)
				ELSE NULL
		END AS season_notes
FROM    players p
CROSS JOIN lateral
        jsonb_to_recordset(LOWER(p.teams::text)::jsonb) AS d(teamid INT, seasonstart INT, seasonend INT)
LEFT JOIN teams t
ON d.teamid = t.team_id
WHERE p.first_name || ' ' || p.last_name = 'Trevor Ariza'

