import mysql.connector 
import PySimpleGUI as psg

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='thien123',
  database='SinhVien'
)
mycursor=mydb.cursor()

def ShowInfo(thongtin):
  headings=['Mã', 'Tên', 'Lớp', 'Địa Chỉ']
  layout = [[psg.Table(thongtin, headings=headings,justification='left')]]
  window=psg.Window('Thông tin sinh viên', layout, margins=(50, 50))

  event, values = window.read()
  if event == psg.WIN_CLOSED:
    window.close()

def Insert(masv, ten, lop, diachi):
  query = 'INSERT INTO thongtin(masv, ten, lop, diachi) VALUES (%s, %s, %s, %s)'
  fields = (masv, ten, lop, diachi)
  mycursor.execute(query, fields)
  mydb.commit()

def CreateTable():
  sql_str = 'CREATE TABLE thongtin (masv VARCHAR(10), ten VARCHAR(30), lop VARCHAR(20), diachi VARCHAR(100))'
  mycursor.execute(sql_str)
  mydb.commit()

def login():
  try:
    left = [[psg.Button('Đăng Nhập')]]
    right = [[psg.Text(' ' * 65),psg.Button('Thoát')]]
    layout = [[psg.Text('Tài khoản : '), psg.InputText(key='username'),],
              [psg.Text('Mật khẩu : '), psg.InputText(key='password', password_char='*')],
              [psg.Text('_' * 60)],
              [psg.Column(left), psg.Column(right)]]

    window = psg.Window('Đăng nhập', layout, margins=(50, 50))
    event, values = window.Read()
    
    if (event == 'Đăng Nhập'):
      username = str(values['username'])
      password = str(values['password'])

      sql_str = "Select * from login WHERE username = '" +username+ "' and password = '"+password+"'"
      mycursor.execute(sql_str)
      myresult = mycursor.fetchall()
      
      if username=='' or password =='':
        psg.Popup('Thiếu thông tin')
        window.close()
        login()
      elif len(myresult) > 0:
        sql_str = 'SELECT * FROM thongtin'
        mycursor.execute(sql_str)
        result=mycursor.fetchall()
        thongtin=[]
        if result:
          for masv, ten, lop, diachi in result:
            thongtin.append([masv, ten, lop, diachi])
          ShowInfo(thongtin)
        else:
          psg.Popup('Không có thông tin !!!')
          window.close()
      else:
        psg.Popup('Tài khoản hoặc mật khẩu không đúng !!!')
        window.close()
        login()
    if event == psg.WIN_CLOSED or event == 'Thoát':
      window.close()
  except Exception:
    psg.Popup('Đã xảy có lỗi xảy ra !!!')
    window.close()
    login()

login()