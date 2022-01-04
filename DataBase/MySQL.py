import mysql.connector
import PySimpleGUI as sg

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "thien123",
    database = "hocsinh"
)
mycursor = mydb.cursor()

# sql_str = "CREATE TABLE login (username VARCHAR(30), password VARCHAR(30))"
# sql_str = "INSERT INTO login(username, password) VALUES (%s,%s)"
# values = ('admin','123')

sql_str = "CREATE TABLE thongtin (ten VARCHAR(10), lop VARCHAR(30), diachi VARCHAR(100), diemtoan VARCHAR(2), diemly VARCHAR(2), diemhoa VARCHAR(2))"
sql_str = 'INSERT INTO thongtin(ten, lop, diachi, diemtoan, diemly, diemhoa) VALUES (%s, %s, %s, %s, %s, %s)'
values =('Thiện', '12H', 'Hải Dương', '8', '8', '8')
sql_str = "SELECT * FROM thongtin"
mycursor.execute(sql_str, values)
mydb.commit()

# sql_str = "DROP TABLE thongtin"
# sql_str = "CREATE TABLE thongtin (masv VARCHAR(10), ten VARCHAR(30), lop VARCHAR(20), diachi VARCHAR(100))"
# sql_str = "INSERT INTO thongtin(masv,ten,lop,diachi) VALUES (%s,%s,%s,%s)"
# values = ('5','Dương Văn Duy','d13cnpm7','Hà Nội')
# values = ("Đức","Ba Đình")
# sql_str = "SELECT * FROM thongtin"
# mycursor.execute(sql_str)
# mycursor.execute(sql_str, values)
# mydb.commit()

# sql_str = "INSERT INTO user(taikhoan, matkhat) VALUES (%s, %s)"
# values = ("admin", "123")
# mycursor.execute(sql_str, values)
# mydb.commit()

# myresult = mycursor.fetchall()
# dulieu = []
# for ten, diachi in myresult:
#     dulieu.append([ten, diachi])
# print(dulieu)

# headings = ['Tên', 'Địa Chỉ']
# layout = [[sg.Table(dulieu, headings=headings, justification = 'left', key = 'TABLE')]]
# Window = sg.Window("Bảng địa chỉ sinh viên",layout)
# while True:
#     event, values = Window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     print(event,values)
# Window.close()