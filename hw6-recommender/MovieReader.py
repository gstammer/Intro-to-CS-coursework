'''
@author: Georgie Stammer
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open("data/movies.txt", "r")
    data = []
    movies = []
    ratings = {}
    for line in f:
        line = (line.strip()).split(",")
        name = line[0]
        movie = line[1]
        rate = int(line[2])
        data.append([name, movie, rate])
    data = sorted(data, key=lambda x: x[1])
    for item in data:
        if item[0] not in ratings:
            ratings[item[0]] = []
        if item[1] not in movies:
            movies.append(item[1])
    for name in ratings.keys():
        for movie in movies:
            ratings[name].append(0)
    for item in data:
        name = item[0]
        movie = item[1]
        rate = int(item[2])
        ind = movies.index(movie)
        ratings[name][ind] = rate
    f.close()
    return (movies, ratings)
