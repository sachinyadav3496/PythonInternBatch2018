def dec_baap(*tags):
    def dec(old):
        def work(s):
            for tag in tags :
                s = '\t\n<{0}>{1}</{0}\n>'.format(tag,s)
            f = open('code.html','w')
            f.write(s)
            f.close()
        return work
    return dec

tags = input("Enter tags by space separted ").split()
@dec_baap(*tags)
def old(s):
    pass

old(input("Enter you code : \n\n"))
