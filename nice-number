v=0
x,y,z= input("Sayı aralığı ve bölen sayıyı aralarında bir boşluk bırakarak giriniz:").split()
x=int(x)
y=int(y)
z=int(z)

for a in range(x,y+1,1):
    a_temp=list(str(a))
    temp=a_temp[0]
    a_temp[0]=a_temp[1]
    a_temp[1]=temp
    a_temp="".join(a_temp)
    a_temp=int(a_temp)
    if (a-a_temp)%z==0:
        v=v+1
print(v, "tane güzel sayı var bu aralıkta.")
