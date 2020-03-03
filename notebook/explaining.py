import notebook

# object - note
object = "hello first"

#all attributes of class note
print(dir(notebook.Note))

#is now object the object of note?
print(isinstance(object, notebook.Note))

# create note, that is object of class Note
note = notebook.Note(object)
print(isinstance(note, notebook.Note))

# using an attribute of class Note
print(note.id)

# all attributes and methods of class Note
print(dir(note))

#method __init__
print(notebook.Note.__init__)

#method __str__
print(notebook.Note.__str__)

# class
print(notebook.Note)

#object of Note
print(note)