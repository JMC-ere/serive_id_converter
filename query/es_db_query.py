SEARCH_SERVICE_ID = """
select stb_id from HANAROCMS.STB where user_service_num =  %s and rownum = 1
"""
SEARCH_SERVICE_IDS = """
SELECT STB_ID, USER_SERVICE_NUM FROM HANAROCMS.STB WHERE USER_SERVICE_NUM IN (%s)
"""