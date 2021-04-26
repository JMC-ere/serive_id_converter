SEARCH_SERVICE_ID="""
select stb_id from HANAROCMS.STB where user_service_num =  %s and rownum = 1
"""