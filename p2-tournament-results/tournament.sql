-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


--CREATE DATABASE tournament;

DROP TABLE matches CASCADE;
DROP TABLE players CASCADE;
DROP TABLE match_player CASCADE;

CREATE TABLE players (
	id serial PRIMARY KEY,
	name varchar(128) NOT NULL,
	data_added timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE matches (
	id serial PRIMARY KEY,
	data_added timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE match_player (
	match_id integer NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
	player_id integer NOT NULL REFERENCES players(id) ON DELETE CASCADE,
	is_win boolean NOT NULL DEFAULT 0,
	data_added timestamp DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (match_id, player_id)
);


-- \i tournament.sql
-- \d
-- \d players



