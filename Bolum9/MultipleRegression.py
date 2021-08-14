# Coklu Regresyon




"""




Çoklu regresyon
---------------



Çoklu regresyon, lineer regresyon gibidir , ancak birden fazla bağımsız değere sahiptir, yani
---------------  ------------------------         ----------------------------

iki veya daha fazla değişkene dayalı bir değeri tahmin etmeye çalışıyoruz .
--- ---- ---- ----- --------- ------ --- ------- ----- ------ -----------




Aşağıdaki veri setine bir göz atın, arabalar hakkında bazı bilgiler içeriyor.
----------------------------------------------------------------------------





Arac	        Model	         Hacim	        Agirlik        Karbon Emisyonu
---             -----            -----          -------        ---------------


Toyota	        Aygo	         1000	         790	            991

Mitsubishi	    Space Star	     1200	         1160	            95

Skoda	        Citigo	         1000	         929	            95

Fiat	        500	             900	         865	            90

Mini	        Cooper	         1500	         1140	            105

VW	            Up!	             1000	         929	            105

Skoda	        Fabia	         1400	         1109	            90

Mercedes	    A-Class	         1500	         1365	            92

Ford	        Fiesta	         1500	         1112	            98

Audi	        A1	             1600	         1150	            99

Hyundai	        I20	             1100	         980	            99

Suzuki	        Swift	         1300	         990	            101

Ford	        Fiesta	         1000	         1112	            99

Honda	        Civic	         1600	         1252	            94

Hundai	        I30	             1600	         1326	            97

Opel	        Astra	         1600	         1330	            97

BMW	            1	             1600	         1365	            99

Mazda	        3	             2200	         1280	            104

Skoda	        Rapid	         1600	         1119	            104

Ford	        Focus	         2000	         1328	            105

Ford	        Mondeo	         1600	         1584	            94

Opel	        Insignia	     2000	         1428	            99

Mercedes	    C-Class	         2100	         1365	            99

Skoda	        Octavia	         1600	         1415	            99

Volvo	        S60	             2000	         1415	            99

Mercedes	    CLA	             1500	         1465	            102

Audi	        A4	             2000	         1490	            104

Audi	        A6	             2000	         1725	            114

Volvo	        V70	             1600	         1523	            109

BMW	            5	             2000	         1705	            114

Mercedes	    E-Class	         2100	         1605	            115

Volvo	        XC70	         2000	         1746	            117

Ford	        B-Max	         1600	         1235	            104

BMW	            2	             1600	         1390	            108

Opel	        Zafira	         1600	         1405	            109

Mercedes	    SLK	             2500	         1395	            120










Motorun boyutuna bağlı olarak bir arabanın CO2 emisyonunu tahmin edebiliriz, ancak çoklu regresyonla, tahmini
-----------------------------------------------------------------------------      -----------------  -------

daha doğru hale getirmek için arabanın ağırlığı gibi daha fazla değişken ekleyebiliriz.
----------------------------- --------------------------------------------------------






"""







# Peki Bunu Nasil Yapabiliriz ?








"""




Nasil Calisiyor bu sistem?
-------------------------




Python'da işi bizim için yapacak modüllerimiz var. Pandas modülünü içe aktararak başlayın.
-------------------------------------------------  *************** -----------------------



import pandas





Pandas Eğitimimizde Pandas modülü hakkında bilgi edinin.
---------------------------------------------------------

Pandas modülü, csv dosyalarını okumamıza ve bir DataFrame nesnesi döndürmemize izin verir.
-------------- --------------------------   ----------------------------------------------


Dosya yalnızca test amaçlıdır, buradan indirebilirsiniz: cars.csv
----------------------------   ------------------------- ********




df = pandas.read_csv("cars.csv") 





Ardından bağımsız değerlerin bir listesini yapın ve bu değişkeni (X) olarak çağırın
---------------------------------------------------------------------------

Bağımlı değerleri adı verilen bir (y) değişkene koyun .
---------------- ---------------- -- -----------------






X = df[['Weight', 'Volume']]
y = df['CO2']








İpucu: Bağımsız değerler listesini büyük harf X ile ve bağımlı değerler listesini küçük harf y ile adlandırmak yaygındır.
-------------------------------------------------------------------------------------------------------------------------





Sklearn modülünden bazı yöntemler kullanacağız, bu yüzden o modülü de içe aktarmamız gerekecek:
-----------------------------------------------------------------------------------------------






from sklearn import linear_model







Sklearn modülünden, LinearRegression() yöntemi doğrusal bir regresyon nesnesi oluşturmak için kullanacağız .
--------------------*************************************************-------------------------------------






Bu nesnenin, fit() bağımsız ve bağımlı değerleri parametre olarak alan ve regresyon nesnesini ilişkiyi tanımlayan 
------------ ***** ----------------------------------------------------------------------------------------------

verilerle dolduran bir yöntemi vardır :
-------------------------------------





regr = linear_model.LinearRegression()
regr.fit(X, y)







Artık bir otomobilin ağırlığına ve hacmine dayalı olarak CO2 değerlerini tahmin etmeye hazır bir regresyon nesnemiz var:
------------------------------------------------------------------------------------------------------------------------





# ağırlığı 2300 kg ve hacmi 1300 cm3 olan bir arabanın CO2 yani Karbon emisyonunu tahmin edin:

predictedCO2 = regr.predict([[2300, 1300]])



"""












# Ornek  Tüm örneği çalışırken görün:








# import pandas
# from sklearn import linear_model
#
#
#
#
#
#
#
#
# df = pandas.read_csv("cars.csv")
#
#
#
#
#
# X = df[['Weight', 'Volume']]
# y = df['CO2']
#
#
#
#
#
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
#
#
#
#
# # ağırlığı 2300 kg ve hacmi 1300 cm3 olan bir arabanın CO2 yani Karbon emisyonunu tahmin edin:
# predictedCO2 = regr.predict([[2300, 1300]])
#
#
#
#
#
# print(predictedCO2)






# Cikan Sonuç [107.2087328]





# 1,3 litrelik motora ve 2300 kg ağırlığa sahip bir otomobilin kat ettiği her kilometrede yaklaşık 107 gram CO2
# salacağını tahmin etmiştik.











"""






Katsayi
-------




Katsayı, bilinmeyen bir değişkenle olan ilişkiyi tanımlayan bir faktördür.
--------------------------------------------------------------------------

Örnek: x bir değişken ise, o zaman 2x, x'in iki katıdır. x bilinmeyen değişkendir ve 2 sayısı katsayıdır.
       ------------------------------------------------  -----------------------------------------------


Bu durumda, CO2'ye karşı ağırlığın ve CO2'ye karşı hacmin katsayı değerini isteyebiliriz. 
----------------------------------    --------------------------------------------------
Aldığımız cevap(lar), bağımsız değerlerden birini arttırırsak veya azaltırsak ne olacağını söyler.
-------------------------------------------------------------------------------------------------





"""









# Örnek Regresyon nesnesinin katsayı değerlerini yazdırın:








# import pandas
# from sklearn import linear_model
#
#
#
# df = pandas.read_csv("cars.csv")
#
#
#
#
# X = df[["Weight", "Volume"]]
# y = df["CO2"]
#
#
#
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
#
#
#
#
# print(regr.coef_)







# Sonuc [0.00755095 0.00780526] bu sekildedir








"""



Sonuç Açıklaması
----------------



Sonuç dizisi, ağırlık ve hacmin katsayı değerlerini temsil eder.
----------------------------------------------------------------


Ağırlık: 0.00755095
Hacim: 0.00780526


Bu değerler bize ağırlık 1 kg artarsa CO2 emisyonunun 0.00755095 gr arttığını söyler.
------------------------------------------------------------------------------------

Motor hacmi (Hacim) 1 cm3 artarsa CO2 emisyonu 0,00780526 gr artar.
--------------------------------------------------------------------

Bence bu adil bir tahmin, ama test edelim!
------------------------------------------

1300cm3 motorlu bir arabanın 2300 kg ağırlığında olması durumunda CO2 emisyonunun yaklaşık 107g olacağını zaten tahmin etmiştik.
---------------------------------------------------------------------------------------------------------------------





Ağırlığı 1000kg ile arttırırsak ne olur?
----------------------------------------




"""










# Örnegi  öncekinden kopyalayın, ancak ağırlığı 2300'den 3300'e değiştirin:








import pandas
from sklearn import linear_model




df = pandas.read_csv("cars.csv")





X = df[["Weight", "Volume"]]
y = df["CO2"]




regr = linear_model.LinearRegression()
regr.fit(X, y)




predictCO2 = regr.predict([[3300, 1300]])




print(predictCO2)









# Sonuç: [114.75968007] seklinde cikti








# Bilgi







"""


1,3 litrelik motora ve 3300 kg ağırlığa sahip bir otomobilin kat ettiği her kilometrede yaklaşık 
115 gram CO2 salacağını tahmin etmiştik.


Bu, 0.00755095 katsayısının doğru olduğunu gösterir:


107.2087328 + (1000 * 0.00755095) = 114.75968


"""



# Bu sekilde tahminlerimiz gerceklerle ortusmeye basladi :)







