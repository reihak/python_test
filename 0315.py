import sys

"""if __name__ == '__main__':
    arg = sys.argv
    print(arg)

    first = arg[0]
    second = arg[1]
    print("first: {}, second: {}".format(first, second))
    third = arg[2]
    print(int(second) + int(third))
"""

class CLI:

    """
    ----------------------
    CLI:使い方
    python3 0315.py command arg1, arg2, ......
    -----------------------
    """
    def __init__(self,argv):
        self.argv = argv
        self.function = {
        "help":self.usage,
        "cat":self.cat,
        }
        #print(self.argv)
    def parse(self):
        if not self.argv:
            self.usage()
        else:
            func = self.function.get(self,arvg[0])
            if func is not None:
                if "-h" in self.argv:
                    print("show help message")
                    print(func.__doc__)
                else:
                    try:
                        func()
                    except:
                        print(func.__doc__)
            else:
                print("command: {} is unfined.".format(self.argc[0]))
                print(self.__doc__)
    def cat(self):
        """
        python3 app.py cat filename
        show file
        """
        with open(self.argv[1],"r")as f:
            data = f.readlines()
            for line in data:
                print(line)
    def usage(self):
        print(self.__doc__)

if __name__ == '__main__':
    cli = CLI(sys.argv[1:]).usage()
