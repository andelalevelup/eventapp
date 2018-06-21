import pymysql
conn = pymysql.connect(host='andelalevelup.mysql.pythonanywhere-services.com', user='andelalevelup', passwd='password12', db='mydb')
cur = conn.cursor()
cur.execute("SELECT Host, User FROM user")
for r in cur:
    print(r)
cur.close()
conn.close()