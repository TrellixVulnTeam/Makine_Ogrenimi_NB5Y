# Train/Test -- Egitim/Test




"""


Modelinizi Değerlendirin
------------------------



Makine Öğreniminde, ağırlığı ve motor boyutunu bildiğimizde bir arabanın CO2 emisyonunu tahmin ettiğimiz önceki
------------------ ----------------------------------------- --------------------------------------------------
bölümde olduğu gibi, belirli olayların sonucunu tahmin etmek için modeller oluşturuyoruz.
----------------------------------------------------------------------------------------

Modelin yeterince iyi olup olmadığını ölçmek için Train/Test adlı bir yöntem kullanabiliriz.
--------------------------------------------------------------------------------------------





Tren/Test Nedir?
---------------



Train/Test, modelinizin doğruluğunu ölçmek için kullanılan bir yöntemdir.
------------------------------------------------------------------------

Train/Test olarak adlandırılır çünkü veri kümesini iki kümeye bölersiniz: bir eğitim kümesi ve bir test kümesi.
---------------------------------------------------------------------------------------------------------------




Eğitim için %80 ve test için %20.
---------------    -------------



Modeli eğitim setini kullanarak eğitirsiniz.
-------------------------------------------
Test setini kullanarak modeli test edersiniz .
--------------------------------------------




Modeli eğitmek , modeli oluşturmak anlamına gelir .
-------------------------------------------------
Test aracı model doğruluğunu test modeli.
----------------------------------------








Bir Veri Kümesiyle Başlayın
---------------------------





Test etmek istediğiniz bir veri seti ile başlayın.
--------------------------------------------------

Veri setimiz bir mağazadaki 100 müşteriyi ve onların alışveriş alışkanlıklarını göstermektedir.
----------------------------------------------------------------------------------------------



"""








# Ornek  Veri setimiz bir mağazadaki 100 müşteriyi ve onların alışveriş alışkanlıklarını göstermektedir.






# import numpy as np
# import matplotlib.pyplot as plt
#
#
#
#
# np.random.seed(2)
#
#
#
#
# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
#
#
#
#
# plt.scatter(x, y)
#
#
# plt.show()








# Sonuç: aldigimiz bu bolumde "img_traintest1.png" adli diyagramdan sonucu inceleyebilirsiniz



# X ekseni, satın alma yapmadan önceki dakika sayısını temsil eder.

# Y ekseni, satın alma işlemine harcanan para miktarını temsil eder.








"""




Tren/Test olarak Böl
--------------------





Eğitim seti, orijinal verilerin %80'inden  rastgele secilmis olmalı.
-------------------------------------------------------------------

Test grubu ise kalan %20'lik kisim olmalı.
-----------------------------------------



train_x = x[:80]        Eğitim seti     -->
                                                % 80
train_y = y[:80]        Eğitim seti     -->



test_x = x[80:]         Test grubu      -->  
                                                % 20
test_y = y[80:]         Test grubu      -->










Eğitim Setini Görüntüle
-----------------------




Eğitim seti ile aynı dağılım grafiğini görüntüleyin:





Örnek



plt.scatter(train_x, train_y)

plt.show()








Sonuç: Karsimiza cikan "img_traintest2.png" adli diyagramdaki veriler


Orijinal veri kümesine benziyor, bu yüzden adil bir seçim gibi görünüyor:








Test Setini Görüntüle
---------------------


Test setinin tamamen farklı olmadığından emin olmak için test setine de bir göz atacağız.




Örnek
-----


plt.scatter(test_x, test_y)
plt.show()




Sonuç: Karsimiza cikan "img_traintest3.png" adli diyagramdaki

Test seti ayrıca orijinal veri setine benziyor:










Veri Kümesini Sığdır
--------------------






Veri seti neye benziyor? 


Bence en uygun olanı polinom regresyonu olur, bu yüzden bir polinom regresyon doğrusu çizelim.
----------------------------------------------------------------------------------------------

Veri noktalarından bir çizgi çekmek icin  plt.plot() matplotlib modülünün yöntemini kullanıyoruz :
-----------------------------------



"""









# Örnek Veri noktalarından bir polinom regresyon çizgisi çizin:








# import numpy as np
# import matplotlib.pyplot as plt
#
#
#
# np.random.seed(2)
#
#
# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
#
#
# train_x = x[:80]
# train_y = y[:80]
#
#
# test_x = x[80:]
# test_y = y[80:]
#
#
#
# mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
#
#
# myline = np.linspace(0, 6, 100)
#
#
#
#
# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()









# Sonuc Karsimiza cikan "img_traintest3_2.png" adli diyagramdaki veriler







# Sonuç, veri kümesinin dışındaki değerleri tahmin etmeye çalışırsak bize bazı garip sonuçlar verecek olsa da, '
# bir polinom regresyonuna uyan veri kümesi önerimi destekleyebilir. Örnek: satır, mağazada 6 dakika geçiren bir
# müşterinin 200 değerinde bir satın alma yapacağını gösterir. Bu muhtemelen fazla uydurmanın bir işaretidir.



# Peki ya R-kare puanı? R-kare puanı, veri setimin modele ne kadar iyi uyduğunun iyi bir göstergesidir.







"""



R2
--



R-kare olarak da bilinen R2'yi hatırlıyor musunuz?
--------------------------------------------------



X ekseni ile y ekseni arasındaki ilişkiyi ölçer ve 0 ile 1 arasında değişir; burada 0, ilişki yok ve 1 tamamen 
--------------------------------------------------------------------------------------------------------------
ilişkili anlamına gelir.
-----------------------


Sklearn modülünün r2_score() bu ilişkiyi bulmamıza yardımcı olacak adında bir metodu vardır 
----------------- ********** --------------------------------------------------------------


Bu durumda müşterinin mağazada kaldığı dakikalar ile ne kadar para harcadıkları arasındaki ilişkiyi ölçmek istiyoruz.
--------------------------------------------------------------------------------------------------------------------



"""










# Örnek Eğitim verilerim bir polinom regresyonuna ne kadar uyuyor?







# import numpy as np
# from sklearn.metrics import r2_score
#
#
#
#
#
# np.random.seed(2)
#
#
#
#
#
# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
#
#
#
#
#
# train_x = x[:80]
# train_y = y[:80]
#
# test_x = x[80:]
# test_y = y[80:]
#
#
#
#
# mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
#
#
#
# r2 = r2_score(train_y, mymodel(train_x))
#
#
# print(r2)








# Not: 0.799 sonucu, bir OK ilişkisi olduğunu gösterir.







"""



Test Setini Getirin
-------------------



Şimdi, en azından eğitim verileri söz konusu olduğunda, tamam olan bir model yaptık.
-----------------------------------------------------------------------------------

Şimdi aynı sonucu verip vermediğini görmek için modeli test verileriyle de test etmek istiyoruz.
-----------------------------------------------------------------------------------------------



"""










# Örnek Test verilerini kullanırken R2 puanını bulalım:





# import numpy as np
# from sklearn.metrics import r2_score
#
#
#
#
# np.random.seed(2)
#
#
#
#
# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x
#
#
#
# train_x = x[:80]
# train_y = y[:80]
#
#
#
# test_x = x[80:]
# test_y = y[80:]
#
#
#
#
# mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
#
#
# r2 = r2_score(test_y, mymodel(test_x))
#
#
#print(r2)







# Not: 0.8086921460343559  sonucu, modelin test kümesine de uyduğunu gösterir ve modeli gelecekteki değerleri tahmin
# etmek için kullanabileceğimizden eminiz.








"""





Tahmin Değerleri
----------------


Artık modelimizin iyi olduğunu belirlediğimize göre, yeni değerleri tahmin etmeye başlayabiliriz.
-------------------------------------------------------------------------------------------------



"""




# Örnek Satın alan bir müşteri, dükkanda 5 dakika kalırsa ne kadar para harcar?







import numpy as np
from sklearn.metrics import r2_score




np.random.seed(2)




x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x



train_x = x[:80]
train_y = y[:80]



test_x = x[80:]
test_y = y[80:]




mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))




print(mymodel(5))









# Örnek, şemaya  "img_traintest_predict.png"  karşılık geldiği gibi, müşterinin 22.88 dolar harcamasını öngördü:







