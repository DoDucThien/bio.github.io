import mysql.connector as sql
import PySimpleGUI as psg

mydb = sql.connect(
    host='localhost',
    user='root',
    password='thien123',
    database='sinhvien'
)
mycursor = mydb.cursor()


def Insert(masv, ten, lop, diachi):
    query = 'INSERT INTO thongtin(masv, ten, lop, diachi) VALUES (%s, %s, %s, %s)'
    fields = (masv, ten, lop, diachi)
    mycursor.execute(query, fields)
    mydb.commit()


def InsertGUI():
    layout = [[psg.Text('Mã sinh viên : '), psg.InputText(key='masv')],
              [psg.Text('Tên sinh viên : '), psg.InputText(key='name')],
              [psg.Text('Lớp : '), psg.Text(' ' * 6),
               psg.InputText(key='class')],
              [psg.Text('Địa chỉ: '), psg.Text(' ' * 6),
               psg.InputText(key='address')],
              [psg.Text('_' * 60)],
              [psg.Button('Cập nhật')],
              [psg.Button('Hủy')]]

    window = psg.Window('Thêm thông tin sinh viên', layout, margins=(50, 50))
    event, values = window.Read()
    if event == 'Cập nhật':
        masv = str(values['masv'])
        ten = str(values['name'])
        lop = str(values['class'])
        diachi = str(values['address'])
        if ten == '' or lop == '' or diachi == '':
            psg.Popup('Vui lòng nhập đầy đủ thông tin !!!')
            InsertGUI()
        else:
            query = 'INSERT INTO thongtin(masv, ten, lop, diachi) VALUES (%s, %s, %s, %s)'
            fields = (masv, ten, lop, diachi)
            mycursor.execute(query, fields)
            mydb.commit()
            main()
    if event == psg.WINDOW_CLOSED or event == 'Hủy':
        main()


def DropTable():
    sql_str = 'DROP TABLE thongtin'
    mycursor.execute(sql_str)
    mydb.commit()


def CreateTable():
    sql_str = 'CREATE TABLE thongtin (masv VARCHAR(10), ten VARCHAR(30), lop VARCHAR(20), diachi VARCHAR(100))'
    mycursor.execute(sql_str)
    mydb.commit()

    Insert('1', 'Đỗ Đức Thiện', 'd13cnpm7', 'Hải Dương')
    Insert('2', 'Nguyễn Duy Quang', 'd13cnpm7', 'Hà Nội')
    Insert('3', 'Nguyễn Quang Nguyên', 'd13cnpm7', 'Hà Nội')
    Insert('4', 'Hoàng Anh Vũ', 'd13cnpm7', 'Hà Nội')
    Insert('5', 'Dương Văn Duy', 'd13cnpm7', 'Hà Nội')


def main():
    try:
        sql_str = 'SELECT * FROM thongtin'
        mycursor.execute(sql_str)
        result = mycursor.fetchall()
        if result:
            thongtin = []
            for masv, ten, lop, diachi in result:
                thongtin.append([masv, ten, lop, diachi])

        headings = ['Mã', 'Tên', 'Lớp', 'Địa Chỉ']
        left = [[psg.Button('Thêm thông tin')], [psg.Button('Xóa bảng')]]
        right = [[psg.Text(' ' * 60), psg.Button('Thoát')]]
        layout = [[psg.Table(thongtin, headings=headings, justification='left')],
                  [psg.Text('_' * 60)],
                  [psg.Column(left), psg.Column(right)]]

        window = psg.Window('Đăng nhập hệ thống', layout, margins=(50, 50))
        event, values = window.Read()

        if event == 'Thêm thông tin':
            InsertGUI()
        if event == 'Xóa bảng':
            psg.Popup('Xóa bảng thành công !!!')
            window.close()
            DropTable()
            View()
        if event == psg.WIN_CLOSED or event == 'Thoát':
            window.close()
    except Exception:
        psg.Popup('Bảng thông tin đã tự động được tạo !!!')
        CreateTable()
        main()


def View():
    left = [[psg.Button('Thêm bảng')]]
    right = [[psg.Text(' ' * 60), psg.Button('Thoát')]]
    layout = [[psg.Column(left), psg.Column(right)]]

    window = psg.Window('Đăng nhập hệ thống', layout, margins=(50, 50))
    event, values = window.Read()

    if event == 'Thêm bảng':
        CreateTable()
        main()
    if event == psg.WIN_CLOSED or event == 'Thoát':
        window.close()


def login():
    try:
        left = [[psg.Button('Đăng Nhập')]]
        right = [[psg.Text(' ' * 65), psg.Button('Thoát')]]
        layout = [[psg.Text('Tài khoản : '), psg.InputText(key='username'), ],
                  [psg.Text('Mật khẩu : '), psg.InputText(
                      key='password', password_char='*')],
                  [psg.Text('_' * 60)],
                  [psg.Column(left), psg.Column(right)]]

        window = psg.Window('Đăng nhập hệ thống', layout, margins=(50, 50))
        event, values = window.Read()

        if (event == 'Đăng Nhập'):
            username = str(values['username'])
            password = str(values['password'])

            sql_str = "Select * from login WHERE username = '" + \
                username + "' and password = '"+password+"'"
            mycursor.execute(sql_str)
            myresult = mycursor.fetchall()

            if username == '' or password == '':
                psg.Popup('Vui lòng nhập đầy đủ thông tin !!!')
                window.close()
                login()
            elif len(myresult) > 0:
                main()
            else:
                psg.Popup('Tài khoản hoặc mật khẩu không đúng !!!')
                window.close()
                login()
        if event == psg.WIN_CLOSED or event == 'Thoát':
            window.close()
    except Exception:
        psg.Popup('Đã có lỗi xảy ra !!!')
        window.close()
        login()


login()
