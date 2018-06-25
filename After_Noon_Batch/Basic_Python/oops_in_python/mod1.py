def show():
    print("Hi I am a show function of mod1 file")
    print("File name = ",__name__)

#show()
#when we run this file __name__ will be __main__
#when we import this file __name__ will be filename for eg mod1

if __name__ == "__main__" :
    show()
