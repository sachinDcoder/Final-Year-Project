import requests

url = "https://api.themoviedb.org/3/movie/popular?api_key=58d0835042567afd821659c32cb13765"
resp = requests.get(url=url)
data = resp.json()


base_url = 'http://image.tmdb.org/t/p/w185/'
print("<br>")
c = 0
for x in data['results']:
	if c<12:
		print('<div class="col-3 mb-2 pt-2 text-center border border-dark"><img src="'+base_url+x['poster_path']+'"</img><h3>'+x['title']+'</h3><p>Release Date:'+x['release_date']+'</p></div>')
	else:
		break
	c+=1

