numbers = [3, 1, 6, 4, 3, 8, 1, 1, 1, 2]
uniques = []

def countCounter(arrayofNum):
    arrayofNum = sorted(arrayofNum)
    uniques = []
    for number in arrayofNum:
        if number not in uniques:
            uniques.append(number)

    uniques = sorted(uniques)

    counts = []

    for unique in uniques:
        count = 0
        for number in arrayofNum:
            if number == unique:
                count += 1
        counts.append(count)
    #print(uniques)
    #print(counts)

    print(dict(zip(uniques, counts))) #this pairs the uniques and counts as a dictionary. Remember to tell zip what type of object you want zip to be


countCounter (numbers)

