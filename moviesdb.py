from imdb import IMDb

ia = IMDb()

the_matrix = ia.search_movie('%mission: impossible - fallout%')
id_movie = the_matrix[0].movieID
title = the_matrix[0].movie_storyline
print(ia.get_movie(id_movie))



#print(ia.get_movie(id_movie))
#print(ia.get_movie(id_movie))
#print(ia.get_movie_infoset())
#get_movie_synopis release_dates video_clips
