# coding : utf-8

# solution devoir 1

url = "https://montrealcampus.ca?p="

l2 = list()
n = 20001
l2.append(str(n))
 
article = l2

for article in l2:
   n = n+1
   l2.append(str(n))
   print(url[0:28]+str(article))
   if (int(n)) == 30151:
       break
print(len(l2))