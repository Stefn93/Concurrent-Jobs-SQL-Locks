import pymysql
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sql_user", type=str, required=True)
parser.add_argument("--sql_pw", type=str, required=True)
parser.add_argument("--sql_db", type=str, required=True)
parser.add_argument("--sql_host", type=str, required=True)

args = parser.parse_args()

connection = pymysql.connect(host=opt.sql_host,
                             user=opt.sql_user,
                             password=opt.sql_pw,
                             db=opt.sql_db)

def print_rows(cur):
    cur.execute("SELECT ID_TASK,azione FROM audit_activity;")
    rows = cur.fetchall()
    for row in rows:
        print("{0}".format(row[:]))
        
def init_audit(cur):
    cur.execute("DELETE FROM audit_activity;")
    connection.commit()
    sql = "INSERT INTO `audit_activity` (`ID_TASK`, `fase`, `azione`) VALUES (%s, %s, %s)"
    
    l = []
   # for i in range(0, 5):
   #     l.append((str(i), 'fase1', 'DONE'))
    for i in range(5, 10):
        l.append((str(i), 'fase2', 'QUEUED'))
    for i in range(10, 15):
        l.append((str(i), 'fase2', 'RUNNING'))
   # for i in range(15, 20):
   #     l.append((str(i), 'fase2', 'SUCCEEDED')) 

    for elem in l:
        cur.execute(sql, elem)
    connection.commit()

def init_pre_elab(cur):

    # Create a new record
    cur.execute("DELETE FROM pre_elaborazione;")
    connection.commit()

    sql = "INSERT INTO `pre_elaborazione` (`UUID`, `codice_linea`, `stato`, `data_inizio_elborazione`) VALUES (%s, %s, %s, %s)"

    l = []
    for i in range(0, 5):
        l.append((str(i), 'STEFN_LINEA', 'IN_ATTESA', datetime.strptime('05/12/2018 12:50:0'+str(i), '%d/%m/%Y %H:%M:%S')))
    for i in range(5, 10):
        l.append((str(i), 'STEFN_LINEA', 'TRASFERIMENTO', datetime.strptime('05/12/2018 12:5'+ str(10-i) +':0'+str(i), '%d/%m/%Y %H:%M:%S')))
    for i in range(10, 15):
        l.append((str(i), 'STEFN_LINEA', 'IN_ELABORAZIONE', datetime.strptime('05/12/2018 13:0'+str(15-i)+':'+str(i), '%d/%m/%Y %H:%M:%S')))
    for i in range(15, 20):
        l.append((str(i), 'STEFN_LINEA', 'ELABORATO', datetime.strptime('05/12/2018 13:05:'+str(i), '%d/%m/%Y %H:%M:%S'))) 

    for elem in l:
        cur.execute(sql, elem)

    connection.commit()
    

BATCH_ID = 9
MAX_PARALLEL_JOBS = 6

with connection.cursor() as cur: 
    init_audit(cur)
    init_pre_elab(cur)
    print_rows(cur)
connection.close()