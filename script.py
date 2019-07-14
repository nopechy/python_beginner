istek=int(input("Asansör sıfırıncı katta. Kaçıncı kata çıkmak istersiniz?:"))
if istek>5 : 
	print("Bu apartman beş katlı. Lütfen 5 veya altındaki bir sayı giriniz")
	istek=int(input("Asansör sıfırıncı katta. Kaçıncı kata çıkmak istersiniz?:"))

elif istek<5 :
	print("Şu an" ,istek,". katındasınız.")

istek2=input("Yukarı mı yoksa aşağı mı ineceksiniz? A/Y:")
if istek2=='A' or 'a' :
	istek3=int(input("Kaç kat aşağı ineceksiniz?"))
	if istek3>istek :
		print("Çok fazla aşağı indiniz. Sıfırıncı kattasınız.")
	else :
		print(istek3, "kat aşağı indiniz." ,istek-istek3, ". kattasınız.")

elif istek2=='Y' or 'y' :
	istek3=int(input("Kaç kat yukarı çıkacaksınız?"))
	if istek3>5-istek :
		print("Çok fazla yukarı çıktınız. Beşinci kattasınız.")
	else :
		print(istek3, "kat yukarı çıktınız." ,istek+istek3, ". kattasınız.")

else :
	print("Kodumun malı git merdiveni kullan.")


