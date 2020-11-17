import sqlite3

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))

        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e);
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(item):
     try:
         conn  = sqlite3.connect(DB_PATH)
         c = conn.cursor()
         c.execute("select status from items where item = '%s'" % item)
         status = c.fetchone()[0]
         return status

     except Exception as e:
        print('Error: ', e)
        return None

def delete_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where item=?', (item,))
        conn.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None


