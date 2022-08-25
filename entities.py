class Entities:
    def __init__(self):
        self._persons = []
        self._groups = []
        self._locations = []
        self._events = []
        self._time_references = []

    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, person):
        self._persons.append(person)


    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, group):
        self._groups.append(group)

    
    @property
    def locations(self):
        return self._locations

    @locations.setter
    def locations(self, location):
        self._locations.append(location)


    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, event):
        self._events.append(event)


    @property
    def time_references(self):
        return self._time_references

    @time_references.setter
    def time_references(self, time_reference):
        self._time_references.append(time_reference)   