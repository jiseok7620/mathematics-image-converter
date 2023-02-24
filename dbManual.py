import sqlite3
import traceback

def dbInsert(ques, school, grade, unit, answer, diff, exam1, exam2, exam3, exam4, exam5):
    try:
        # db connect
        conn = sqlite3.connect("test.db", isolation_level=None)
        cs = conn.cursor()

        # primary key(id) 찾기
        cs.execute("SELECT max(id) FROM table2")
        mId = cs.fetchall()
        mathId = int(mId[0][0])
        if mId[0][0] != None :
            mathId += 1
        else :
            mathId = 1000000
        print(mathId)

        # 데이터 넣기
        insert_list = (
            (mathId, ques, school, grade, unit, answer, diff, exam1, exam2, exam3, exam4, exam5)
        )
        cs.execute("INSERT INTO table2(id, ques, school, grade, unit, answer, diff, exam1, exam2, exam3, exam4, exam5) \
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", insert_list)

        # db close
        conn.close()

        return 1
    except:
        err_msg = traceback.print_exc()
        return err_msg

def dbSelect():
    conn = sqlite3.connect("test.db", isolation_level=None)
    cs = conn.cursor()
    cs.execute("SELECT * FROM table2")
    returnList = cs.fetchall()

    # db close
    conn.close()

    return returnList
