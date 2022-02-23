
"""
#dict of {str : int}
name_to_rating = {'George Porgie': 87,
'Queen St. Cafe': 82,
'Dumplings R Us': 71,
'Mexican Grill': 85,
'Deep Fried Everything': 52}

#dict of {str : list of str}
price_to_name = {'$': ['Queen St. Cafe, Dumplings R Us, Deep Fried Everything'],
'$$': ['Mexican Grill'],
'$$$': ['Georgie Porgie'],
'$$$$': []}

#dict of {str : list of str}
cuisine_to_name = {'Canadian': ['Georgie Porgie'],
'Pub Food': ['Georgie Porgies', 'Deep Fried Everything'],
'Malaysia': ['Queen St. Cafe'],
'Thai': ['Queen St. Cafe'],
'Chinese': ['Dumplings R Us'],
'Mexican': ['Mexican Grill']}


With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we would
provide this list:
[[82, 'Queen St. Cafe'], ['71, 'Dumplings R Us']]
"""

def recommend(file, price, cuisines_list):
    """ file open for reading, str, list of str) -> lost of [int, str]

    Find restaurants that are priced according to the price and tagged with any
    of the items in cuisines_list. Return a list of lists of the form
    [ratings%, restaurant name], sorted by ratings.
    """

    #read the file and build the data structures
    '''OUTPUT: name_to_rating, price_to_names, cuisine_to_names'''
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)
    
    #price: look up the list of restaurant names for the requested price.
    names_in_pricerange = price_to_names[price]

    #now we have a list of restaurants in the right price range.
    #need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_in_pricerange, cuisine_to_names, cuisines_list)
    
    #now we have a list of restaurants that are in the right price range and serve
    #the requested cuisine.
    #need to look at ratings and sort the list
    menu = []

    for i in range(len(names_final)):
        n = names_final[i]
        menu.append([name_to_rating[n], n])
        menu.sort() 
        menu.reverse()
    return menu



def filter_by_cuisine(names_in_pricerange, cuisine_to_names, cuisines_list):
    ''' (list of str, dict of {str:list of str},  list of str) -> list of str

    names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    cuis = {'Canadian': ['Georgie Porgie'],
    'Pub Food': ['Georgie Porgies', 'Deep Fried Everything'],
    'Malaysia': ['Queen St. Cafe'],
    'Thai': ['Queen St. Cafe'],
    'Chinese': ['Dumplings R Us'],
    'Mexican': ['Mexican Grill']}
    cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisines(names, cuis, cuisines)
    '''
    filtered_list = []
    restaurants_by_cuisine = []

    for cuisine in cuisines_list:
        for i in range(len(cuisine_to_names[cuisine])):
            restaurants_by_cuisine.append(cuisine_to_names[cuisine][i])
            
    for name in names_in_pricerange:
        if name in restaurants_by_cuisine:
            filtered_list.append(name)
            
    return filtered_list

    
def read_restaurants(file):
    '''(file) -> (dict, dict, dict)
    Return a tuple of three dictionaries based on the information in the file.
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    '''
    name_to_rating = {}
    price_to_names = {'$':[], '$$':[], '$$$':[], '$$$$':[]}
    cuisine_to_names = {}
    sorted_list = file_list(file)
    for i in range(len(sorted_list)):
        name_to_rating[sorted_list[i][0]] = sorted_list[i][1]

        if '$' in sorted_list[i]:
            price_to_names['$'].append(sorted_list[i][0])
        if '$$' in sorted_list[i]:
            price_to_names['$$'].append(sorted_list[i][0])
        if '$$$' in sorted_list[i]:
            price_to_names['$$$'].append(sorted_list[i][0])
        if '$$$$' in sorted_list[i]:
            price_to_names['$$$$'].append(sorted_list[i][0])
            
        part = sorted_list[i][3].split(',')
        for j in range(0,len(part)):
            k = part[j]
            m = sorted_list[i][0]
            if k not in cuisine_to_names:
                cuisine_to_names[k] = [m]
            elif k in cuisine_to_names:
                cuisine_to_names[k].append(m)
            
    return (name_to_rating, price_to_names, cuisine_to_names)

def file_list(file):
    '''(file) -> list of list of str'''
    list1 = file.readlines()
    list2 = []
    for i in range(len(list1)):
        list1[i] = list1[i].rstrip('\n')   
    for i in range(0,len(list1), 5):
            minilist = [list1[i], list1[i+1], list1[i+2], list1[i+3]]
            minilist[1] = minilist[1].rstrip('%')
            list2.append(minilist)
    return list2
    



    
    


    
