from re import L
import time
import random



class Kumanda():

    def __init__(self, tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT",Hoperlor="R",renk_ayari=70,altyazi=["EN:1","TR:2","DE:3","RUS:4","FR:5"]):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal= kanal
        self.Hoperlor=Hoperlor
        self.renk_ayari=renk_ayari
        self.altyazi=altyazi


    def tv_ac(self):

        if (self.tv_durum  == "Kapalı"):
            print("Tv açılıyor")
            self.tv_durum="Açık"
        else:
            print("Tv zaten acik")

    def tv_kapat(self):
        
        if (self.tv_durum  == "Kapalı"):
            print("Tv zaten kapalı")
        
        else:
            print("Tv zaten kapaniyor")
            self.tv_durum="Kapalı"
    

    def ses_ayari(self):

        while True:

            cevap=input("Sesi artır :>\nSesi azalt: <\nÇıkış: q")

            if (cevap=='>'):
                if self.tv_ses>=100:
                    print("Max Ses")
                else:
                    self.tv_ses+=1
                print("Tv Sesi: {}".format(self.tv_ses))
            
            elif (cevap=="<"):
                if (self.tv_ses<=0):
                    print("Min ses")
                else:
                    self.tv_ses-=1
                print("tv_ses: {}",format(self.tv_ses))
            elif (cevap=="q"):
                break
            else:
                print("hatalı tuşlama")

    def kanal_ekle(self,kanal):
        if kanal in self.kanal_listesi:
            print("Kanal zaten var")
        else:
            
            print("Kanal ekleniyor...")
            time.sleep(1)
            

            self.kanal_listesi.append(kanal)

            print("Kanal listesi: {}".format(self.kanal_listesi))

    def kanal_sec(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]
        print(self.kanal)

    def Hoparlor(self):

        while True:

            cevap2=input("hoparlor :R veya L veya RL\nÇıkış: q")

            if (cevap2=='R'):
                print("Sağ hoparlor çalışıyor")
            elif (cevap2=="L"):
                self.Hoperlor="L"
                print("Sol hoparlor çalışıyor")
            elif (cevap2=="RL"):
                self.Hoperlor="RL"
                print("Sağ ve Sol hoparlor çalışıyor")
            elif (cevap2=="q"):
                break
            else:
                print("hatalı tuşlama")

    def renk(self):

        while True:

            cevap3=input("Renk artır :>\nRenk azalt: <\nÇıkış: q")

            if (cevap3=='>'):
                if self.renk_ayari>=100:
                    print("Max Renk")
                else:
                    self.renk_ayari+=1
                print("Renk:",format(self.renk_ayari)," \n")
            
            elif (cevap3=="<"):
                if (self.renk_ayari<=0):
                    print("Min ses")
                else:
                    self.renk_ayari-=1
                print("Renk:",format(self.renk_ayari)," \n")
            elif (cevap3=="q\n"):
                break
            else:
                print("hatalı tuşlama")

    def alyazi(self):

        print(self.altyazi,"\n Seçmek istediğiniz altyazini nümerik olarak numarasını giriniz.")
        
        while True:
            cevap4=input()
            alttyazi=0
            if (cevap4=="1"):
                alttyazi=self.altyazi[0]
            elif(cevap4=="2"):
                alttyazi=self.altyazi[1]
            elif (cevap4=="3"):
                alttyazi=self.altyazi[2]
            elif(cevap4=="4"):
                alttyazi=self.altyazi[3]
            elif (cevap4=="q\n"):
                break
            else:
                print("yanlış tuşlama")
            print("Altyazi durumu şu an: ",alttyazi)

    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv_durum: {}\ntv_ses: {}\nkanal listesi: {}\nkanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

print("""

        1. TV aç
        2. TV kapat
        3. Ses Ayarları
        4. Kanal Ekle
        5. Açık Kanalı Öğren
        6. Kanal Sayısı
        7. TV Bilgileri
        8. Hoparlor Bilgileri
        9. Renk Ayari
        10. Altyazi Bilgileri

Çıkmak için q'ya bas.

""")
kumanda=Kumanda()

while True:

    islem= input("İslem seçiniz")

    if islem =="q":
        print("Sonlandırılıyor")
     
    elif islem =="1":
        kumanda.tv_ac()
    
    elif islem=="2":
        kumanda.tv_kapat()

    elif islem=="3":
        kumanda.ses_ayari()
    
    elif islem=="4":

        kanal_isimleri=input("Kanal isimlerini lütfen , ile ayırarak giriniz.")

        x=kanal_isimleri.split(",")

        for i in x:
            kumanda.kanal_ekle(i)
    
    elif islem=="5":
        kumanda.kanal_sec()

    elif islem=="6":
        print("Kanal sayısı: ",len(kumanda))
    
    elif islem=="7":
        print(kumanda)
    
    elif islem=="8":
        kumanda.Hoparlor()

    elif islem=="9":
        kumanda.renk()
    
    elif islem=="10":
        kumanda.alyazi()

    else:
        print("hatalı Tuşlama")



    
