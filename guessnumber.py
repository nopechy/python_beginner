import random
print( " Programın tuttuğu sayıyı bilmeye hoşgeldiniz 0 ile 100 arasında bir sayı tuttum bilene kadar tahmin edeceksiniz, bildiğiniz takdirde yeni bir sayı tutacağım. Programı durdurmak için -1 giriniz " )
x=0
y=random.randrange(0,100,1)
while x==0:
	sayi=int(input("Bir sayı giriniz: "))
	if sayi==-1: break
	if sayi==y:
		print("Doğru bildiniz ")
		y=random.randrange(0,100,1)
		print("Yeni bir sayı tuttum")
	elif sayi>y : print("Yüksek bir sayı söylediniz, ")
	else : print ("Alçak bir sayı söylediniz, ")
	

