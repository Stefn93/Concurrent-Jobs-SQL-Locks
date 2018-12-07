HOST=$1
USER=$2
PW=$3
DB=$4

echo "Starting simulation..."
python ./set_sql.py --sql_host $HOST --sql_user $USER --sql_pw $PW --sql_db $DB
python ./job6.py --sql_host $HOST --sql_user $USER --sql_pw $PW --sql_db $DB &
python ./job7.py --sql_host $HOST --sql_user $USER --sql_pw $PW --sql_db $DB &
python ./job8.py --sql_host $HOST --sql_user $USER --sql_pw $PW --sql_db $DB &
python ./job9.py --sql_host $HOST --sql_user $USER --sql_pw $PW --sql_db $DB &
    