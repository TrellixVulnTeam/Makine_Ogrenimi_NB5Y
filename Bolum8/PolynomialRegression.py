# Polinom Regresyon


"""

Polinom Regresyon
-----------------


Veri noktalarınız açıkça doğrusal bir regresyona uymuyorsa (tüm veri noktalarından geçen düz bir çizgi),
-----------------        ---------------------------------  ------------------------------------------
polinom regresyon için ideal olabilir.
----------------------


Polinom regresyon, Dogrusal regresyon gibi, veri noktalarından bir çizgi çizmenin en iyi yolunu bulmak için
-----------------  ---------------------    ---------------------------------------------------------------
x ve y değişkenleri arasındaki ilişkiyi kullanır.
---------------------------------------


"""





# Ornek diagrama buradan "img_polynomial_regression.png" goz atabilirsiniz.





"""



O nasıl çalışır?
----------------


Python, veri noktaları arasında bir ilişki bulmak ve bir polinom regresyon çizgisi çizmek için yöntemlere sahiptir. 
        ----------------------  -----------------    -----------------------------------------                              
Matematik formülü üzerinden gitmek yerine bu yöntemleri nasıl kullanacağınızı göstereceğiz.
-------!!!-------------------------------    --------------------------------




Aşağıdaki örnekte, belirli bir gişeden geçerken 18 araba kaydettik.
----------------------------------------------- -- ---------------
Aracın hızını ve geçişin gerçekleştiği günün saatini (saati) kaydettik.
-------------    ----------------------------------- ------- ---------

X ekseni günün saatlerini ve y ekseni hızı temsil eder:
-------------------------    --------------------



"""





# Örnek  Bir dağılım grafiği çizerek başlayın:






# import matplotlib.pyplot as plt
#
#
#
#
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#
#
#
# plt.scatter(x, y)
#
#
# plt.show()






# Cikan sonucu "img_polynomial_scatter.png" adli diagram uzerinden inceleyebilirsiniz










# Ornek Polinom Regresyon çizgisini içe aktarın numpyve matplotlib ile çizin:





# import numpy as np
# import matplotlib.pyplot as plt
#
#
#
#
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#
#
#
#
#
# mymodel = np.poly1d(np.polyfit(x, y, 3))
#
#
# myline = np.linspace(1, 22, 100)
#
#
#
# plt.scatter(x, y)
#
# plt.plot(myline, mymodel(myline))
#
# plt.show()






# Cikan Sonucumuz "img_polynomial_regression.png" adli diagrama bu sekilde yansitilmistir inceleyiniz







"""



Örnek Açıklama
--------------



---------------------------------------------------------------------------------------------------------------

İhtiyacınız olan modülleri içe aktarın.



NumPy modülü hakkında bilgi edinebilirsiniz NumPy Öğreticisi .
------------

SciPy modülü hakkında SciPy Eğitimimizde bilgi edinebilirsiniz .
------------



import numpy as np
import matplotlib.pyplot as plt


----------------------------------------------------------------------------------------------------------------



x ve y ekseninin değerlerini temsil eden dizileri oluşturun:






x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]

y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]



--------------------------------------------------------------------------------------------------------



NumPy, bir polinom modeli yapmamızı sağlayan bir metoda sahiptir:





mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))



---------------------------------------------------------------------------------------------------------



Ardından satırın nasıl görüneceğini belirtin, 1. pozisyondan başlayıp 22. pozisyonda bitirelim:





myline = numpy.linspace(1, 22, 100)



------------------------------------------------------------------------------------------------------------



Orijinal dağılım grafiğini çizin:





plt.scatter(x, y)



------------------------------------------------------------------------------------------------------------



Polinom regresyon çizgisini çizin:





plt.plot(myline, mymodel(myline))



--------------------------------------------------------------------------------------------------------------




Diyagramı görüntüleyin:





plt.show()




--------------------------------------------------------------------------------------------------------------




"""








# Simdi acalim biraz konuyu








"""




R-kare
------


X ve y ekseni değerleri arasındaki ilişkinin ne kadar iyi olduğunu bilmek önemlidir, eğer ilişki yoksa polinom 
---------------------------------- --------- -------  --- --------- ---------------------------------- -------
regresyonu hiçbir şeyi tahmin etmek için kullanılamaz.
---------- -----------------------------

İlişki, r-kare adı verilen bir değerle ölçülür.
-----   --------------------------------------

r-kare değeri 0 ile 1 arasındadır, burada 0 hiçbir ilişki olmadığı ve 1 %100 ilişkili anlamına gelir.
------------- ******* ------------        * ----------------------    * -------------


Python ve Sklearn modülü bu değeri sizin için hesaplayacaktır, tek yapmanız gereken onu x ve y dizileriyle beslemek:
------    --------------                      --------------                            ------ ----------- --------



"""






# Ornek Verilerim bir polinom regresyonuna ne kadar uyuyor?






# import numpy as np
# from sklearn.metrics import r2_score
#
#
#
#
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#
#
#
#
# mymodel = np.poly1d(np.polyfit(x, y, 3))
#
#
#
# print(r2_score(y, mymodel(x)))









# Not: 0.9432150416451026 sonucu, çok iyi bir ilişkinin olduğunu ve gelecek tahminlerinde polinom regresyonunu
# kullanabileceğimizi göstermektedir.







"""



Gelecekteki Değerleri Tahmin Edin
---------------------------------


Artık gelecekteki değerleri tahmin etmek için topladığımız bilgileri kullanabiliriz.

Örnek: Saat 17.00 civarında gişeden geçen bir arabanın hızını tahmin etmeye çalışalım:
-------------------------------------------------------------------------------------

Bunu yapmak mymodeliçin yukarıdaki örnekteki aynı diziye ihtiyacımız var :



mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))



"""






# Örnek Saat 17.00'de geçen bir arabanın hızını tahmin edin:






# import numpy as np
# from sklearn.metrics import r2_score
# import matplotlib.pyplot as plt
#
#
#
#
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#
#
#
#
# mymodel = np.poly1d(np.polyfit(x, y, 3))
#
#
#
# speed = mymodel(17)
#
#
#
# print(speed)








# Örnek, şemadan da okuyabileceğimiz bir hızın 88.87331269698007 olacağını öngördü:



# Burada cikan sonucu ayrica "img_polynomial_prediction.png" adli diagramdan inceleyibilirsiniz






"""


Kötü Uyum?
----------


Polinom regresyonunun gelecekteki değerleri tahmin etmek için en iyi yöntem olmayacağı bir örnek oluşturalım.


"""






# Ornek x ve y ekseni için bu değerler, polinom regresyonu için çok kötü bir uyumla sonuçlanmalıdır:






# import numpy as np
# import matplotlib.pyplot as plt
#
#
#
#
#
# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
#
#
#
#
# mymodel = np.poly1d(np.polyfit(x, y, 3))
#
#
#
# myline = np.linspace(2, 95, 100)
#
#
#
# plt.scatter(x, y)
#
# plt.plot(myline, mymodel(myline))
#
# plt.show()






# Burada gormus oldugumuz diagram "img_polynomial_badfit.png" polinom regresyonun kotu bir uyumla sonuclandigini gorebilirsiniz




# Ve r-kare değeri?






# Ornek Çok düşük bir r-kare değeri almalısınız.




import numpy as np
from sklearn.metrics import r2_score




x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]




mymodel = np.poly1d(np.polyfit(x, y, 3))




print(r2_score(y, mymodel(x)))







# Sonuç: 0.009952707566680652 çok kötü bir ilişkiyi gösterir ve bize bu veri setinin polinom regresyonu için uygun
# olmadığını söyler.





















