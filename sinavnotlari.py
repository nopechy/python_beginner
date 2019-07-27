x=0
y=0
a,b,c = input("Allen'ın sınav notları giriniz (3 Tane):").split()

int_a = int(a)
int_b = int(b)
int_c = int(c)

d,e,f = input("Bob'ın sınav notlarını giriniz (3 Tane):").split()

int_d = int(d)
int_e = int(e)
int_f = int(f)

if (int_a>int_d):
    x=x+1
elif (int_a<int_d):
    y=y+1
if (int_b>int_e):
    x=x+1
elif (int_b<int_e):
    y=y+1
if (int_c>int_f):
    x=x+1
elif(int_c<int_f):
    y=y+1
print("Allen'ın puanı:" ,x ,",Bob'ın puanı:" ,y)
if (x>y):
    print("Allen kazandı!")
elif(y>x):
    print("Bob kazandı!")
else:
    print("Berabere kaldılar!")
