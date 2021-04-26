import cx_Oracle
import json
from query import es_db_query
from src.make_log import log_print


def oracle_connect():
    with open('../config/info.json', 'r') as f:
        oracle_info = json.load(f)

    try:
        # DB Connect
        conn = cx_Oracle.connect(oracle_info['STG']['DB_USER'],
                                 oracle_info['STG']['DB_PW'],
                                 oracle_info['STG']['DB_HOST'],
                                 encoding='UTF-8')

        cursor = conn.cursor()

        test = cursor.exexute(es_db_query.SEARCH_SERVICE_ID % '100601051470')

        print(test)

        return conn

    except ConnectionError as conn_err:
        log_print().info("ORACLE CONNECT ERROR :", conn_err)
        exit()

    except Exception as err:
        log_print().info("mysql_connect function ERROR :", err)
        exit()


# DB Close Function
def oracle_close(conn):

    try:
        conn.close()
        pass
    except Exception as close_err:
        log_print().info(close_err)


