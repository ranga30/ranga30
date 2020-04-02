import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import re

html = requests.get('https://www.instagram.com/username')
soup = BeautifulSoup(html.text, 'lxml')

data = soup.find_all('meta', attrs={'property':'og:description'})
text = data[0].get('content').split()

user = '%s %s %s' % (text[-3], text[-2], text[-1])
str =  ''.join(user)
print(str)
followers = text[0]
following = text[2]
print('User:', user)
print('Followers:', followers)
print('Following:', following)
f=np.array([int(s) for s in followers.split() if s.isdigit()])
h=np.array([int(a) for a in following.split() if a.isdigit()])
l=np.concatenate((f, h), axis=None)
g=np.zeros(2)
ax = plt.subplot(111)
plt.pie(l,g,labels=['followers','following'],autopct='% 2f% %')
ax.set_title(str+"Instagram profile")
plt.show()

