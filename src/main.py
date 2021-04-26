from src.es_db_connect import oracle_close, oracle_connect


if __name__ == '__main__':
    oracle_connect()
    oracle_close(oracle_connect())
