def producerColor():
    with open("todaysTemMax.txt", "r+") as file:
        content = file.readline().splitlines()
        for i in content:
            i = int(i)
            if i < 15:
                return 'blue'
            elif i > 15:
                return 'yellow'