<!-- SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- LOGO -->
<br />
  <h3 align="center">NBA API-Database</h3>

  <p align="center">
    Stores data from NBA data API into PostrgreSQL database.
    <br />
    <a href="http://data.nba.net/10s/prod/v1/today.json"><strong>NBA Data API »</strong></a>
    <br />
    <br />
  </p>
</p>

## Overview
[`build.py`](build.py) script creates the following tables in the PostreSQL database:
* teams
* players
* coaches

[`api.py`](api.py) script calls the following endpoints from the NBA data API.
* **teams** - [/prod/v2/2019/teams.json](http://data.nba.net/10s/prod/v2/2019/teams.json)
* **leagueRosterPlayers** - [/prod/v1/2019/players.json](http://data.nba.net/10s/prod/v1/2019/players.json)
* **leagueRosterCoaches** - [/prod/v1/2019/coaches.json](http://data.nba.net/10s/prod/v1/2019/coaches.json)

[`import.py`](import.py) script imports the data recieved by the API call into the tables that were created.

### teams to `TEAMS` Table Mapping
| Source  | Target |
| ------------- | ------------- |
| `teamId`  | team_id  |
| `fullName`  | name  |
| `city` | city |
| `nickname` | nickname |
| `confName` | conference |
| `divName` | division |
| `tricode` | abbr |

### leagueRosterPlayers to `PLAYERS` Table Mapping
| Source  | Target |
| ------------- | ------------- |
| `personId`  | player_id  |
| `firstName`  | first_name  |
| `lastName` | last_name |
| `teamId` | team_id |
| `pos` | position |
| `jersey` | jersey |
| `heightFeet` | height_ft |
| `heightInches` | height_in |
| `heightMeters` | height_m |
| `weightPounds` | weight_lbs |
| `weightKilograms` | weight_kg |
| `dateOfBirthUTC` | dob_utc |
| `roundNum` | draft_round |
| `pickNum` | draft_pick |
| `teamId` | draft_team |
| `seasonYear` | draft_year |
| `nbaDebutYear` | debut_year |
| `yearsPro` | years_pro |
| `collegeName` | college_name |
| `lastAffiliation` | last_affiliation |
| `country` | country |
| `teams` | teams |
| `isActive` | is_active |

### leagueRosterCoaches to `COACHES` Table Mapping
| Source  | Target |
| ------------- | ------------- |
| `personId`  | coach_id  |
| `firstName`  | first_name  |
| `lastName` | last_name |
| `teamId` | team_id |
| `college` | college |
| `isAssistant` | is_assistant |

### Built With
* Python
* PostgreSQL database


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gilbert-hopkins
[product-screenshot]: images/screenshot.png
