DROP TABLE IF EXISTS wc_players;
DROP TABLE IF EXISTS wc_matches;
DROP TABLE IF EXISTS world_cups;
DROP TABLE IF EXISTS unique_players;

CREATE TABLE world_cups (
	index INT,
	"Year" INT,
	"Country" VARCHAR(255),
	"Winner" VARCHAR(255),
	"Second" VARCHAR(255),
	"Third" VARCHAR(255),
	"Fourth" VARCHAR(255),
	"GoalsScored" INT,
	"QualifiedTeams" INT,
	"MatchesPlayed" INT,
	"Attendance" INT,
	data_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ("Year")
);