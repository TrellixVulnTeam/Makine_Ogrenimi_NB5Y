# Dagilim Grafigi

"""


Dağılım grafiği



Dağılım grafiği, veri kümesindeki her değerin bir nokta ile temsil edildiği bir diyagramdır.



# Ornek resim dosya icerisinde "img_scatterplot.png" goruntuleyiniz



Matplotlib modülünün dağılım grafikleri çizmek için bir yöntemi vardır, biri x ekseninin değerleri için diğeri
                     ------------------------------                     ------------------------------- ------
 y ekseninin değerleri için olmak üzere aynı uzunlukta iki diziye ihtiyaç duyar:
---------------------------             -------------------------





x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]



x Dizisi her arabanın yaşını temsil eder.
---------------------*-----*-----------

y Dizisi, her arabanın hızını temsil eder.
-----------------------*----*----------


"""





# Ornek  scatter() Bir dağılım grafiği çizmek için yöntemi kullanın :



import matplotlib.pyplot as plt
import numpy.random

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]



plt.scatter(x, y)

plt.show()





# Calistirdiktan sonra karsimiza cikan diagram "img_matplotlib_scatter.png" --- (  (x)  sirasi yasi  (y)  sirasi ise hiz bilgisini noktalarla gosteriyor






"""


Dağılım Grafiği Açıklaması
--------------------------



X ekseni yaşları ve y ekseni hızları temsil eder.
----------------    ----------------



Diyagramdan okuyabildiğimiz, en hızlı iki arabanın ikisinin de 2 yaşında olduğu ve en yavaş arabanın 
                             --------------------------------------------------    -----------------
12 yaşında olduğudur.
---------------------



***
Not: Araba ne kadar yeni olursa, o kadar hızlı gidiyor gibi görünüyor, ancak bu bir tesadüf olabilir, 
sonuçta sadece 13 araba kaydettik.
***


"""




# Rasgele Veri Dagilimlari





"""


Rastgele Veri Dağılımları
-------------------------


Makine Ogrenimi'nde veri kümeleri binlerce, hatta milyonlarca değer içerebilir.
                    ------------- --------        -----------------

Bir algoritmayı test ederken gerçek dünya verileriniz olmayabilir, rastgele oluşturulmuş değerler kullanmanız gerekebilir.
                             ------------------------------------   ------------------------------------------------------

Önceki bölümde öğrendiğimiz gibi, NumPy modülü bu konuda bize yardımcı olabilir!
                                  ------------

Her ikisi de normal bir veri dağılımından 1000 rastgele sayı ile dolu iki dizi oluşturalım.
*------------------------------------------------------------------------------------------*

İlk dizi, 1.0'lık bir standart sapma ile ortalamasi 5.0'a ayarlayacaktır.
--------  -------     --------------     -------------------------------

İkinci dizi, 2.0 standart sapma ile ortalama 10.0'a ayarlanacaktır:
----------   --- --------------     -------------------------------


"""





# Örnek  1000 noktalı bir dağılım grafiği:




import numpy as np
import matplotlib.pyplot as plt



x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)


plt.scatter(x, y)

plt.show()





# Ciktimiz bir diagram (x ve y eksenli) ortalamasi 5 ve standard sapma degeri 1.0 ve ortalamasi 10 olan ve standard sapma degeri 2.0  olan iki veri listesinin diagram uzerinde ki goruntusu
# --> * ' img_matplotlib_scatter_1000.png ' * #  <--






"""



Dağılım Grafiği Açıklaması
--------------------------


Noktaların x ekseninde 5, y ekseninde 10 değeri etrafında yoğunlaştığını görebiliriz.
------------------------  --------------------------------

Yayılmanın y ekseninde x ekseninden daha geniş olduğunu da görebiliriz.
---------------------- --------------------------------



"""
