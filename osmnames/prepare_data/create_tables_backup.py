import os

from osmnames.database.functions import vacuum_database

def create_tables_backup():
    exec_sql_from_file("create_tables_backup.sql", cwd=os.path.dirname(__file__))
	vacuum_database()
