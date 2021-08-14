# Olcek





"""



Ölçek Özellikleri
-----------------



Verileriniz farklı değerlere ve hatta farklı ölçüm birimlerine sahip olduğunda bunları karşılaştırmak zor olabilir.
----------------------------    -----------------------------------------------------------------------------------
Metre ile karşılaştırıldığında kilogram nedir? Ya da zamana göre yükseklik?
---------------------------------------------- ----------------------------


Bu sorunun cevabı ölçeklendirmedir. Verileri, karşılaştırması daha kolay yeni değerlere ölçekleyebiliriz.
----------------- ****************  --------------------------------------------------------------------


Aşağıdaki tabloda bakabilirsiniz, biz de kullanılan aynı veri kümesidir çoklu regresyon bölüm , ama bu kez
--------------------------------  -----------------------------------------------------------------------
hacimli sütun değerleri içeren litre yerine cm3 (1000 yerine 1.0).
------------------------------------------------------------------






Dosya yalnızca test amaçlıdır, buradan indirebilirsiniz: cars2.csv
------------------------------------------------------------------









Arac	        Model	         Hacim	        Agirlik        Karbon Emisyonu
---             -----            -----          -------        ---------------


Toyota	        Aygo	         1.0	         790	            991

Mitsubishi	    Space Star	     1.2	         1160	            95

Skoda	        Citigo	         1.0 	         929	            95

Fiat	        500	             0.9	         865	            90

Mini	        Cooper	         1.5	         1140	            105

VW	            Up!	             1.0	         929	            105

Skoda	        Fabia	         1.4	         1109	            90

Mercedes	    A-Class	         1.5	         1365	            92

Ford	        Fiesta	         1.5	         1112	            98

Audi	        A1	             1.6	         1150	            99

Hyundai	        I20	             1.1	         980	            99

Suzuki	        Swift	         1.3	         990	            101

Ford	        Fiesta	         1.0	         1112	            99

Honda	        Civic	         1.6	         1252	            94

Hundai	        I30	             1.6	         1326	            97

Opel	        Astra	         1.6	         1330	            97

BMW	            1	             1.6	         1365	            99

Mazda	        3	             2.2	         1280	            104

Skoda	        Rapid	         1.6	         1119	            104

Ford	        Focus	         2.0	         1328	            105

Ford	        Mondeo	         1.6	         1584	            94

Opel	        Insignia	     2.0	         1428	            99

Mercedes	    C-Class	         2.1	         1365	            99

Skoda	        Octavia	         1.6	         1415	            99

Volvo	        S60	             2.0	         1415	            99

Mercedes	    CLA	             1.5	         1465	            102

Audi	        A4	             2.0	         1490	            104

Audi	        A6	             2.0	         1725	            114

Volvo	        V70	             1.6	         1523	            109

BMW	            5	             2.0	         1705	            114

Mercedes	    E-Class	         2.1	         1605	            115

Volvo	        XC70	         2.0	         1746	            117

Ford	        B-Max	         1.6	         1235	            104

BMW	            2	             1.6	         1390	            108

Opel	        Zafira	         1.6	         1405	            109

Mercedes	    SLK	             2.5	         1395	            120










1.0 hacmini 790 ağırlığı ile karşılaştırmak zor olabilir, ancak her ikisini de karşılaştırılabilir değerlere
-------------------------------------------------------- --------------------------------------------------
ölçeklendirirsek, bir değerin diğerine kıyasla ne kadar olduğunu kolayca görebiliriz.
*************** --------------------------------------------------------------------

Verileri ölçeklendirmek için farklı yöntemler vardır, bu derste standardizasyon adı verilen bir yöntem kullanacağız.
----------------------------------------------------- ---------- ************** -----------------------------------

Standardizasyon yöntemi şu formülü kullanır:
*********************** -------------------





z = (x - u) / s




(z) Yeni değer nerede demektir (degiskenimiz), (x)  orijinal değer, (u)  ortalama ve  (s)  standart sapmadır.
************************************************************************************************************
Yani z degiskenimiz icerisine = (x yani orjinal deger (-) eksi ortalama (u)) (/) bolu standard sapma (s)
************************************************************************************************************



Ağırlık sütununu yukarıdaki veri kümesinden alırsanız , ilk değer 790'dır ve ölçeklenen değer şöyle olacaktır:
------------------------------------------------------  -----------------------------------------------------




(790 - 1292.23) / 238.74 = -2.1





Hacim sütununu yukarıdaki veri kümesinden alırsanız , ilk değer 1.0'dır ve ölçeklenen değer şöyle olacaktır:
----------------------------------------------------  ------------------------------------------------------




(1.0 - 1.61) / 0.38 = -1.59





Artık 790'ı 1.0 ile karşılaştırmak yerine -2.1 ile -1.59'u karşılaştırabilirsiniz.
*********************************************************************************





Bunu manuel olarak yapmanız gerekmez, Python sklearn modülünde, StandardScaler() veri kümelerini dönüştürmek için
------------------------------------  ************************  **************** --------------------------------
yöntemlerle bir Scaler nesnesi döndüren adlı bir yöntem bulunur .
--------------- ************** ---------------------------------




"""









# Ornek  Ağırlık ve Hacim sütunlarındaki tüm değerleri ölçeklendirin:





import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler




scale = StandardScaler()



df = pandas.read_csv("cars2.csv")



X = df[["Weight", "Volume"]]



scaledX = scale.fit_transform(X)



print(scaledX)









"""




Sonuç: İlk iki değerin -2.1 ve -1.59 olduğuna dikkat edin, bu bizim hesaplamalarımıza karşılık gelir:
       -----------------***-----****----------------------------------------------------------------






[[-2.10389253 -1.59336644]          -> Degerlerimiz Burada ilk satirda
 [-0.55407235 -1.07190106]
 [-1.52166278 -1.59336644]
 [-1.78973979 -1.85409913]
 [-0.63784641 -0.28970299]
 [-1.52166278 -1.59336644]
 [-0.76769621 -0.55043568]
 [ 0.3046118  -0.28970299]
 [-0.7551301  -0.28970299]
 [-0.59595938 -0.0289703 ]
 [-1.30803892 -1.33263375]
 [-1.26615189 -0.81116837]
 [-0.7551301  -1.59336644]
 [-0.16871166 -0.0289703 ]
 [ 0.14125238 -0.0289703 ]
 [ 0.15800719 -0.0289703 ]
 [ 0.3046118  -0.0289703 ]
 [-0.05142797  1.53542584]
 [-0.72580918 -0.0289703 ]
 [ 0.14962979  1.01396046]
 [ 1.2219378  -0.0289703 ]
 [ 0.5685001   1.01396046]
 [ 0.3046118   1.27469315]
 [ 0.51404696 -0.0289703 ]
 [ 0.51404696  1.01396046]
 [ 0.72348212 -0.28970299]
 [ 0.8281997   1.01396046]
 [ 1.81254495  1.01396046]
 [ 0.96642691 -0.0289703 ]
 [ 1.72877089  1.01396046]
 [ 1.30990057  1.27469315]
 [ 1.90050772  1.01396046]
 [-0.23991961 -0.0289703 ]
 [ 0.40932938 -0.0289703 ]
 [ 0.47215993 -0.0289703 ]
 [ 0.4302729   2.31762392]]




"""









# CO2 Degerlerini Tahmin Edin









"""



CO2 Değerlerini Tahmin Edin
---------------------------


Çoklu Regresyon bölümündeki görev, yalnızca ağırlığını ve hacmini bildiğiniz bir arabadan kaynaklanan 
-----------------------------------------------------------------------------------------------------
CO2 emisyonunu tahmin etmekti.
-----------------------------


Veri seti ölçeklendiğinde, değerleri tahmin ederken ölçeği kullanmanız gerekecektir:
-----------------------------------------------------------------------------------



"""






# Örnek 2300 kilogram ağırlığındaki 1,3 litrelik bir arabanın CO2 emisyonunu tahmin edin:







import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler



scale = StandardScaler()

df = pandas.read_csv("cars2.csv")


X = df[["Weight", "Volume"]]
y = df["CO2"]


scaledX = scale.fit_transform(X)


regr = linear_model.LinearRegression()
regr.fit(scaledX, y)


scaled = scale.transform([[2300, 1.3]])


predictedCO2 = regr.predict([scaled[0]])


print(predictedCO2)







# Sonuç: [107.2087328]