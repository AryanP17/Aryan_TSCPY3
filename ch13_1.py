def exercise_131():
    with open('text.txt', 'w') as f:
        f.write('hiiiiii\n')
        f.write('hello therererererere\n')
        f.write('hi')

    with open('exercise131.txt', 'w') as f:
        for line in reversed(list(open('text.txt'))):
            print(list(open("text.txt")))
            # f.write(line.rstrip())
            f.write(line)
            # f.write('\n')


exercise_131()
