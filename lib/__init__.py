import sqlite3

CONN = sqlite3.connect('lib/music.db')
CURSOR = CONN.cursor()