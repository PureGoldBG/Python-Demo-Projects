def words(file):
    f=open(file,"r")
    text=f.read()

    words=len(text.split())
    chars=len(text)

    f.close()

    print("Number of words: ",words," ;Number of symbols: ",chars)

words("test.txt")
