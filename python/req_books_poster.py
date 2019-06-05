import requests
import numpy as np



try:
	recom = np.loadtxt('F:/Softwares/XXAMP/htdocs/final/python/recom_books.txt', dtype='str', usecols=None, delimiter='\n') 
	#print(recom)
	# f = open("test.php",'w')
	recom = list(recom)

	for y in recom:
		#print()
		#print(y)
		url1 = 'https://www.googleapis.com/books/v1/volumes?key=AIzaSyBTqxHtvOlk2hhErMUBrLIbPDzLx3e0Cqw&q=intitle:'
		url1 = url1 + y
		response = requests.get(url=url1)
		data = response.json()
		
		try:
			for x in data['items']:
				#print(x['volumeInfo']['title'])
				#print(x['volumeInfo']['imageLinks']['thumbnail'])
				#print(x['volumeInfo']['publishedDate'])
				try:
					if(isinstance(x['volumeInfo']['title'], str) and isinstance(x['volumeInfo']['imageLinks']['thumbnail'], str)):
						print('<div class="col-3 text-center mb-2 pt-2 border border-dark"><img src="'+x['volumeInfo']['imageLinks']['thumbnail']+'"</img><h3>'+x['volumeInfo']['title']+'</h3><p>Release Date:'+x['volumeInfo']['publishedDate']+'</p></div>')
						break
				except:
					pass
		except:
			pass
			
except Exception as e:
	print(str(e))
	exit()

