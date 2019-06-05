import requests
import facebook
import json

#print("fetch")
'''
app_id = '1982798855161094'
app_secret = '9fdbdb87bb84c998c612c98df961154e'
graph = facebook.GraphAPI()
access_token = graph.get_app_access_token(app_id, app_secret) 

link = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + app_id +"&client_secret=" + app_secret + "&fb_exchange_token=" + access_token
print(link)
s = requests.Session()
token = s.get(link).content
token=json.loads(token)
token=token.get('access_token')
print(token)
'''

try:
    f1 = open('F:/Softwares/XXAMP/htdocs/final/access_token.txt','r')
    acc = f1.read()
    #print(acc)

    token = "EAAcLWFVsRQYBAH13HmHwBctoC4ITfMxqIIym0zbGuweLWnZCKFW3SlbhZA7HZBQPRBdRb4WZAZAYXOZClpM24vPOMAw80gsGgtoP1aYZATDiBw5RstB3zV4UExE0vkAGRIZC2oKnxGfw8e9uNY7Noe9Wao3T7XxikiKH3ycn09ZCQAuSuOgZBcEcPl8SUvwv6EyjQZD"
    token = acc
    me = "https://graph.facebook.com/v3.2/me?access_token="+token 
    #print("<br>"+me)
    likes = "https://graph.facebook.com/v3.2/me/likes?access_token="+token
    movies = "https://graph.facebook.com/v3.2/me/movies?access_token="+token
    posts = "https://graph.facebook.com/v3.2/me/posts?access_token="+token
    books = "https://graph.facebook.com/v3.2/me/books?access_token="+token
    
    
    me1 = requests.get(me)
    me1_file = open("python/me1.txt", "w")
    me1_file.write(me1.text)  
    me1_file.close()
    
    
    movies1 = requests.get(movies)
    movies1_file = open("python/movies1.txt", "w")
    movies1_file.write(movies1.text)
    movies1_file.close()
    
    books1 = requests.get(books)
    books1_file = open("python/books1.txt", "w")
    books1_file.write(books1.text)
    books1_file.close()
    
    
    me1_file = open("python/me1.txt", "r", encoding="utf-8")
    me1_json = json.load(me1_file)
    me1_file.close()
    
    
    books1_file = open("python/books1.txt", "r", encoding="utf-8")
    books1_json = json.load(books1_file)
    books1_file.close()
    
    
    movies1_file = open("python/movies1.txt", "r", encoding="utf-8")
    movies1_json = json.load(movies1_file)
    movies1_file.close()
    
    movies1_file_name = open("python/movies1_name.txt", "w")
    for x in movies1_json['data']:
        if '-' in x['name']:
            movies1_file_name.write(x['name'].replace('-','(')+')')
            movies1_file_name.write('\n')
        else:
            movies1_file_name.write(x['name'])
            movies1_file_name.write('\n')
        
    movies1_file_name.close()
    
    books1_file_name = open("python/books1_name.txt", "w")
    for x in books1_json['data']:
        books1_file_name.write(x['name'])
        books1_file_name.write('\n')
    
    books1_file_name.close()
    
    
    
    '''
    likes1 = requests.get(likes)
    likes1_file = open("python/likes1.txt", "w")
    likes1_file.write(likes1.text)
    likes1_file.close()
    
    posts1 = requests.get(posts)
    posts1_file = open("python/posts1.txt", "w")
    posts1_file.write(posts1.text)
    posts1_file.close()
    
    likes1_file = open("python/likes1.txt", "r", encoding="utf-8")
    likes1_json = json.load(likes1_file)
    likes1_file.close()
    
    posts1_file = open("python/posts1.txt", "r", encoding="utf-8")
    posts1_json = json.load(posts1_file)
    posts1_file.close()
    
    
    likes1_file_name = open("likes1_name.txt", "w")
    for x in likes1_json['data']:
        likes1_file_name.write(x['name'])
        likes1_file_name.write("\n")
        
    likes1_file_name.close()
    '''
    
    '''
    posts1_file_name = open("posts1_name.txt", "w")
    for x in posts1_json['data']:
        if(x['message']!=None):
            posts1_file_name.write(x['message'])
            posts1_file_name.write("\n")
        
    posts1_file_name.close()
    '''
    
    '''
    me1_file_name = open("me1_name.txt", "w")
    for x in me1_json:
        me1_file_name.write(x['name'])
        me1_file_name.write("\n")
        
    me1_file_name.close()
    '''
    
    '''
    likes1_file_name = open("likes1_name.txt", "w")
    likes1_file_name.write(str(likes1_json['data']).replace('\'','\"'))
    likes1_file_name.close()
    
    likes1_file_name = open("likes1_name.txt", "r", encoding="utf-8")
    likes1_json_name = json.load(likes1_file_name)
    likes1_file_name.close()
    '''
    
    #print(me1_json)
    #print(likes1_file_name)
    #print("In fetch_data last")
    
    #print("last_fetch")
except Exception as e:
    print(str(e))