#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cur = DB.cursor()

    cur.execute("DELETE FROM matches;")

    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cur = DB.cursor()

    cur.execute("DELETE FROM players;")

    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    cur = DB.cursor()

    cur.execute("SELECT COALESCE(count(*)) FROM players")

    rows = cur.fetchall()
    DB.close()

    for row in rows:
        count = row[0]

    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cur = DB.cursor()

    cur.execute("INSERT INTO players (name) values (%s);", 
        (bleach.clean(name),))

    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB = connect()
    cur = DB.cursor()

    cur.execute('''
        SELECT P.id, P.name, 
            COUNT(CASE WHEN MP.is_win THEN 1 ELSE NULL END) AS wins,
            COUNT(MP.player_id) AS matches
        FROM players AS P
        LEFT JOIN match_player AS MP ON MP.player_id = P.id
        GROUP BY P.id
        ORDER BY wins DESC;
        ''')

    rows = cur.fetchall()
    DB.close()

    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    cur = DB.cursor()

    # insert record in to matches
    cur.execute("INSERT INTO matches DEFAULT VALUES;")

    # insert record in to match_players (winner) 
    # with matches id (just inserted)
    cur.execute('''
        INSERT INTO match_player (match_id, player_id, is_win) 
        VALUES (currval(pg_get_serial_sequence('matches','id')), %s, '1');
        ''', (bleach.clean(winner),))

    # insert record in to match_players (looser) 
    # with matches id (just inserted)
    cur.execute('''
        INSERT INTO match_player (match_id, player_id, is_win)
        VALUES (currval(pg_get_serial_sequence('matches','id')), %s, '0');
        ''',(bleach.clean(loser),))

    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = playerStandings()
    pairing = []

    for i in range(0, (len(standings)), 2):
        pairing.append(
            [standings[i][0], standings[i][1], 
            standings[i+1][0], standings[i+1][1]])

    return pairing

