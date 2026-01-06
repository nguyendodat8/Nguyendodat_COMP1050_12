students = []
n = int(input('Nhập số lượng sinh viên:'))
for i in range (n):
    print(f"\nNhập thông tin cho sinh viên {i+1}:")
    ma_SV = input()
    Ten_SV = input()
    Ngay_sinh = input()
    Noi_sinh = input()
    Diem_GPA = float(input())
    Diem_Ren_Luyen = int(input())
#Tạo dictionary cho sinh vien:
    student = {
        "MSV": ma_SV,
        "Ho ten": Ten_SV,
        "Ngay sinh": Ngay_sinh,
        "Noi sinh": Noi_sinh,
        "Diem_GPA": Diem_GPA,
        "Diem_ren_luyen": Diem_Ren_Luyen
    }
students.append(student)
#Tạo các tác vụ với danh sách sinh viên:
while True:
    print("Chào mừng bạn đến với hệ thống quản lý sinh viên")
    print('Nhập 1: Xem danh sách sinh viên.')
    print('Nhập 2: Thêm sinh viên.')
    print('Nhập 3: Tìm kiếm sinh viên.')
    print('Nhập 4: Xem xếp loại sinh viên')
    print('Nhập 5: Xem danh sách sinh viên nhận học bổng')
    print('Nhập 0: Kết thúc')
    tac_vu = int(input('Chọn 1 tác vụ:'))
    if tac_vu == 0:
        break
    if tac_vu == 1:
        print('DANH SÁCH SINH VIÊN')
        print('STT  MSV   Tên SV      Ngày sinh      Nơi sinh       Điểm GPA       Điểm rèn luyện')
        for i,student in enumerate(students):
            print(i,student["MSV"],student["Ho ten"],student["Ngay sinh"],student["Noi sinh"],student["Diem_GPA"],student["Diem_ren_luyen"],sep='\t\t')
    if tac_vu == 2:
        n = int(input('Nhập số lượng sinh viên cần thêm:'))
        for i in range(n):
            print(f"\nNhập thông tin cho sinh viên {i+1}:")
            ma_SV = input()
            Ten_SV = input()
            Ngay_sinh = input()
            Noi_sinh = input()
            Diem_GPA = float(input())
            Diem_Ren_Luyen = int(input())
    #Tạo dictionary cho sinh vien:
        student = {
            "MSV": ma_SV,
            "Ho ten": Ten_SV,
            "Ngay sinh": Ngay_sinh,
            "Noi sinh": Noi_sinh,
            "Diem_GPA": Diem_GPA,
            "Diem_ren_luyen": Diem_Ren_Luyen
        }
        students.append(student)
    #Tìm kiếm sinh viên:
    if tac_vu == 3:
        Ma_sinh_vien = input('Nhập mã sinh viên:')
        if student["MSV"] == Ma_sinh_vien :
            print("Tìm thấy:",student[Ten_SV])
        else:
            print("Không tìm thấy sinh viên")
        Ten = input('Nhập họ tên:')
        if student["Họ tên"] == Ten_SV :
            print("Tìm thấy:",student[Ten_SV])
        else:
            print("Không tìm thấy sinh viên")
    if tac_vu == 4:
        def xep_loai_sinh_vien(xep_loai):
            xep_loai = ""
            if 3.6<Diem_GPA<4.0:
                xep_loai = 'Xuất sắc'
            elif 3.2<Diem_GPA<=3.6:
                xep_loai = 'Giỏi'
            elif 2.8<Diem_GPA<=3.2:
                xep_loai = 'Khá'
            elif 2.5<Diem_GPA<=2.8:
                xep_loai = 'Trung bình khá'
            elif 2<Diem_GPA<=2.5:
                xep_loai = 'Trung bình'
            else:
                print('Yếu')
            return xep_loai
        def xep_loai_DRL(xl):
            xl = ""
            if 90<=Diem_Ren_Luyen<100:
                xl = 'Xuất săc'
            elif 80<=Diem_Ren_Luyen<90:
                x1 = 'Tốt'
            elif 65<=Diem_Ren_Luyen<80:
                xl = 'Khá'
            elif 50<=Diem_Ren_Luyen<65:
                xl = 'Trung bình'
            else:
                xl = 'Yếu'
            return xl
    print('KẾT QUẢ XẾP LOẠI SINH VIÊN')
    print('STT MSV Họ tên Ngày sinh Nơi sinh GPA Điểm rèn luyện Xếp loại học lực Xếp loại ĐRL')
    for i in enumerate(students):
        xeploai = xep_loai_sinh_vien(Diem_GPA)
        xl_ĐRL = xep_loai_DRL(Diem_Ren_Luyen)
        print(i+1,student["MSV"],student["Ho ten"],student["Ngay sinh"],student["Noi sinh"],student["Diem_GPA"],student["Diem_ren_luyen"],xeploai,xl_ĐRL,sep='\t\t')
    if tac_vu == 5:
        print('Danh sách sinh viên nhận học bổng')
        for student in students:
            if student[Diem_GPA] >= 3.2 and student[Diem_Ren_Luyen] >= 85:
                print('KẾT QUẢ XẾP LOẠI SINH VIÊN')
                print('MSV Họ tên Ngày sinh Nơi sinh GPA Điểm rèn luyện Xếp loại học lực Xếp loại ĐRL')
                print(student["MSV"],student["Ho ten"],student['Ngay sinh'],student['Noi sinh'],student['Diem_GPA'],student['Diem_ren_luyen'],sep='\t\t')