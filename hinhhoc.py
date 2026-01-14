import math

def dthinhchunhat (dai,rong):
    return dai*rong
def dthinhtron(r):
    return r*r
def dthinhthang(a,b,h):
    return (a+b)*h/2
def dttamgiacvuong(a,b):
    return (a*b)/2
def dthinhthoi(d1,d2):
    return (d1*d2)/2
def dttamgiaccan(day,chieucao):
    return (day*chieucao)/2
def dthbh(day,chieucao):
    return day*chieucao
from hinhhoc import*
print("dien tich hinh chu nhat" ,dthinhchunhat(5,6))
print(" dien tich hinh tron ", dthinhtron(8))
print(" dien tich hinh thang",dthinhthang(3,7,4))
print("dien tich tam giac vuong" , dttamgiacvuong(10,34))
print(" dien tich hinh thoi" , dthinhthoi(6,8))
print(" dien tich tam giac can" , dttamgiaccan(7,9))
print(" dien tich hinh binh hanh", dthbh(12,13))
