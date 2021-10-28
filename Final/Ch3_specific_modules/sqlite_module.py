from sqlite3 import connect


conn = connect(":memory:", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    UserID integer primary key not null,
    MsgID  integer not null
) 
""")

cur.execute("INSERT INTO messages VALUES (:UserID, :MsgID)", {"UserID": 1234, "MsgID": 321})

cur.execute("SELECT MsgID FROM messages WHERE UserID = :UserID", {"UserID": 1234})
print(cur.fetchone()[0])
