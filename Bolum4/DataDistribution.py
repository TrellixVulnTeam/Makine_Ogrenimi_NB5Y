"""

Veri Dağıtımı
-------------


Bu öğreticinin önceki bölümlerinde, yalnızca farklı kavramları anlamak için örneklerimizde çok az miktarda
veriyle çalıştık.


Gerçek dünyada, veri kümeleri çok daha büyüktür, ancak en azından bir projenin erken bir aşamasında gerçek dünya
verilerini toplamak zor olabilir.




Büyük Veri Kümelerini Nasıl Elde Edebiliriz?
-------------------------------------------


Test için büyük veri kümeleri oluşturmak için, herhangi bir boyutta rastgele veri kümeleri oluşturmak için
çeşitli yöntemlerle birlikte gelen Python modülü NumPy'yi kullanıyoruz.



"""


# Örnek  0 ile 5 arasında 250 rastgele kayan nokta içeren bir dizi oluşturun:



import numpy as np



x2 = np.random.uniform(0.0, 5.0, 250)


print(x2)



"""

# Cikan deger 0.0 ile 0.5 arasinda toplam 250 tane rasgele sayi urettik
-----------------------------------------------------------------------

[2.55897846 1.5630046  2.43321384 0.57155098 0.74200727 0.60230008
 1.86809308 2.09596064 1.23027042 4.90554039 2.65628373 1.10596365
 2.25306204 2.38197497 0.71598607 0.72536495 4.88132384 4.32994586
 4.38954194 2.43990144 2.99189258 3.12573598 1.86537769 4.36191319
 4.582714   1.93939895 2.66023128 4.74071244 1.40924642 0.06066989
 3.10400369 2.59612404 4.06598516 3.73708999 3.9799902  3.49355639
 2.49000345 2.86976233 4.47694529 0.91431706 0.28317063 4.91396067
 3.59344988 2.72690888 1.62071748 4.37062498 2.51461467 0.34370322
 4.76497177 4.50838341 0.91124205 0.51137991 0.05405577 1.83843608
 4.86059838 1.47132117 0.13749599 3.1613813  0.0971531  2.52287098
 4.35468913 1.90122909 2.39872601 2.10831469 4.37128274 3.3445744
 1.96340868 2.27603315 2.58293638 1.74459248 3.40825448 0.01408455
 0.37229917 1.37643493 0.96823248 0.48033769 1.94400369 1.22859381
 1.62789336 3.77184454 3.12600506 1.95492032 1.96498752 0.39468725
 0.11634664 2.205057   1.46653129 4.58176298 2.31523896 3.29981797
 0.40759353 3.90864411 4.21206213 3.55797646 0.3449249  4.96243566
 0.3446047  1.94184808 3.0820929  4.79021954 2.26484859 0.25584477
 0.06207677 1.32404584 3.20678896 4.43809493 3.47791393 0.07620392
 2.08645297 2.17127892 4.52181174 3.19522931 1.46055074 0.78155702
 2.10473452 0.1190374  4.04239023 1.03497227 1.52521652 0.53352846
 4.74940868 0.20052814 3.73881147 0.00923457 2.13480797 4.03815177
 1.82181803 0.26809332 1.58787593 2.83743912 4.97968921 0.561437
 1.43502025 0.72388603 0.04498829 1.68018409 0.43776591 3.52686467
 3.03130598 4.85896615 3.25190493 4.58744948 1.91726941 1.82982047
 1.99949603 1.86036596 1.89193261 4.88717659 4.29911125 3.84544249
 3.2149341  3.24719437 0.13932202 3.74499982 3.10847973 4.49692625
 4.69325479 4.8672857  1.27814714 4.41809578 1.74018537 3.79104746
 2.96739161 4.14443757 1.30295755 1.71203208 1.39773439 2.26202937
 3.34134797 1.75978828 1.32274209 1.50249165 1.93052935 4.11904541
 4.18257563 2.9447075  0.60545327 4.16996603 0.96387051 4.39525013
 2.3603757  0.96103026 1.79336503 3.83817159 2.46140582 0.46191697
 2.26549749 0.89194712 2.8806812  1.54330664 3.30403615 2.11074488
 2.01988054 4.94745366 3.78110902 3.13949833 3.99368246 2.03457489
 4.46496025 1.42709795 4.71254728 3.74110716 4.55150622 1.6486924
 3.73388917 3.52573406 4.52918829 2.75346264 2.80541848 3.04580193
 3.74908521 3.86831486 2.54597258 2.43467119 4.01428147 3.10197633
 4.79841671 3.93692841 2.75368028 1.93786795 0.94946937 1.4641997
 4.04801455 1.27459557 3.43577161 2.13968783 1.79829138 1.33565165
 1.5161402  2.67428451 1.93254137 1.33883866 3.78927704 0.09956802
 4.0503587  0.1608149  3.46652353 2.47948918 4.38584812 0.91764685
 3.88430767 1.06286619 1.40221915 1.00065288 4.84297514 3.43349487
 1.3064427  2.04368879 4.16219798 1.47081015]
 

"""


# Histogram


"""

Histogram
---------


Veri setini görselleştirmek için topladığımız verilerle bir histogram çizebiliriz.


Bir histogram çizmek için Python modülü Matplotlib'i kullanacağız.


Bizim de Matplotlib modülü hakkında bilgi Matplotlib Öğreticisi .


"""




# Örnek  Bir histogram çizin:



import numpy as np
import matplotlib.pyplot as plt


x3 = np.random.uniform(0.0, 0.5, 250)

plt.hist(x3, 5)

plt.show()




"""

Histogram Açıklaması
---------------------


5 çubuklu bir histogram çizmek için örnekteki diziyi kullanıyoruz. ------   ornek resim ( dosya icerisinde bulunan 'img_numpy_uniform3.png')


İlk çubuk, dizideki kaç değerin 0 ile 1 arasında olduğunu gösterir.
                                -------

İkinci çubuk, 1 ile 2 arasında kaç değer olduğunu gösterir.
              -------
              
Vb.



Bu bize şu sonucu verir:
------------------------

    - 52 değer 0 ile 1 arasındadır
    - 48 değer 1 ile 2 arasındadır
    - 49 değer 2 ile 3 arasındadır
    - 51 değer 3 ile 4 arasındadır
    - 50 değer 4 ile 5 arasındadır
    
    
    

Not: Dizi değerleri rastgele sayılardır ve bilgisayarınızda tam olarak aynı sonucu göstermez.
---------------------------------------------------------------------------------------------


"""


# Buyuk Veri Dagilimlari



"""


Büyük Veri Dağıtımları
----------------------

250 değer içeren bir dizi çok büyük sayılmaz ama artık rastgele bir değer kümesi oluşturmayı biliyorsunuz 
ve parametreleri değiştirerek istediğiniz kadar büyük veri kümesi oluşturabilirsiniz.


"""




# Ornek  100.000 rastgele sayı içeren bir dizi oluşturun ve bunları 100 çubuklu bir histogram kullanarak görüntüleyin:



import numpy as np
import matplotlib.pyplot as plt



x4 = np.random.uniform(0.0, 0.5, 100000)


plt.hist(x4, 100)

plt.show()




# 100.000 rastgele sayı içeren  ve bunları 100 çubuklu bir histogramda goruntuledigimiz resim  -- 'img_numpy_uniform_big3.png'










