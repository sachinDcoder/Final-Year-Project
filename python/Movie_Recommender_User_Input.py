#print("movie rec")

try:
    import numpy as np
    import pandas as pd
    from sklearn.metrics import pairwise_distances
    from scipy.spatial.distance import cosine, correlation

    #print("movie rec")

    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_csv('python/u.data', sep='\t', names=r_cols,
                          encoding='latin-1')
    
    #print("movie rec1")
    
    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
    movies = pd.read_csv('python/u.item', sep='|', names=m_cols, usecols=range(5),
                         encoding='latin-1')
    
    movie_ratings = pd.merge(movies, ratings)
    
    ratings.drop( "unix_timestamp", inplace = True, axis = 1 )
    movies.drop(movies.columns[[3,4]], inplace = True, axis = 1 )
    
    ratings_matrix = ratings.pivot_table(index=['movie_id'],columns=['user_id'],values='rating').reset_index(drop=True)
    ratings_matrix.fillna( 0, inplace = True )
    
    movie_similarity = 1 - pairwise_distances( ratings_matrix.as_matrix(), metric="cosine" )
    
    np.fill_diagonal( movie_similarity, 0)
    ratings_matrix = pd.DataFrame( movie_similarity )
    
    movie_names = np.loadtxt('python/movies1_name.txt', dtype='str', usecols=None, delimiter='\n') 
    writeFile = open('python/recom_movies.txt', 'w')
    writeFile.close()
    
    #print("movie rec2")
    
    for x in movie_names:
        writeFile = open('python/recom_movies.txt', 'a')
        try:
            user_inp = x
            # user_inp=input('Enter the reference movie title based on which recommendations are to be made: ')
            inp = movies[movies['title'] == user_inp].index.tolist()
            inp = inp[0]
        
            movies['similarity'] = ratings_matrix.iloc[inp]
            movies.columns = ['movie_id', 'title', 'release_date', 'similarity']
            
            temp = movies.sort_values(["similarity"], ascending=False)[1:5]
            
            
            for index, row in temp.iterrows():
                print(row['title'])
                writeFile.write(row['title']+'\n')
            
            
            print("Recommended movies based on your choice of ", user_inp, ": \n",
                  movies.sort_values(["similarity"], ascending=False)[1:5])
            
        
        except:
            writeFile.write(x+'\n')
            print(x)
            
    writeFile.close()
    
    #print("movie rec last")
    
except Exception as e:
    print(e)
