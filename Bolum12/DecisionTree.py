# Decision Tree - Karar Agaci







# Gorseli inceleyin "img_ml_decision_tree.png icerisinde asamalar mevcut Bu bir Akis Semasidir"








"""





Karar ağacı
-----------



Bu bölümde size nasıl bir "Karar Ağacı" yapacağınızı göstereceğiz.
-----------------------------------------------------------------
Karar Ağacı bir Akış Şemasıdır ve önceki deneyimlere dayalı kararlar vermenize yardımcı olabilir.
-------------------------------------------------------------------------------------------------



Örnekte, bir kişi bir komedi şovuna gidip gitmeyeceğine karar vermeye çalışacaktır.
----------------------------------------------------------------------------------


Neyse ki örnek kişimiz kasabada her komedi şovu olduğunda kayıt olmuş ve komedyen hakkında bazı bilgileri
---------------------------------------------------------------------------------------------------------
kaydetmiş ve gitmiş olup olmadığını da kaydetmiştir.
---------------------------------------------------







Yaş	                Tecrübe Suresi	                Sira	                Milliyet	                Gitmek



36	                    10	                          9	              Birleşik Krallık	                HAYIR

42	                    12	                          4	        Amerika Birleşik Devletleri	            HAYIR

23	                    4	                          6	                    N	                        HAYIR

52	                    4	                          4	        Amerika Birleşik Devletleri	            HAYIR

43	                    21	                          8	        Amerika Birleşik Devletleri	            EVET

44	                    14	                          5	            Birleşik Krallık	                HAYIR

66	                    3	                          7	                    N	                        EVET

35	                    14	                          9	            Birleşik Krallık	                EVET

52	                    13	                          7	                    N	                        EVET

35	                    5	                          9	                    N	                        EVET

24	                    3	                          5	        Amerika Birleşik Devletleri	            HAYIR

18	                    3	                          7	            Birleşik Krallık	                EVET

45	                    9	                          9	            Birleşik Krallık	                EVET









Şimdi, bu veri setine dayanarak Python, herhangi bir yeni şovun katılmaya değer olup olmadığına karar vermek için
kullanılabilecek bir karar ağacı oluşturabilir.







O nasıl çalışır?
---------------



İlk önce ihtiyacınız olan modülleri içe aktarın ve veri setini pandas.read_csv ile okuyun:
---------------------------------------------------------------------------------




"""








# Örnek Veri setini okuyun ve yazdırın:








# import pandas
# from sklearn import tree
# import pydotplus
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg
#
#
#
#
# df = pandas.read_csv("shows.csv")
#
#
# print(df)







# Burada Ciktimiz bize "shows.csv" dosyasini okuyarak python consola yazdirdi






"""



    Age  Experience  Rank Nationality   Go
0    36          10     9          UK   NO
1    42          12     4         USA   NO
2    23           4     6           N   NO
3    52           4     4         USA   NO
4    43          21     8         USA  YES
5    44          14     5          UK   NO
6    66           3     7           N  YES
7    35          14     9          UK  YES
8    52          13     7           N  YES
9    35           5     9           N  YES
10   24           3     5         USA   NO
11   18           3     7          UK  YES
12   45           9     9          UK  YES



"""







# Simdi devam edelim







"""




Bir karar ağacı oluşturmak için tüm verilerin sayısal olması gerekir.
---------------------------------------------------------------------


Sayısal olmayan 'Nationality' ve 'Go' sütunlarını sayısal değerlere dönüştürmemiz gerekiyor.
-------------------------------------------------------------------------------------------


Pandaların, map() değerlerin nasıl dönüştürüleceği hakkında bilgi içeren bir sözlük alan bir yöntemi vardır.
-----------------------------------------------------------------------------------------------------------



{'UK': 0, 'USA': 1, 'N': 2}




'UK' değerlerini 0'a, 'USA' değerlerini 1'e ve 'N' değerlerini 2'ye dönüştürmek anlamına gelir.
----------------------------------------------------------------------------------------------



"""








# Örnek Dize değerlerini sayısal değerlere değiştirin:







# import pandas
# from sklearn import tree
# import pydotplus
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg
#
#
#
#
# df = pandas.read_csv("shows.csv")
#
#
#
#
# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)
#
#
#
#print(df)









# Burada Ciktimiz bize "shows.csv" dosyasinda bulunan  tüm verileri sayısal degerlere cevirdi.









"""


    Age  Experience  Rank  Nationality  Go
0    36          10     9            0   0
1    42          12     4            1   0
2    23           4     6            2   0
3    52           4     4            1   0
4    43          21     8            1   1
5    44          14     5            0   0
6    66           3     7            2   1
7    35          14     9            0   1
8    52          13     7            2   1
9    35           5     9            2   1
10   24           3     5            1   0
11   18           3     7            0   1
12   45           9     9            0   1



"""









# Hic durmadan devam ediyoruz :)










"""




Ardından, özellik sütunlarını hedef sütundan ayırmamız gerekir.
--------------------------------------------------------------



Özellik sütunları, tahmin etmeye çalıştığımız sütunlardır ve hedef sütun, tahmin etmeye çalıştığımız 
----------------------------------------------------------------------------------------------------
değerlerin bulunduğu sütundur.
------------------------------



"""









# Örnek X özellik sütunları, y hedef sütun:







# import pandas
# from sklearn import tree
# import pydotplus
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg
#
#
#
#
# df = pandas.read_csv("shows.csv")
#
#
#
#
# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)
#
#
#
#
# features = ['Age', 'Experience', 'Rank', 'Nationality']
#
# X = df[features]
# y = df['Go']
#
#
#
#print(X)
#print(y)









# Burada Ciktimiz bize "shows.csv" dosyasinda bulunan özellik sütunlarının hedef sütundan ayırdigimizi gosteriyor





"""



    Age  Experience  Rank  Nationality
0    36          10     9            0
1    42          12     4            1
2    23           4     6            2
3    52           4     4            1
4    43          21     8            1
5    44          14     5            0
6    66           3     7            2
7    35          14     9            0
8    52          13     7            2
9    35           5     9            2
10   24           3     5            1
11   18           3     7            0
12   45           9     9            0


0     0
1     0
2     0
3     0
4     1
5     0
6     1
7     1
8     1
9     1
10    0
11    1
12    1

Name: Go, dtype: int64



"""






# Artık gerçek karar ağacını oluşturabilir, onu ayrıntılarımıza sığdırabilir ve bilgisayara bir .png dosyası kaydedebiliriz:











# Örnek Bir Karar Ağacı oluşturun, onu bir resim olarak kaydedin ve resmi gösterin:





# import pandas
# from sklearn import tree
# import pydotplus
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg
#
#
#
# df = pandas.read_csv("shows.csv")
#
#
# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)
#
# features = ['Age', 'Experience', 'Rank', 'Nationality']
#
# X = df[features]
# y = df['Go']
#
#
#
#
# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)
# data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
# graph = pydotplus.graph_from_dot_data(data)
# graph.write_png('mydecisiontree.dot')
#
#
#
# img=pltimg.imread('mydecisiontree.png')
# imgplot = plt.imshow(img)
# plt.show()











"""


Sonuç Açıklaması Ayrica cikan sonucu yani png resmini gorebilirsiniz "img_ml_decision_tree.png"
----------------


Karar ağacı, bir komedyeni görmek isteyip istememe ihtimalinizi hesaplamak için önceki kararlarınızı kullanır.
-------------------------------------------------------------------------------------------------------------







Karar ağacının farklı yönlerini okuyalım: Buradan kontrol edin "img_decisiontree1.png"
-------------------------------------------------------------------------------------






Rank (Rutbe)
----------


Rank <= 6.5 --> 6.5 veya daha düşük rütbeli her komedyenin True oku (solda) ve geri kalanının False oku (sağda) izleyeceği anlamına gelir .
----

gini = 0.497 bölmenin kalitesine atıfta bulunur ve her zaman 0.0 ile 0.5 arasında bir sayıdır; burada 0.0, tüm örneklerin aynı sonucu aldığı anlamına gelir ve 0,5, bölmenin tam olarak ortada yapıldığı anlamına gelir.
----

samples = 13 Demek ki kararda bu noktada 13 komedyen kaldı ki bu ilk adım olduğu için hepsi bu.
-------

value = [6, 7] bu 13 komedyenden 6'sının "No" ve 7'sinin "Go" alacağı anlamına gelir.
-----











Gini
-------



Örnekleri bölmenin birçok yolu vardır, bu eğitimde GINI yöntemini kullanıyoruz.
-------------------------------------------------------------------------------

Gini yöntemi şu formülü kullanır:
---------------------------------


Gini = 1 - (x/n)2 - (y/n)2


Burada x, olumlu yanıtların ("GO") sayısıdır, n örnek sayısıdır ve y, bize bu hesaplamayı veren olumsuz yanıtların ("HAYIR") sayısıdır:



1 - (7 / 13)2 - (6 / 13)2 = 0.497









Simdi resimdeki su bolume goz atalim "img_decisiontree2.png"





Bir sonraki adım iki kutu içerir, bir kutu 'Rank' 6.5 veya daha düşük olan komedyenler için ve bir kutu geri 
kalanıyla birlikte.






True - 5 Komedyen Burada Bitiyor:
--------------------------------



gini = 0.0 tüm örneklerin aynı sonucu aldığı anlamına gelir.
----

samples = 5 bu branşta 5 komedyen kaldığı anlamına gelir (Rütbesi 6.5 veya daha düşük olan 5 komedyen).
-------

value = [5, 0] 5'in "NO" ve 0'ın "GO" alacağı anlamına gelir.









False - 8 Komedyen Devam Ediyor:
--------------------------------



Milliyet
--------



Nationality <= 0.5 uyruk değeri 0,5'ten az olan komedyenlerin soldaki oku takip edeceği (yani İngiltere'den herkes anlamına gelir) ve geri kalanların sağdaki oku izleyeceği anlamına gelir.
-----------

gini = 0.219 örneklerin yaklaşık %22'sinin bir yöne gideceği anlamına gelir.
-----

samples = 8 bu branşta 8 komedyen kaldığı anlamına gelir (8 komedyen, Rütbesi 6.5'ten yüksek).
-------

value = [1, 7] bu 8 komedyenden 1'inin "NO" ve 7'sinin "GO" alacağı anlamına gelir.
------





Teyit etmek icin su gorseli inceleyin "img_decisiontree3_2.png"











True - 4 Komedyen "GO":
----------------------


Yaş
---



Age <= 35.5 35,5 yaş ve altındaki komedyenlerin soldaki oku, geri kalanların ise sağdaki oku izleyeceği anlamına gelir.
---

gini = 0.375 örneklerin yaklaşık %37,5'inin bir yöne gideceği anlamına gelir.
----

samples = 4 bu branşta 4 komedyen kaldığı anlamına gelir (İngiltere'den 4 komedyen).
-------

value = [1, 3] bu 4 komedyenden 1'inin "NO" ve 3'ünün "GO" alacağı anlamına gelir.
-----












False - 4 Komedyen Burada Bitiriyor:
------------------------------------



gini = 0.0 tüm örneklerin aynı sonucu aldığı anlamına gelir.
-----

samples = 4 bu branşta 4 komedyen kaldığı anlamına gelir (İngiltere'den olmayan 4 komedyen).
-------

value = [0, 4] bu 4 komedyenden 0'ın "NO" ve 4'ünün "GO" alacağı anlamına gelir.
------






Teyit etmek icin simdide bu resmi inceleyebilirsiniz "img_decisiontree4_2.png"












True - 2 Komedyen Burada Bitiyor:
--------------------------------


gini = 0.0 tüm örneklerin aynı sonucu aldığı anlamına gelir.
----

samples = 2 bu branşta 2 komedyen kaldığı anlamına gelir (2 komedyen 35.5 yaşında veya daha genç).
-------

value = [0, 2] bu 2 komedyenden 0'ın "NO" ve 2'sinin "GO" alacağı anlamına gelir.
-----







False - 2 Komedyen Devam:
--------------------------


Tecrübe suresi
-------------



Experience <= 9.5  --> 9.5 yıl veya daha az deneyime sahip komedyenlerin soldaki oku, geri kalanların ise sağdaki oku izleyeceği anlamına gelir.
----------

gini = 0.5 örneklerin %50'sinin bir yöne gideceği anlamına gelir.
----

samples = 2 bu branşta 2 komedyen kaldığı anlamına gelir (35,5 yaşından büyük 2 komedyen).
-------

value = [1, 1] bu 2 komedyenden 1'inin "NO" ve 1'inin "GO" alacağı anlamına gelir.
-----










Simdi "img_decisiontree5.png" resminden teyit edebilirsiniz













True - 1 Komedyen Burada Bitiyor:
---------------------------------



gini = 0.0 tüm örneklerin aynı sonucu aldığı anlamına gelir.
----

samples = 1 bu branşta 1 komedyen kaldığı anlamına gelir (1 komedyen 9,5 yıl veya daha az deneyime sahip).
-------

value = [0, 1] 0'ın "NO" alacağı ve 1'in "GO" alacağı anlamına gelir.
-----








False - 1 Komedyen Burada Bitiyor:
-----------------------------------




gini = 0.0 tüm örneklerin aynı sonucu aldığı anlamına gelir.
----

samples = 1 bu branşta 1 komedyen kaldığı anlamına gelir (1 komedyen 9,5 yıldan fazla deneyime sahip).
-------

value = [1, 0] 1'in "NO" ve 0'ın "GO" alacağı anlamına gelir.
------













Tahmin Değerleri
----------------------




Yeni değerleri tahmin etmek için Karar Ağacını kullanabiliriz.
--------------------------------------------------------------




"""







# Ornege Goz Atalim







"""

Örnek: 40 yaşında, 10 yıllık deneyime sahip ve komedi sıralaması 7 olan bir Amerikalı komedyenin oynadığı 
---------------------------------------------------------------------------------------------------------
bir gösteriye gitmeli miyim?
----------------------------

"""





# Ornek Yeni değerleri tahmin etmek için predict() yöntemini kullanın:




# import pandas
# from sklearn import tree
# import pydotplus
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg
#
#
#
# df = pandas.read_csv("shows.csv")
#
#
# d = {'UK': 0, 'USA': 1, 'N': 2}
# df['Nationality'] = df['Nationality'].map(d)
# d = {'YES': 1, 'NO': 0}
# df['Go'] = df['Go'].map(d)
#
# features = ['Age', 'Experience', 'Rank', 'Nationality']
#
# X = df[features]
# y = df['Go']
#
#
#
#
# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)
#
#
# print(dtree.predict([[40, 10, 7, 1]]))
#
#
# print("[1] means 'GO'")
# print("[0] means 'NO'")







# Cikan Sonuca bakalim asagida inceleyin




# Ilk sorumuzu hatirlayalim!



# Soru: 40 yaşında, 10 yıllık deneyime sahip ve komedi sıralaması 7 olan bir Amerikalı komedyenin oynadığı
# bir gösteriye gitmeli miyim?



# [1]                          -> Evet cevabimiz gitmekten yana yani gitmeliyim tahminler bu dogrultuda


# [1] means 'GO'            -> Gitmek  Anlami tasiyor
# [0] means 'NO'            -> Gitmemek  Anlami tasiyor






# Basarili bir tahmindi :)











# Peki ya Komedi sıralaması 6 olsaydı cevap ne olurdu?      Hadi Bakalim!!






import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg



df = pandas.read_csv("shows.csv")


d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']




dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)


print(dtree.predict([[40, 10, 6, 1]]))                              # Sadece siralamamiz degisti 7 idi 6 oldu


print("[1] means 'GO'")
print("[0] means 'NO'")





# [0]                          -> Evet cevabimiz gitmemekten yana yani gitmek mantikli degil tahminler bu dogrultuda


# [1] means 'GO'            -> Gitmek  Anlami tasiyor
# [0] means 'NO'            -> Gitmemek  Anlami tasiyor










# Tahminlerimiz bence fena degil amaaaaa!!! soyle bir durum var... Farkli Sonuclar evettt malesef





"""



Farklı Sonuçlar
---------------



Karar Ağacı'nı aynı verilerle besleseniz bile yeterince çalıştırırsanız size farklı sonuçlar verdiğini göreceksiniz.
----------------------------------------------------------------------------- ************** ----------------------


Bunun nedeni, Karar Ağacı'nın bize %100 kesin bir cevap vermemesidir. Bir sonucun olasılığına dayanır ve cevap değişecektir.
---------------------------------- **** ----------------------------  ----------- *********** ------- -- *******************


"""




# Dersimiz bitti umarim makine ogrenimi hakkinda bilgi edinmissinizdir ama daha fazla calismaniz gerektigini unutmayin
# Bu konular derin ogrenme ve ozel pyhon kutuphaneleri ile bagintilidir. Iyi calismalar dilerim




# by @Songurdeveloper

