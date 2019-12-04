print("Merhaba! Size 2 tane kanguru verildi. Bu 2 kangurunun başlangıç noktalarını ve hızlarını yazıcaksınız.")
print("Ben de bu 2 kangurunun aynı noktaya gelip gelmeme şansını hesaplayacağım.")
x1,v1,x2,v2=input("Önce 1., sonra 2. kangurunun başlangıç noktasını ve hızını giriniz. (Örnek: 0 3 2 2):").split()
a=1
int_x1=int(x1)
int_x2=int(x2)
int_v1=int(v1)
int_v2=int(v2)
while a==1:
    int_x1=int_x1+int_v1
    int_x2=int_x2+int_v2
    if int_x1==int_x2:
        print("Aynı noktaya geldiler.")
        break
    elif int_x2==int_x2:
        print("Aynı noktaya geldiler.")
        break
    elif int_x1>=(500) or int_x2>=(500):
        print("Gelmediler.")
        break
-------------------------------------------------
if int_x1 != int_x2 and v1 == v2:
    print("Gelmezler")
else:
    print("Geldi")
