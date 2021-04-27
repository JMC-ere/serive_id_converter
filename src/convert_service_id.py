import json
from query import es_db_query
from src.get_service_id_with_xl import read_xl


def make_dict_factory(cursor):
    column_names = [d[0] for d in cursor.description]

    def create_row(*args):
        return dict(zip(column_names, args))

    return create_row


# Oracle 쿼리를 보내 STB_ID를 구함
def convert_service_id(conn, logger):

    with open('../config/info.json', 'r') as f:
        count_info = json.load(f)

    cursor = conn.cursor()

    # 오라클 MariaDB 쿼리 in 조건 갯수 제한 Max 1000
    # service_ids를 배열로 담음
    in_count = count_info['STG']['READ_COUNT']
    service_ids = read_xl(logger)
    service_ids_partial = [service_ids[i:i + in_count] for i in range(0, len(service_ids), in_count)]

    count = 1

    data_list = []

    for partial in service_ids_partial:

        qry = es_db_query.SEARCH_SERVICE_IDS % str(partial).strip('[]')
        cursor.execute(qry)

        logger.info(f"QUERY COUNT : {count}")
        count = count + 1

        cursor.rowfactory = make_dict_factory(cursor)
        data_list.append(cursor.fetchall())

    for m in data_list:
        for n in m:
            print(n)
