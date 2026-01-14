import numpy as np
a= np.array([[12,3,4,10],[21,45,14,20],[26,19,2,9]])
print (a)
print (" phan tu o dong 2 va cot 3",a[1,2])
print (" phan tu nho nhat", a.min())
print (" phan tu lon nhat",a.max())
print (" tong cac phan tu",a.sum(axis=0))
print ("tong cac phan tu",a.sum(axis=1))
print (" so chieu cua mang la",a.size)
print ("hinh dang mang",a.shape)
print (" so chieu cua mang",a.ndim)
arr=a.reshape(4,3)
print("mang sau khi reshape: ")
print (arr)
with open("data.txt","w") as f:
    f.write(format(a))
    f.write(format(a[1,2]))
    f.write(format(a.min()))
    f.write(format(a.max()))
    f.write(format(a.sum(axis=0)))
    f.write(format(a.sum(axis=1)))
    f.write(format(a.size))
    f.write(format(a.shape))
    f.write(format(a.ndim))
print("data.txt")





