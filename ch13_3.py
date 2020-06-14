def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    count = 0
    while True:
        count += 1
        text = infile.readline()
        if len(text) == 0:
            break

        # Put any more processing logic here
        outfile.write(str(count))
        outfile.write(text)

    infile.close()
    outfile.close()


filter("mirror.py", "12 by 12.py")