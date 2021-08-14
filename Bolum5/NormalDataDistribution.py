"""

Normal Veri Dağılımı
--------------------

Önceki bölümde, belirli bir boyutta ve verilen iki değer arasında tamamen rastgele bir dizi oluşturmayı öğrendik.


Bu bölümde, değerlerin belirli bir değer etrafında yoğunlaştığı bir dizi oluşturmayı öğreneceğiz.


Olasılık teorisinde bu tür veri dağılımı, bu veri dağılımının formülünü bulan matematikçi Carl Friedrich
-------------------
Gauss'tan sonra normal veri dağılımı veya Gauss veri dağılımı olarak bilinir .
                --------------------      -------------------

"""




# Ornek  Tipik bir normal veri dağılımı:



import numpy as np
import matplotlib.pyplot as plt


x = np.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)

plt.show()




# cikan sonuc "img_numpy_normal.png" yani normal standard dagilim grafiginde gorebilirsiniz





"""


Histogram Açıklaması
--------------------


numpy.random.normal() 100 çubuklu bir histogram çizmek için yöntemden 100000 değer içeren diziyi kullanırız .
                      -----------                                     ------    
Ortalama değerin 5.0 ve standart sapmanın 1.0 olduğunu belirtiyoruz.
--------------------    ----------------------

Bu, değerlerin 5.0 civarında ve nadiren ortalamadan 1.0'dan daha uzakta yoğunlaşması gerektiği anlamına gelir.
               ---                                  -------      -------------------
Ve histogramdan da görebileceğiniz gibi, çoğu değer 4.0 ile 6.0 arasındadır ve tepe noktası yaklaşık 5.0'dır.
                                                    -----------                -----------------------------

"""



