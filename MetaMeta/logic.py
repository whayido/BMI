import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

x=(2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012)

y1=(103,114,112,107,114,113,100,98,106,101,107)

y2=(103,109,113,113,114,116,114,95,106,107,106) 

plt.plot(x,y1,color='purple',label='Индекс двухвалютного курса рубля,% к пред.году')

plt.plot(x,y2,color='pink', label='Оборот розничной торговли,% к пред.году')

plt.xlabel("Год")
plt.ylabel("Процент,%")
plt.title("Вариант 12",fontsize=17)

plt.grid(True)


plt.locator_params(axis='x',nbins=12)
plt.locator_params(axis='y',nbins=30)

plt.legend(loc='upper right',fontsize= 9)


plt.show()