import time
from re import L
import random

class Pc_Lab():
    
    def __init__(self, ogrenci_sayisi=6, bilgisayar_sayisi=12, dolu_bilgisayar_sayisi=6, bos_bilgisayar_sayisi=6, Sinif_Ogretmeni=["Ahmet","Mehmet","Cemal"]):
        self.ogrenci_sayisi=ogrenci_sayisi
        self.bilgisayar_sayisi=bilgisayar_sayisi
        self.dolu_bilgisayar_sayisi=dolu_bilgisayar_sayisi
        self.bos_bilgisayar_sayisi=bos_bilgisayar_sayisi
        self.Sinif_Ogretmeni=Sinif_Ogretmeni

    def Ogrenci(self):
        
        print("Ogrenci sayisi: ", self.ogrenci_sayisi)

    def Ogrenci_degisimi(self):
        
        while True:

            cevap=input("Ogrenci_geldi :+\nOgrenci_gitti: -\nÇıkış: q")

            if (cevap=='+'):
                self.ogrenci_sayisi+=1
                print("Ogrenci sayisi",format(self.ogrenci_sayisi))
            
            elif (cevap=="-"):
                if (self.ogrenci_sayisi<=0):
                    print("Daha öğrenci kalmadı")
                else:
                    self.ogrenci_sayisi-=1
                print("Ogrenci sayisi: ",format(self.ogrenci_sayisi))
            elif (cevap=="q"):
                break
            else:
                print("hatalı tuşlama")

    def bilgisayar_ogrenme(self):
        if (self.ogrenci_sayisi==6):
            print("İşler yolunda\n")
        else:
            self.dolu_bilgisayar_sayisi=self.ogrenci_sayisi
            print("Dolu olan bilgisayar sayisi: ",self.dolu_bilgisayar_sayisi,"\n")
        self.bos_bilgisayar_sayisi=(self.bilgisayar_sayisi)-(self.dolu_bilgisayar_sayisi)
        print("Boş bilgisayar sayisi: ",self.bos_bilgisayar_sayisi)
    
    def Ogretmen(self):
        Ahmet_sina=random.randint(0,3)
        print("Sınıf öğretmeninin ismi: ", self.Sinif_Ogretmeni[Ahmet_sina])



pc_lab = Pc_Lab()

while True:


        print("""
            1.Ogrenci bilgileri
            2.Öğrenci değişimi
            3.Bilgisayara yerleştirme
            4.Ogretmen Bilgileri
            5.Çıkış
            """)

        islem1 = input("Hoşgeldiniz lütfen bir seçim yapınız: ")

        if islem1 == "1":
            pc_lab.Ogrenci()
        elif islem1 == "2":
            pc_lab.Ogrenci_degisimi()
        elif islem1 == "3":
            pc_lab.bilgisayar_ogrenme()
        elif islem1== "4":
            pc_lab.Ogretmen()
        elif islem1 == "5":
            break
        else:
            print("Geçersiz işlem")