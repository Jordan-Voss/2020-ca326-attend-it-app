import mysql.connector
def add_mod_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Attendit",
    database="attendit"
    )
    mycursor = mydb.cursor(buffered=True)
    c = mycursor.excecute("SELECT * FROM student")
    for r in c:
        print(c[r])
    query = "SELECT * FROM student"
    quer = "UPDATE student SET day = replace(day, 'NULL', 'Tuesday')"
    #val = (0,mod_name,'Tuesday',hours)
    #que="SELECT day, time FROM student WHERE day IS NOT NULL"
    #mycursor.execute(que)
    #row_count = 'error'
    #print ("number of affected rows: {}".format(row_count))
    #if row_count == 'error':
    try:
        mycursor.execute("UPDATE student SET day = IF (day IS NULL,'tuesday', day)")
        mydb.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    #else:
    #    print(row_count)

mod =['a','b','c','d']
ranking = {'a':4,'b':3,'c':2,'d':1}
avail_hours = 10
m = 0
for item in ranking:
    m= m + ranking[item]

mod_hours = {}
rnk = 4
print(rnk/avail_hours)
for r in mod:
    if ranking[r] == rnk:
        mod_hours[r] = (rnk/avail_hours * 10)
        rnk = rnk - 1
print(mod_hours)
am = []
for i in mod_hours:
    am.append(float(mod_hours[i]))
print(am)
add_mod_db()
