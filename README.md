# Concurrent-Jobs-SQL-Locks

This simulation is a showcase created in 8 hours and might be fixed further.

This simulation involves four python scripts which must be executed one by one since the GPU in this scenario is asssumed to be almost busy and has the possibility to run just another concurrent job. At each step, we also want to run the ID_TASK that has been scheduled first for the execution. 
The python files connect to a cloud sql instance with two tables: "audit_activity" and "pre_elaborazione". 
These tables must be created following the same format specified below in order to have a working simulation.
Once created the tables, just run the "start_concurrent simulation.sh" giving sql connection parameter in order to start.

- First parameter: "HOST", must be the IP address where the cloud sql db is hosted to.
- Second parameter: "USER", must be the user that authenticates in the database.
- Third parameter: "PW", the password used to log in the database.
- Fourth parameter: "DB", the database where the tables are.

MySQL [MY_DB]> select * from audit_activity;
+---------+-------+---------+---------------------+
| ID_TASK | fase  | azione  | data                |
+---------+-------+---------+---------------------+
| 10      | fase2 | RUNNING | 2018-12-06 17:27:08 |
| 11      | fase2 | RUNNING | 2018-12-06 17:27:08 |
| 12      | fase2 | RUNNING | 2018-12-06 17:27:08 |
| 13      | fase2 | RUNNING | 2018-12-06 17:27:08 |
| 14      | fase2 | RUNNING | 2018-12-06 17:27:08 |
| 5       | fase2 | QUEUED  | 2018-12-06 17:27:08 |
| 6       | fase2 | DONE    | 2018-12-06 17:27:20 |
| 7       | fase2 | DONE    | 2018-12-06 17:27:18 |
| 8       | fase2 | DONE    | 2018-12-06 17:27:14 |
| 9       | fase2 | DONE    | 2018-12-06 17:27:11 |
+---------+-------+---------+---------------------+


MySQL [MY_DB]> select * from pre_elaborazione;
+------+--------------+----------------+-----------------+------------------+-------------------------+-------------------+---------------+--------+
| UUID | codice_linea | data_ispezione | stato           | data_caricamento | data_inizio_elborazione | tipo_elaborazione | call_back_uri | job_id |
+------+--------------+----------------+-----------------+------------------+-------------------------+-------------------+---------------+--------+
| 0    | STEFN_LINEA  | NULL           | IN_ATTESA       | NULL             | 2018-12-05 12:50:00     | NULL              | NULL          | NULL   |
| 1    | STEFN_LINEA  | NULL           | IN_ATTESA       | NULL             | 2018-12-05 12:50:01     | NULL              | NULL          | NULL   |
| 10   | STEFN_LINEA  | NULL           | IN_ELABORAZIONE | NULL             | 2018-12-05 13:05:10     | NULL              | NULL          | NULL   |
| 11   | STEFN_LINEA  | NULL           | IN_ELABORAZIONE | NULL             | 2018-12-05 13:04:11     | NULL              | NULL          | NULL   |
| 12   | STEFN_LINEA  | NULL           | IN_ELABORAZIONE | NULL             | 2018-12-05 13:03:12     | NULL              | NULL          | NULL   |
| 13   | STEFN_LINEA  | NULL           | IN_ELABORAZIONE | NULL             | 2018-12-05 13:02:13     | NULL              | NULL          | NULL   |
| 14   | STEFN_LINEA  | NULL           | IN_ELABORAZIONE | NULL             | 2018-12-05 13:01:14     | NULL              | NULL          | NULL   |
| 15   | STEFN_LINEA  | NULL           | ELABORATO       | NULL             | 2018-12-05 13:05:15     | NULL              | NULL          | NULL   |
| 16   | STEFN_LINEA  | NULL           | ELABORATO       | NULL             | 2018-12-05 13:05:16     | NULL              | NULL          | NULL   |
| 17   | STEFN_LINEA  | NULL           | ELABORATO       | NULL             | 2018-12-05 13:05:17     | NULL              | NULL          | NULL   |
| 18   | STEFN_LINEA  | NULL           | ELABORATO       | NULL             | 2018-12-05 13:05:18     | NULL              | NULL          | NULL   |
| 19   | STEFN_LINEA  | NULL           | ELABORATO       | NULL             | 2018-12-05 13:05:19     | NULL              | NULL          | NULL   |
| 2    | STEFN_LINEA  | NULL           | IN_ATTESA       | NULL             | 2018-12-05 12:50:02     | NULL              | NULL          | NULL   |
| 3    | STEFN_LINEA  | NULL           | IN_ATTESA       | NULL             | 2018-12-05 12:50:03     | NULL              | NULL          | NULL   |
| 4    | STEFN_LINEA  | NULL           | IN_ATTESA       | NULL             | 2018-12-05 12:50:04     | NULL              | NULL          | NULL   |
| 5    | STEFN_LINEA  | NULL           | TRASFERIMENTO   | NULL             | 2018-12-05 12:55:05     | NULL              | NULL          | NULL   |
| 6    | STEFN_LINEA  | NULL           | TRASFERIMENTO   | NULL             | 2018-12-05 12:54:06     | NULL              | NULL          | NULL   |
| 7    | STEFN_LINEA  | NULL           | TRASFERIMENTO   | NULL             | 2018-12-05 12:53:07     | NULL              | NULL          | NULL   |
| 8    | STEFN_LINEA  | NULL           | TRASFERIMENTO   | NULL             | 2018-12-05 12:52:08     | NULL              | NULL          | NULL   |
| 9    | STEFN_LINEA  | NULL           | TRASFERIMENTO   | NULL             | 2018-12-05 12:51:09     | NULL              | NULL          | NULL   |
+------+--------------+----------------+-----------------+------------------+-------------------------+-------------------+---------------+--------+
