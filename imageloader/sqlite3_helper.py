import sqlite3 as lite

def connect():
    conn = lite.connect('db.sqlite3')
    cur = conn.cursor()
    return cur


def get_images():
    cur = connect()
    cur.execute("SELECT * FROM imageloader_image")
    return cur.fetchall()


def get_pipelines():
    cur = connect()
    cur.execute("SELECT * FROM imageloader_pipeline")
    return cur.fetchall()