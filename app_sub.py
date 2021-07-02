# DBから通知を表示してみよう
@app.route("/notice/tasklist")
def notice_tasklist():
    today = dt.date.today()
    today = today.strftime('%Y/%m/%d')
    print(today)
    conn = sqlite3.connect("maintenance.db")
    c = conn.cursor()
    c.execute("select table_name from item")
    print(table_name)
    table_name = []
    for row in c.fetchall():
        print(row[0])
        c.execute("select notice from " + row[0] + "")
        notice = c.fetchone()
        notice2 = []
        if notice is None:
            print("--------???------------")
            return "通知が設定されていないタスクがあります"
        else:
            notice2.append({"notice":notice})
            print("----------------------")
            c.execute("select notice from " + row[0] + "")
            print(notice)
            return redirect("/index")
    #     table_name.append({"table_name":row[0]})
    # # print(table_name)
    
    # print(table_name[0])
    # c.execute("select date, task from mado")
    # c.execute("select date from {}" .format(row[0]))
    # for row in table_name():
    #     print(row[0])
    
    # task_list =  []
    # # print(task)
    # # print("--------")
    # for row in c.fetchall():
    #     task_list.append({"date":row[0],"task":row[1]})
    # c.close()
    
    # return render_template("notice_list.html",task_list = task_list, today = today)
        