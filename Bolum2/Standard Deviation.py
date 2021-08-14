# Bolum 1


"""

Standart Sapma nedir?
---------------------


Standart sapma, değerlerin ne kadar yayıldığını açıklayan bir sayıdır.


Düşük bir standart sapma, sayıların çoğunun Mean (ortalama) değere yakın olduğu anlamına gelir.
-------------------------                   -----------------------------

Yüksek standart sapma, değerlerin daha geniş bir aralığa yayıldığı anlamına gelir.
---------------------                  ---------------------------



Örnek: Bu sefer 7 arabanın hızını kaydettik:
-------------------------------------------


speed = [86,87,88,86,87,85,86]



Standart sapma:
--------------

0.9



Bu, değerlerin çoğunun, 86.4 olan ortalama değerden 0.9 aralığında olduğu anlamına gelir. standart sapma dusuktur degerlerin ortalamasinin birbirine yakin olduguna isaret eder dusuk standart sapma vardir
                        ----                        ---




Aynı şeyi daha geniş bir aralıkta bir sayı seçimi ile yapalım:


speed = [32,111,138,28,59,77,97]


Standart sapma:
--------------


37.85



Degerlerin ortalamasinin birbirinden uzak olduguna isaret eder standart sapma yuksektir



Yani değerlerin çoğu, ortalama değer olan 77,4'ten 37,85 aralığındadır.

Gördüğünüz gibi, daha yüksek bir standart sapma, değerlerin daha geniş bir aralığa yayıldığını gösterir.

-----------------------------------------------------------------------------------------------------------------------
Not: Listedeki sayilarin ortalamasini buluyoruz ve ardindan buldugumuz ortalama degeri ikiye bolup standart sapma degerine ulasabiliriz
------------------------------------------------------------------------------------------------------------------------

NumPy modülünün standart sapmayı hesaplamak için bir yöntemi vardır:


"""




# Ornek  std() Standart sapmayı bulmak için NumPy yöntemini kullanın :


import numpy as np



speed = [86,87,88,86,87,85,86]


x = np.std(speed)


print(x)


# Burada ciktimiz 0.9035079029052513  yani standard sapma degerimiz cok dusuktur





# Ornek std() Standart sapmayı bulmak için NumPy yöntemini kullanın :



import numpy as np


speed1 = [32,111,138,28,59,77,97]


x1 = np.std(speed1)


print(x1)



# Burada ciktimiz 37.84501153334721 yani standart sapma degeri cok yuksek




"""

Varyans
-------


Varyans, değerlerin ne kadar yayılmış olduğunu gösteren başka bir sayıdır.
                             --------------------------

Aslında varyansın karekökünü alırsanız standart sapmayı elde edersiniz!
        -----------------------------------------------

Ya da tam tersi, standart sapmayı kendisiyle çarparsanız varyansı elde edersiniz!
                 --------------------------------------- --------

Varyansı hesaplamak için aşağıdaki gibi yapmanız gerekir:



1. Ortalamayı bulun:


(32+111+138+28+59+77+97) / 7 = 77.4



2. Her değer için: ortalamadan farkı bulun:




 32 - 77.4 = -45.4
 111 - 77.4 =  33.6
 138 - 77.4 =  60.6
 28 - 77.4 = -49.4
 59 - 77.4 = -18.4
 77 - 77.4 = - 0.4
 97 - 77.4 =  19.6
 
 
 

 3. Her bir fark için: kare değerini bulun:



 (-45.4)2 = 2061.16
 (33.6)2 = 1128.96
 (60.6)2 = 3672.36
 (-49.4)2 = 2440.36
 (-18.4)2 =  338.56
 (- 0.4)2 =    0.16
 (19.6)2 =  384.16
 
 
 


4. Varyans, bu kare farkların ortalama sayısıdır:


(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2




Neyse ki, NumPy'nin varyansı hesaplamak için bir yöntemi var:


"""


# Ornek var() Varyansı bulmak için NumPy yöntemini kullanın :


import numpy as np



speed2 = [12,86,64,28,95,19]

x2 = np.var(speed2)

print(x2)




"""

Standart sapma
--------------


Öğrendiğimiz gibi, standart sapmayı bulmak için formül varyansın kareköküdür:
                                                       --------------------


√1432.25 = 37.85    -> Burada kisaca ilk olarak varyansi bulduk varyansin karekoku ise bize islemimizin standard sapma sonucunu veriyor



Veya önceki örnekte olduğu gibi, standart sapmayı hesaplamak için NumPy'yi kullanın:


"""



# Ornek std() Standart sapmayı bulmak için NumPy yöntemini kullanın :


import numpy as np



speed3 = [32,111,138,28,59,77,97]

x3 = np.std(speed3)

print(x3)





"""


Semboller
---------


Standart Sapma genellikle Sigma sembolü ile temsil edilir: σ
--------------            -------------

Varyans genellikle Sigma Karesi sembolü ile temsil edilir: σ 2
-------            --------------------







-----------
Bölüm özeti
-----------

Standart Sapma ve Varyans, Makine Öğreniminde sıklıkla kullanılan terimlerdir, bu nedenle bunların nasıl 
alınacağını ve arkasındaki kavramı anlamak önemlidir.


"""
