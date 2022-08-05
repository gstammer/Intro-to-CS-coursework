'''
@author: Georgie Stammer
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
    correctavg = [('DivinityCafe', 4.0), ('TheCommons', 3.0),
                  ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
                  ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0),
                  ('TheSkillet', 0.0), ('PandaExpress', -0.2),
                  ('McDonalds', -0.3333333333333333)]
    if avg == correctavg:
        print("average works! :)")
    else:
        print("average does not work :(")

    slist = RecommenderEngine.similarities("Sung-Hoon",ratings)
    correctslist = [('Wei', 1), ('Sly one', -1), ('Melanie', -2),
                    ('Sarah Lee', -6), ('J J', -14), ('Harry', -24),
                    ('Nana Grace', -29)]
    if slist == correctslist:
        print("similarities works! :)")
    else:
        print("similarities does not work :(")

    r3 = RecommenderEngine.recommendations("Sarah Lee",items,ratings,3)
    correctr3 = [('Tandoor', 149.5), ('TheCommons', 128.0),
                 ('DivinityCafe', 123.33333333333333), ('FarmStead', 69.5),
                 ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0),
                 ('IlForno', 33.0), ('McDonalds', -69.5),
                 ('PandaExpress', -165.0)]
    if r3 == correctr3:
        print("recommendations works! :)")
    else:
        print("recommendations does not work :(")
        
        
        
if __name__ == '__main__':
    driver()