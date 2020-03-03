from menu import Menu

from notebook import Note, Notebook

lst = [Note, Notebook, Menu]

for i in lst:
    print("{}:".format(i))
    if i == Note:
        object = "hello first"
        print("     # all attributes of class {}:".format(i))
        print("             dir({})".format(i))
        print("     " + str(dir(i)))
        print("     # is now object the object of {}?".format(i))
        print("             isinstance(object, {}))".format(i))
        print("     " + str(isinstance(object, i)))
        print("     # create note, that is object of class {}".format(i))
        print("             note = {}(object); isinstance(note, {}))".format(i,
                                                                             i))
        note = i(object)
        print("     " + str(isinstance(note, i)))
        print("     # all attributes and methods of class {}".format(i))
        print("             dir({}))".format(i))
        print("     " + str(dir(i)))
        print("     # method __init__")
        print("             {}.__init__".format(i))
        print("     " + str(i.__init__))
        print("     #method __str__")
        print("             {}.__str__".format(i))
        print("     " + str(i.__str__))
        print("     # class")
        print("     " + str(i))
        print("\n\n\n")

    print("     # all attributes of class {}:".format(i))
    print("             dir({})".format(i))
    print("     " + str(dir(i)))
    print("     # create note, that is object of class {}".format(i))
    print("             note = {}(); isinstance(note, {}))".format(i, i))
    print("     # all attributes and methods of class {}".format(i))
    print("             dir({}))".format(i))
    print("     " + str(dir(i)))
    print("     # method __init__")
    print("             {}.__init__".format(i))
    print("     " + str(i.__init__))
    print("     #method __str__")
    print("             {}.__str__".format(i))
    print("     " + str(i.__str__))
    print("     # class")
    print("     " + str(i))
    print("\n\n\n")
