x, y, z=input("Bir zaman giriniz (Örnek: 05:32:15 PM):").split(':')
int_x=int(x)
int_y=int(y)


if z[3]=='A' or z[3]=='a':
    z=list(z)
    z="".join(z[0:2])
    if int_x==12:
        int_x='00'
        seq=[str(int_x),y,z]
        print("Saat:" ,":".join(seq))
    elif int_x>12:
        print("Bozuk girdiniz.")
    elif int_y>60:
        print("Bozuk girdiniz.")
    elif int(z)>60:
        print("Bozuk girdiniz.")
    else:
        seq=[str(int_x),y,z]
        print("Saat:" ,":".join(seq))
elif z[3]=='P' or z[3]=='p':
    z=list(z)
    z="".join(z[0:2])
    int_x=(int_x+12)
    if int_x>24:
        print("Bozuk girdiniz.")
    elif int_y>60:
        print("Bozuk girdiniz.")
    elif int(z)>60:
        print("Bozuk girdiniz.")
    else:
        seq=[str(int_x),y,z]
        print("Saat:" ,":".join(seq))
        
else : print("Yanlış formatta girdiniz")
