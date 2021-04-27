import cx_Oracle
import os
import json
from query import es_db_query
from src.make_log import log_print


def oracle_connect():

    # oracle client 관련
    LOCATION = r"C:/instantclient_19_10"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  # 환경변수 등록

    with open('../config/info.json', 'r') as f:
        oracle_info = json.load(f)

    try:
        # DB Connect
        conn = cx_Oracle.connect(oracle_info['STG']['DB_USER'],
                                 oracle_info['STG']['DB_PW'],
                                 oracle_info['STG']['DB_HOST'],
                                 encoding='UTF-8')

        return conn
    except TimeoutError as time_err:
        log_print().error("ORACLE TIME OUT ERROR :", time_err)

    except ConnectionError as conn_err:
        log_print().error("ORACLE CONNECT ERROR :", conn_err)

    except Exception as err:
        log_print().error("mysql_connect function ERROR :", err)


# DB Close Function
def oracle_close(conn):

    try:
        conn.close()
        pass
    except Exception as close_err:
        log_print().error(close_err)


