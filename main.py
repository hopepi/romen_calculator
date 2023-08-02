romen_sayilar = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  ##Hazır değişkenler
class romenclass:

    try:
        def hesaplayici(self, deger):
            int_cevirisi = 0  ##değişken burda

            for i in range(len(deger)):  ## örnek olarak MMMM verildiğinde değişkenin uzunluğu kadar dönecek yani 4
                if i > 0 and romen_sayilar[deger[i]] > romen_sayilar[deger[i - 1]]:
                    int_cevirisi += romen_sayilar[deger[i]] - 2 * romen_sayilar[deger[i - 1]]
                else:
                    int_cevirisi += romen_sayilar[deger[i]]
            return int_cevirisi
    except:
        print("Yanlış bir değer girdiniz lütfen tekrar deneyiniz")
        kullanicinin_deger = input()

kullanicinin_deger = input()

try:
    print(romenclass().hesaplayici(kullanicinin_deger))
except:
    print("Yanlış bir değer girdiniz lütfen tekrar deneyiniz")
    kullanicinin_deger = input()
    print(romenclass().hesaplayici(kullanicinin_deger))