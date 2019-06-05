import requests
import numpy as np

url1 = 'https://api.themoviedb.org/3/search/movie?api_key=58d0835042567afd821659c32cb13765&query='

try:
	recom = np.loadtxt('F:/Softwares/XXAMP/htdocs/final/python/recom_movies.txt', dtype='str', usecols=None, delimiter='\n') 
	#print(recom)
	# f = open("test.php",'w')

	for y in recom:
		#print(y[:-7])
		try:
			url1 = 'https://api.themoviedb.org/3/search/movie?api_key=58d0835042567afd821659c32cb13765&query='+y[:-7]
			#print(url1)
			resp = requests.get(url=url1)
			data = resp.json()
			base_url = 'http://image.tmdb.org/t/p/w185/'
			#print(data)

			for x in data['results']:
				if(isinstance(x['poster_path'], str) and isinstance(x['title'], str) and isinstance(x['release_date'], str)):
					print('<div class="col-3 pl-0 pr-0 text-center mb-2 pt-2 border border-dark"><img src="'+base_url+x['poster_path']+'"</img><h3>'+x['title']+'</h3><p>Release Date:'+x['release_date']+'</p></div>')
					break
		except Exception as e:
			pass

		
except Exception as e:
	print(e)
	exit()

