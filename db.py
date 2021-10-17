from sqlite_simple.simplifer import AdvancedDispatcher
import sqlite3


conn = sqlite3.connect('db.db', check_same_thread=False )
cur = conn.cursor()
disp = AdvancedDispatcher(conn, cur)

@disp.init
@disp.write
def create_recept_table():
  return "CREATE TABLE recepts(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, inside VARCHAR)"

@disp.write
def new_recept(name, data):
  return F"INSERT INTO recepts (name, inside) VALUES ('{name}', '{data}')"

@disp.read
def get_recept_by_id(id_):
 return f"SELECT * FROM recepts WHERE id={id_}"
