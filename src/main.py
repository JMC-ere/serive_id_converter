from src.es_db_connect import oracle_close, oracle_connect
from src.convert_service_id import convert_service_id
from src.make_log import log_print

if __name__ == '__main__':
    logger = log_print()
    convert_service_id(oracle_connect(), logger)
    oracle_close(oracle_connect())
