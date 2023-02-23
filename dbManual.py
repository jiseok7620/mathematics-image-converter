import sqlite3

def dbTest():
    print("db")

    ## --DATABASE--
    # https://hleecaster.com/python-sqlite3/ 참고
    # DB 생성
    conn = sqlite3.connect("test.db", isolation_level=None)  # isolation_level=None : 자동커밋

    # 커서 획득
    cs = conn.cursor()

    # 테이블 생성
    cs.execute("CREATE TABLE IF NOT EXISTS table1 \
                   (id integer PRIMARY KEY, name text)")
    # 데이터 삽입
    cs.execute("INSERT INTO table1 \
                   VALUES(1, 'LEE')")
    # 데이터 조회
    cs.execute("SELECT * FROM table1")
    print(cs.fetchall())

    cs.execute("SELECT * FROM table1")
    for row in cs.fetchall():
        print(row)