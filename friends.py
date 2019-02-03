users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0
    for friend in friendship:
        if user in friend:
            count+=1
    return count
num_friends(8)
       
def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    dictionary = dict()
    for user in users: 
        dictionary[str(user["name"])] = num_friends(user["id"])
    dictionary_sort = (sorted(dictionary.items(), key=lambda t: t[1], reverse=True))
    for name,friends in dictionary_sort:
        print(name,friends)
sort_by_num_friends()    
    
