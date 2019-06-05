import numpy as np
import pandas as pd 
import sys
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import time


data = pd.read_csv("python/data/data.csv", encoding='iso-8859-1')
book_names = np.loadtxt('python/books1_name.txt', dtype='str', usecols=None, delimiter='\n') 
writeFile1 = open('python/recom_books.txt', 'w')


attempts = 5
for x in book_names:
    try:
        usr_title = x
        # usr_title = input("Enter Title: ")
        # usr_author = input("Enter Author: ")
        # found = data[(data.book_name == usr_title) & (data.author == usr_author)]
        found = data[(data.book_name == usr_title)]
        found_book = found['ID']
        id_target = found_book.tolist()[0]
    except IndexError:
        print("**** Title and/or Author Incorrect or Book is not in corpus****\nPlease try again")
        # sys.exit(1)
    else:
        print("************** Searching for Book *******************")
        break
    
# Start timer
start_time = time.time()

data = data.drop('>', 1)
data = data.drop('(', 1)
data = data.drop('[', 1)
data = data.drop('{', 1)
data = data.drop('#', 1)
data = data.drop('&', 1)
data = data.drop('/', 1)
data = data.drop('\\', 1)
data = data.drop('*', 1)
data = data.drop('@', 1)
data = data.drop('_', 1)
data = data.drop('^', 1)


data = pd.concat([data, pd.get_dummies(data['smallClusterId'], prefix="general")], axis=1)  
data = pd.concat([data, pd.get_dummies(data['mediumClusterId'], prefix="medium")], axis=1) 
data = pd.concat([data, pd.get_dummies(data['largeClusterId'], prefix="specific")], axis=1) 
data = pd.concat([data, pd.get_dummies(data['author'])], axis=1)  

titles = data['book_name']
authors = data['author']
IDs = data['ID']

data = data.drop('ID', 1)
data = data.drop('book_name', 1)
data = data.drop('mediumClusterId', 1)
data = data.drop('smallClusterId', 1)
data = data.drop('largeClusterId', 1)
data = data.drop('author', 1)
data = data.drop('filename', 1)
data = data.fillna(0)


scaler = MinMaxScaler()
data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

data['ID'] = IDs   

print("Completed in %.3f seconds..." % (time.time() - start_time))

status = "*********** Finding Recommendations ***************"
print(status)
start_time = time.time()

example = data[data['ID']==id_target]
example = example.drop('ID', 1)
data = data.drop('ID', 1)


neigh = NearestNeighbors(5)
neigh = neigh.fit(data)


# print "example ", example
output = neigh.kneighbors(example, 15)
a = output[0]
b = output[1]
# print "Distance ", a
# print "Nearest Neighbor ", b
b = b.tolist()
b = b[0]

fulldata = data
fulldata['author'] = authors
fulldata['book_name'] = titles
results = data.iloc[b,:]
# print results.shape
results = results[['book_name','author']]
print("Completed in %.3f seconds..." % (time.time() - start_time))

status = "************* Your Recommendations ***************"
print(status)
print(results)
for index, row in results.iterrows():
    print(row['book_name'])
    writeFile1.write(row['book_name']+'\n') 
    
writeFile1.close()