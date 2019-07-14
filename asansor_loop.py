kat=0
while(1):
	print("Şu an" ,kat ,". kattasınız.")
	istek=input("Aşağı mı ineceksiniz, yukarı mı çıkacaksınız A/Y:")
	if istek=='A' or istek=='a' :
		if kat==0 :
			print("Zemin kattasınız. Aşağı inemezsiniz.")
			continue
		else :
			istek2=int(input("Kaç kat aşağı ineceksiniz?"))
			if istek2>kat :
				print("Çok fazla aşağı indiniz. Zemin kattasınız.")
				kat=0
				continue
			elif istek2<kat :
				kat=kat-istek2
				print(istek2, "kat aşağı indiniz," ,kat ,". kattasınız.")
				continue
	elif istek=='Y' or istek=='y' :
		if kat==10 :
			print("En üst kattasınız. Yukarı çıkamazsınız.")
			continue
		else :
			istek2=int(input("Kaç kat yukarı çıkacaksınız?"))
			if istek2>10-kat :
				print("Çok fazla yukarı çıktınız. En üst kattasınız.")
				kat=10
				continue
			else :
				kat=kat+istek2
				print(istek2, "kat yukarı çıktınız," ,kat ,". kattasınız.")
				continue
	else :
		print("Sadece A ya da Y kullanınız.")
		continue

			
			
			
		
