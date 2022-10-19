from flask import flash
from model.mysql import conn_mysql

class Personal_plan():
    def __init__(self, plan_key,cat_key, content, date):
        self.key = plan_key
        self.cate = cat_key
        self.content = content
        self.date = date
        
    @staticmethod
    def get_b_key(cat_key):
        mysql_db = conn_mysql()
        db_cursor = mysql_db.cursor()
        sql = "select * from personal_plan where cat_key = '" + str(cat_key) + "'"
        db_cursor.execute(sql)
        print(sql)
        plan = db_cursor.fetchall()
        print(plan)
        if not plan:
            return None
        return plan
    
    #카테고리 생성
    @staticmethod
    def create(cate, content, date):
        # mysql DB 연결
        conn = conn_mysql()
        # 커서
        cursor = conn.cursor()
        query2 = f"INSERT INTO personal_plan VALUES('None','{cate}', '{content}','{date}');"
        print(query2)
        cnt2 = cursor.execute(query2)    # 쿼리 실행개수 (0:DB오류 / 1:정상)
        conn.commit()


    @staticmethod
    def edit(cate, cat_key):
        print("category edit")
        # mysql DB 연결
        conn = conn_mysql()
        # 커서
        cursor = conn.cursor()
        query = f"UPDATE personal_plan set cate = '{cate}' WHERE cat_key = '{cat_key}';"
        cnt = cursor.execute(query)
        conn.commit()
        
    @staticmethod
    def delete(plan_key):
        # mysql DB 연결
        conn = conn_mysql()
        # 커서
        cursor = conn.cursor()
        query = f"SELECT * FROM personal_plan WHERE plan_key = '{plan_key}';"
        cnt = cursor.execute(query)
        if cnt==1:
            query2 = f"DELETE FROM personal_plan WHERE plan_key = '{plan_key}';"
            cnt2 = cursor.execute(query2)    # 0:DB오류 / 1:정상
            conn.commit()
            return cnt2
        else:       # 오류
            return 0