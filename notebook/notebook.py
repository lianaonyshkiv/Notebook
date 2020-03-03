import datetime

last_id = 0

class Note:
    """ Represent a note in the notebook. Match against a
    string in searches and store tags for eah note. """

    def __init__(self, memo, tags=""):
        """ Initialize a note with memo and optional space-seperated
        tags. Automatically set the note`s creation date a unique id.
        >>> n1 = Note("hello first")
        >>> n2 = Note("hello again")
        >>> n1.id
        1
        >>> n2.id
        2
        """
        self.memo = memo
        self.tags = tags
        self.creation_data = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """ Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.
        >>> n1 = Note("hello first")
        >>> n2 = Note("hello again")
        >>> n1.match('hello')
        True
        >>> n2.match('second')
        False
        """
        return filter in self.memo or filter in self.tags

class Notebook:
    ''' Represent a collection of notes that can be tagged,
    modified, and searched. '''

    def __init__(self):
        ''' Initialize a notebook with an empty list.
        >>> n = Notebook()
        >>> n.new_note("hello world")
        >>> n.new_note("hello again")
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        ''' Create a new note and add it to the list.
        >>> n = Notebook()
        >>> n.new_note("hello world")
        >>> n.new_note("hello again")
        >>> n.notes[0].id
        1
        >>> n.notes[1].id
        2
        '''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        ''' Find the note with the given id and change its
        memo to the given value. '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        ''' Find all notes that match the given filter
        string. '''
        return [note for note in self.notes if note.match(filter)]
