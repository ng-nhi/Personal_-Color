def tinhdthinhvuong(canh):
    dt = canh * canh
    return dt
def tinh_dien_tich_hinh_chu_nhat():
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    s = dai * rong
    print(f"➡ Diện tích hình chữ nhật là: {s:.2f}")

def tinh_dien_tich_hinh_tam_giac():
    day = float(input("Nhập độ dài đáy: "))
    cao = float(input("Nhập chiều cao: "))
    s = 0.5 * day * cao
    print(f"➡ Diện tích hình tam giác là: {s:.2f}")

def tinh_dien_tich_hinh_thang():
    day_lon = float(input("Nhập đáy lớn: "))
    day_nho = float(input("Nhập đáy nhỏ: "))
    cao = float(input("Nhập chiều cao: "))
    s = ((day_lon + day_nho) * cao) / 2
    print(f"➡ Diện tích hình thang là: {s:.2f}")
def tinh_dien_tich_hinh_tron():
    r = float(input("Nhập bán kính hình tròn: "))
    s = 3.14* r*r
    print(f"➡ Diện tích hình tròn là: {s:. 2f}")
choice = 0
while choice != 5:
    print('1. Tinh dien tinh hinh vuong')
    print('2. Tinh dien tinh hinh chu nhat')
    print('3. Tinh dien tinh hinh tron')
    print('4. Tinh dien tinh hinh tam giac')
    print('5. Thoat')
    choice = int(input('Nhap lua chon cua ban: '))
    if choice == 1:
        print('Moi ban nhap canh hinh vuong:')
        a = int(input())
        dt = tinhdthinhvuong(a)
        print('Dien tich hinh vuong = ', dt)
    elif choice == 2:
        print('Hinh chu nhat:')
    elif choice == 3:
        print('Hinh tron:')
    elif choice == 4:
        print('Hinh tam giac:')
    elif choice == 5:
        print('hinh thang:')
        break
    else:
        print(' chon so tu 1 den 5')