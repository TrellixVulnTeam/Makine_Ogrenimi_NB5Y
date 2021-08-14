# Bolum 1


"""

Ortalama, Medyan ve Mod
-----------------------

Bir grup sayıya bakarak ne öğrenebiliriz?


Makine Öğreniminde (ve matematikte) bizi ilgilendiren genellikle üç değer vardır:
                                                                 ---------------

    Ortalama - Ortalama değer
    Medyan - Orta nokta değeri
    Mod - En yaygın değer


-----------------------------------------------

Örnek:
------

13 arabanın hızını kaydettik:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


Ortalama, orta veya en yaygın hız değeri nedir?


"""



# Bolum 2


"""

Ortalama
--------


Mean değer, ortalama değerdir.

Ortalamayı hesaplamak için tüm değerlerin toplamını bulun ve toplamı değer sayısına bölün:



(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77


NumPy modülünün bunun için bir yöntemi vardır. Bizim de NumPy modülü hakkında bilgi NumPy Öğreticisi .


"""


# Ornek ---- mean() Ortalama hızı bulmak için NumPy yöntemini kullanın :


import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)

print(x)


# Ortalama deger calistirdiginizda 89.76923076923077 bu sekilde olacaktir yani mean ortalama degeri verdi bize










# Bolum 3


"""

Medyan
------


Medyan değer, tüm değerleri sıraladıktan sonra ortadaki değerdir:
                                               --------

77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
                        --

Medyanı bulmadan önce sayıların sıralanması önemlidir.


NumPy modülünün bunun için bir yöntemi vardır:


"""




# Örnek   median() Orta değeri bulmak için NumPy yöntemini kullanın :

import  numpy as np


speed1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]


x1 = np.median(speed1)


print(x1)


# Cikan sonuc 87.0 sirali sistemde ortadaki degeri bulduk






"""

Ortada iki sayı varsa, bu sayıların toplamını ikiye bölün.
---------------------------------------------------------

77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
                    --  --

(86 + 87) / 2 = 86.5


"""


# ornek NumPy modülünü kullanma:


import numpy as np


speed3 = [99,86,87,88,86,103,87,94,78,77,85,86]

x3 = np.median(speed3)

print(x3)


# Burada ciktimiz 86.5 sirali giden sayilar ortasinda iki farkli sayi var ise numpyda bulunan median sirali sistemde olan ve ortasinda tespit edilen iki farkli sayiyi ikiye boluyor tek sayi olsaydi gerek kalmazdi








# Bolum 4


"""

Mod değeri en çok görünen değerdir:
           ------


99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86


SciPy modülünün bunun için bir yöntemi vardır. SciPy Eğitimimizde SciPy modülü hakkında bilgi edinin .


"""



# Örnek mode() En çok görünen sayıyı bulmak için SciPy yöntemini kullanın :


from scipy import stats


speed4 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x4 = stats.mode(speed4)

print(x4)


# Burada buldugumuz cikan sonuc  -- ModeResult(mode=array([86]), count=array([3])) -- burada bize kisaca sunu soyluyor ciktiiz bu listede en fazla 86 sayisi var ve 3 kere girilmis yani en fazla 86 sayisi var



"""

Bölüm özeti
-----------


Ortalama, Medyan ve Mod, Makine Öğreniminde sıklıkla kullanılan tekniklerdir, bu nedenle bunların arkasındaki 
kavramı anlamak önemlidir.

"""