"""Fonksiyonları Tek Tek Belirtiyoruz"""

def toplamacift(ranget1,ranget2):
    i=0
    for x in range(ranget1,ranget2+1):
        if x % 2 == 0:
            i += x
            continue
    print(i)

def toplamatek(rangec1,rangec2):
    i=0
    for x in range(rangec1,rangec2+1):
        if x % 2 != 0:
            i += x
            continue
    print(i)


def toplama(range1,range2):
    i=0
    for x in range(range1,range2+1):
        i += x
    print(i)
    
"""Aldığımız Sayıları Fonksiyolarda Belirttiğimiz Range Değerleri Yerine Yazıyoruz """

sayi1 = int(input("Belirleyeceğiniz Aralığın Alt Sınırını Giriniz :"))
sayi2 = int(input("Belirleyeceğiniz Aralığın Üst Sınızırını Giriniz :"))
soru = input("Hangi Türde Bir Toplama İstediğinizi Yazınız.Eğer ardışık yoplamak istoyrsanız -a-,çiftleri toplamak isityorsanız -ç- \ntek satıları toplamak istiyorsanız -t- yazınız :" )

""" Yapılan Seçime Göre Belirlediğimiz Fonksiyonu Çağırıyoruz"""

if soru == "t":
    toplamatek(sayi1,sayi2)
elif soru == "a":
    toplama(sayi1,sayi2)
elif soru == "ç" :
    toplamacift(sayi1,sayi2)


