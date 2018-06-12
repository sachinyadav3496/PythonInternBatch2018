def hello():
    print("Hello world :")
    ch = input("type something")
    if ch:
        hello()

hello()
