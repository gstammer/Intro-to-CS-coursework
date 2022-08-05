'''
@author: Georgie Stammer
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    avgratings = []
    for ind in range(len(items)):
        rate = 0
        count = 0
        for person in ratings.keys():
            if ratings[person][ind] != 0:
                rate += ratings[person][ind]
                count += 1
        if count == 0:
            avg = 0.0
        else:
            avg = rate / count
        avgratings.append((items[ind], avg))
    avgratings = sorted(avgratings, key=lambda x: x[0])
    avgratings = sorted(avgratings, key=lambda x: x[1], reverse=True)
    return avgratings


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    simscores = []
    for person in ratings.keys():
        if person != name:
            dotproduct = 0
            for ind in range(len(ratings[name])):
                dotproduct += ratings[name][ind] * ratings[person][ind]
            simscores.append((person, dotproduct))
    simscores = sorted(simscores, key=lambda x: x[0])
    simscores = sorted(simscores, key=lambda x: x[1], reverse=True)
    return simscores


def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    simscores = similarities(name, ratings)
    newratings = {}
    count = 0
    for tup in simscores:
        if count < numUsers:
            person = tup[0]
            weight = tup[1]
            newratings[person] = [x * weight for x in ratings[person]]
            count += 1
    weightedavgs = averages(items, newratings)
    weightedavgs = sorted(weightedavgs, key=lambda x: x[0])
    weightedavgs = sorted(weightedavgs, key=lambda x: x[1], reverse=True)
    return weightedavgs


if __name__ == '__main__':
    items = ["a", "b"]
    name = "name1"
    ratings = {"name1": [2, 0], "name2": [4, 1], "name3": [-2, 5],
               "name4": [0, 0]}
    print(recommendations(name, items, ratings, 3))
    items = ['Tiger', 'Dog', 'Snake', 'Fireball']
    ratings = {'Liam': [0, 0, 0, 0], 'Man-Lin': [0, 0, 0, 0],
               'Jose': [0, 0, 0, 0]}
    print(averages(items, ratings))