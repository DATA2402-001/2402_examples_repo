score = [
    {'name': 'alice', 'score': 5},
    {'name': 'bob', 'score': 3},
    {'name': 'cindy', 'score': 4},
]

# to sort these dictionaries, use the optional "key" parameter
# pass in some function that will return the score from the dict

def get_score_from_dict(a_dict):
    return a_dict['score']
score.sort(key=get_score_from_dict)

# or use a lambda function
score.sort(key= lambda a_dict : a_dict['score'])

print(score)