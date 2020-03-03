from notebook import Note, Notebook
from menu import Menu

lst = [Note, Notebook, Menu]

for i in lst:
    print("{}:".format(i))
    if i == Note:
        object = "hello first"
    if i == Notebook:
        object = None
    if i == Menu:
        object = None
    print("     # all attributes of class note:")
    print("     "+str(dir(Note)))
    print("     # is now object the object of note?")
    print("     "+str(isinstance(object, Note)))
    print("     # create note, that is object of class Note")
    note = Note(object)
    print("     "+str(isinstance(note, Note)))
    print("     # using an attribute of class Note")
    print("     "+str(note.id))
    print("     # all attributes and methods of class Note")
    print("     "+str(dir(note)))
    print("     # method __init__")
    print("     "+str(Note.__init__))
    print("     #method __str__")
    print("     "+str(Note.__str__))
    print("     # class")
    print("     "+str(Note))
    print("\n\n\n")

