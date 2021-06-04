

class Calisan:
    print("Bu Çalışan sınıfıdır")

    def Maas(self):
        mas_sat=int(input("Saatlik maaş : "))
        n=int(input("Çalışan Sayısını Girin : "))
        cal_list=[]
        giris_zamani=[]
        cikis_zamani=[]

        for i in range(0,n):
            cal_list.append(input("Çalışan Adını Girin : "))
            giris_zamani.append(int(input("Giriş saatini 24 saat formatında girin : ")))
            cikis_zamani.append(int(input("Çıkış saatini 24 saat formatında girin : ")))
            cal_sat=int(cikis_zamani[i] - giris_zamani[i])
            top_mas=cal_sat*mas_sat
            print("Çalışma saatleri :",cal_sat)
            print(cal_list[i],"Toplam maaş",top_mas,"TL")

Cal=Calisan()
Cal.Maas()
