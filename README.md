# Concurrent-Jobs-SQL-Locks

This simulation is a showcase created in 8 hours and might be fixed further.

This simulation involves four python scripts which must be executed one by one since the GPU in this scenario is asssumed to be almost busy and has the possibility to run just another concurrent job. At each step, we also want to run the ID_TASK that has been scheduled first for the execution. 
The python files connect to a cloud sql instance with two tables: "audit_activity" and "pre_elaborazione". 
These tables must be created following the same format specified in the file "tables.txt" in order to have a working simulation.
Once created the tables, just run the "start_concurrent simulation.sh" giving sql connection parameter in order to start.

- First parameter: "HOST", must be the IP address where the cloud sql db is hosted to.
- Second parameter: "USER", must be the user that authenticates in the database.
- Third parameter: "PW", the password used to log in the database.
- Fourth parameter: "DB", the database where the tables are.
