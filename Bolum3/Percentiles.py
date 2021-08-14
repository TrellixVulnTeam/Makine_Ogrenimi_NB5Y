"""

Yüzdelikler nedir?
-----------------

Yüzdelikler, istatistiklerde, değerlerin belirli bir yüzdesinin daha düşük olduğu değeri tanımlayan
bir sayı vermek için kullanılır.




Örnek: Diyelim ki bir sokakta yaşayan tüm insanların yaşlarından oluşan bir dizimiz var.
-----


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]



75. yüzdelik nedir? Cevap 43, yani insanların %75'i 43 yasinda veya daha genç.
--                        --                  --------


NumPy modülünün belirtilen yüzdelik dilimini bulmak için bir yöntemi vardır:
----------------------------------------------------------------------------


"""



# Örnek percentile() Yüzdelikleri bulmak için NumPy yöntemini kullanın :


import numpy as np



ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 75)

print(x)




# Örnek İnsanların %90'ının yaşı kaçtır?


import numpy as np


ages1 = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x1 = np.percentile(ages1, 90)

print(x1)


# aldigimiz sonuc 61.0 yani insanlarin %90'inin yasi 61 e denk geliyor
