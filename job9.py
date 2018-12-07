import pymysql
import logging
import time
import random
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


BATCH_ID = 9
MAX_PARALLEL_JOBS = 6
flag = False
MAX_RETRIES = 5
retries = 0


def print_rows(cur):
    cur.execute("SELECT ID_TASK,azione FROM audit_activity where ID_TASK=9 or ID_TASK=6 or ID_TASK=7 or ID_TASK=8;")
    rows = cur.fetchall()
    print "Inizio 1 "
    for row in rows:
        print("{0}".format(row[:]))
    print "Fine 1 "

while flag == False and retries < MAX_RETRIES:
    with connection.cursor() as cur: 
        try:
            print "\nINIZIO RUSCO 1"
            
            time.sleep(random.randint(2, 5))
            #############################  LOCK  ##################################
            cur.execute("LOCK TABLES audit_activity WRITE, pre_elaborazione READ;")
            #######################################################################
            
            print_rows(cur)

            cur.execute("SELECT audit_activity.ID_TASK "+
                        "FROM audit_activity " + 
                        "JOIN pre_elaborazione " +
                        "ON audit_activity.ID_TASK=pre_elaborazione.UUID "+
                        "WHERE audit_activity.fase='fase2' AND audit_activity.azione='QUEUED' " + 
                        "ORDER BY pre_elaborazione.data_inizio_elborazione ASC;")
            rows = cur.fetchall()
            if str(rows[0][0]) == str(BATCH_ID):
                # raise
                cur.execute("SELECT COUNT(*) "#, audit_activity.ID_TASK, audit_activity.fase, audit_activity.azione " +
                            "FROM audit_activity " + 
                            "WHERE fase='fase2' AND azione='RUNNING';")

                rows = cur.fetchall()
                running_count = rows[0][0]

                print "running count: " + str(running_count)
                if running_count < MAX_PARALLEL_JOBS:
                    cur.execute("UPDATE audit_activity SET azione='RUNNING' " +
                                "WHERE azione='QUEUED' " +
                                "AND ID_TASK=9 " +
                                "AND (SELECT COUNT(*) WHERE fase='fase2' AND azione='RUNNING') < " + str(MAX_PARALLEL_JOBS) + ";")
                    print_rows(cur)      
                    flag = True
                else:
                    logging.warn("Non eseguo il job perche la GPU puzza")

            print "FINE RUSCO 1" 
        except:
            logging.warn("RETRYING 1")
            time.sleep(1)
            retries += 1
            if retries >= MAX_RETRIES:
                cur.execute("UPDATE audit_activity SET azione='FAILED' " +
                            "WHERE azione='QUEUED' " +
                            "AND ID_TASK=9;")
        finally:
            cur.execute("UNLOCK TABLES;")
            
            
print "Eseguo il job"
with connection.cursor() as cur: 
    cur.execute("UPDATE audit_activity SET azione='DONE' " +
        "WHERE azione='RUNNING' " +
        "AND ID_TASK=9;")
    print_rows(cur)
            
        
connection.commit()
connection.close()
