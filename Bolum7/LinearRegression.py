# Regreson


"""

Regresyon
----------


Değişkenler arasındaki ilişkiyi bulmaya çalıştığınızda regresyon terimi kullanılır.
---------------------------------------                ----------------

Makine Öğreniminde ve istatistiksel modellemede bu ilişki gelecekteki olayların sonucunu tahmin etmek için kullanılır.
------------------    -------------------------                                          -------------


"""





# Dogrusal Regresyon




"""


Doğrusal Regresyon
-------------------

Doğrusal regresyon, veri noktaları arasındaki ilişkiyi, tüm bunların arasından düz bir çizgi çizmek için kullanır.
------------------  -------------- -------------------  ------------------------------------------------

Bu çizgi gelecekteki değerleri tahmin etmek için kullanılabilir.
---------------------------------------------------------------

****
# -->  Ornek resimde cizgiyi takip edebilirsiniz veriler arasindan geciyor "img_linear_regression.png" inceleyin <--
****


Makine Öğreniminde geleceği tahmin etmek çok önemlidir.



"""





# Simdi nasil calistigini anlayalim





"""


O nasıl çalışır?
-----------------


Python, veri noktaları arasında bir ilişki bulmak ve bir doğrusal regresyon çizgisi çizmek için yöntemlere sahiptir. 
------  -----------------------     ------------         --------------------------------------

Matematik formülü üzerinden gitmek yerine bu yöntemleri nasıl kullanacağınızı göstereceğiz.


"""




# Ornek  Bir dağılım grafiği çizerek başlayın:



# import numpy as np
# import matplotlib.pyplot as plt
#
#
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
#
# plt.scatter(x, y)
#
# plt.show()



# Burada programi calistirdigimizda diagram resmini aliyoruz kontrol edin  --> "img_matplotlib_scatter.png" <--






#------------------------------------------------------------------------------------------------------------#






# Ornek  scipy Lineer Regresyon çizgisini içe aktarın ve çizin:




# import matplotlib.pyplot as plt
# from scipy import stats
#
#
#
#
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
#
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
#
#
# def myfunc(x):
#     return slope * x + intercept
#
#
#
# mymodel = list(map(myfunc, x))
#
#
#
# plt.scatter(x, y)
#
# plt.plot(x, mymodel)
#
# plt.show()




# Burada  veri noktaları arasında bir ilişki bulmak ve bir doğrusal regresyon çizgisi çizmek için kullandik
# --> "img_linear_regression.png" <--  Diagrami buradan gorebilirsiniz







"""

Örnek Açıklama
--------------




----------------------------------------------------------------------------------------

İhtiyacınız olan modülleri içe aktarın.

Matplotlib modülü hakkında Matplotlib Tutorial'ımızda bilgi edinebilirsiniz .

SciPy modülü hakkında SciPy Eğitimimizde bilgi edinebilirsiniz .




import matplotlib.pyplot as plt
from scipy import stats

------------------------------------------------------------------------------------------


x ve y ekseninin değerlerini temsil eden dizileri oluşturun:



x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


------------------------------------------------------------------------------------------


Doğrusal Regresyonun bazı önemli anahtar değerlerini döndüren bir yöntem yürütün:




slope, intercept, r, p, std_err = stats.linregress(x, y)

-------------------------------------------------------------------------------------------


Yeni bir değer döndürmek için slopeve interceptdeğerlerini kullanan bir işlev oluşturun . 
Bu yeni değer, karşılık gelen x değerinin y ekseninde nereye yerleştirileceğini temsil eder:





def myfunc(x):
  return slope * x + intercept


---------------------------------------------------------------------------------------------


x dizisinin her değerini işlev aracılığıyla çalıştırın. 
Bu, y ekseni için yeni değerlere sahip yeni bir diziyle sonuçlanacaktır:




mymodel = list(map(myfunc, x))


----------------------------------------------------------------------------------------------


Orijinal dağılım grafiğini çizin:




plt.scatter(x, y)

----------------------------------------------------------------------------------------------



Doğrusal regresyon çizgisini çizin:





plt.plot(x, mymodel)


------------------------------------------------------------------------------------------------



Diyagramı görüntüleyin:




plt.show()


-------------------------------------------------------------------------------------------------



"""







# Devaminda ise bunlari detaylica aciklamaya devam ediyoruz... simdi yine ayni konudayiz derinlere gidelim detaylari konusalim







"""



İlişki için R
-------------


X ekseninin değerleri ile y ekseninin değerleri arasındaki ilişkinin nasıl olduğunu bilmek önemlidir, eğer ilişki yoksa doğrusal regresyon hiçbir şeyi tahmin etmek için kullanılamaz.


Bu ilişkiye - korelasyon katsayısı - denir (r).


r degeri = Korelasyon katsayısı, bağımsız değişkenler arasındaki ilişkinin yönü ve büyüklüğünü belirten katsayıdır. 
Bu katsayı, (-1) ile (+1) arasında bir değer alır. Pozitif değerler direkt yönlü doğrusal ilişkiyi; negatif değerler 
ise ters yönlü bir doğrusal ilişkiyi belirtir. Korelasyon katsayısı 0 ise söz konusu değişkenler arasında doğrusal 
bir ilişki yoktur.



Python ve Scipy modülü sizin için bu değeri hesaplayacaktır, tek yapmanız gereken onu x ve y değerleri ile beslemektir.



"""



# Ornek  Verilerim doğrusal bir regresyona ne kadar uyuyor?




# from scipy import stats
#
#
#
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
#
#
# print(r)




#  Not:!!!!  Burada cikan korelasyon degeri yani r degeri -0.7585915243761551 sonucu mükemmel olmayan bir ilişki olduğunu gösterir,
    # ancak gelecekteki tahminlerde doğrusal regresyon kullanabileceğimizi gösterir.





"""


Gelecekteki Değerleri Tahmin Edin
---------------------------------


Artık gelecekteki değerleri tahmin etmek için topladığımız bilgileri kullanabiliriz.
      --------------------- ----------------- -----------------------
      
Örnek: 10 yaşında bir arabanın hızını tahmin etmeye çalışalım.
--------------------------------------------------------------

Bunu yapmak için, myfunc()yukarıdaki örnekteki aynı fonksiyona ihtiyacımız var :




def myfunc(x):
  return slope * x + intercept


  
"""





# Ornek  10 yaşında bir arabanın hızını tahmin edin:




# from scipy import stats
# import matplotlib.pyplot as plt
#
#
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
#
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
#
#
#
#
# def myfunc(x):
#     return slope * x + intercept
#
#
#
# speed = myfunc(10)
#
#
#
# print(speed)





# Örnek, şemadan da okuyabileceğimiz 85.59308314937454'da bir hız öngördü:



# Burada resmi "img_linear_regression2.png" inceleyin ve sonucu gozlerinizle gorun :)







"""


Kötü Uyum?
----------


Doğrusal regresyonun gelecekteki değerleri tahmin etmek için en iyi yöntem olmayacağı bir örnek oluşturalım.


"""






# Örnek x ve y ekseni için bu değerler, doğrusal regresyon için çok kötü bir uyumla sonuçlanmalıdır:





# import matplotlib.pyplot as plt
# from scipy import stats
#
#
#
#
# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
#
#
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
#
#
#
#
# def myfunc(x):
#     return slope * x + intercept
#
#
#
#
# mymodel = list(map(myfunc, x))
#
#
# plt.scatter(x, y)
#
# plt.plot(x, mymodel)
#
# plt.show()






# Simdi Cikan Kotu sonucu su diagram "img_linear_regression_badfit" icerisinde kontrol edebilirsiniz. Dogrusal regresyon girdigimiz verilere gore cok kotu bir sonuc cikardi






# Ve r ilişki için?






# Ornek Çok düşük bir r değer almalısınız .






import numpy as np
from scipy import stats



x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]




slope, intercept, r, p, std_err = stats.linregress(x, y)



print(r)



# Sonuç: 0.013 çok kötü bir ilişkiyi gösterir ve bize bu veri setinin lineer regresyon için uygun olmadığını söyler.

