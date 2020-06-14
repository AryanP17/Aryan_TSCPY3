def exercise_132():
    L = ["the snake bit me\n", "the dog bit me\n", "the snake is scary\n", "I like dogs\n", "I hate snakes\n"]
    file1 = open('snake.txt', 'w')
    file1.writelines(L)
    file1 = open('snake.txt', 'r')
    for line in file1:
        if 'snake' in line:
            print(line)


exercise_132()