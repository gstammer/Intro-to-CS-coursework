'''
@author: Georgie Stammer
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open("data/books.txt", "r")
    books = []
    ratings = {}
    for line in f:
        line = (line.strip()).split(",")
        name = line[0]
        ratings[name] = []
        for ind in range(1, len(line)):
            if ind % 2 == 1:
                if len(books) <= 54:
                    books.append(line[ind])
            else:
                ratings[name].append(int(line[ind]))
    return (books, ratings)
