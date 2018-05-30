data_file = 'score.txt'


def load_scores():
    global name

    with open(data_file, 'r') as f:
        lines = f.read().splitlines()

    name = input

    return name
                
    with open(data_file, 'r') as f:
        lines = f.read().splitlines()

    

    scores = []
    for line in lines:
        name, points = line.split(" ")
        scores.append((name, int(points)))


    scores.sort(key=lambda x: x[1], reverse=True)

    return scores

def display_scores(scores):
    for s in scores:
        print(s)

def add_new_score(scores, name, points):
    new = [name, points]
    scores.append(new)
    scores.sort(key=lambda x: x[1], reverse=True)


    
scores = load_scores()
display_scores(scores)
add_new_score(scores, "Jon", 63)
display_scores(scores)
    
