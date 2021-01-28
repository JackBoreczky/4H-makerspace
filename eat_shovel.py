import abc
import shlex

class Interactible(abc.ABC):
    @abc.abstractmethod
    def interact(self, args):
        pass

class BaseEntity(abc.ABC):
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def use(self, itemname):
        maching = [item for item in self.items if item.name == itemname]
        if len(maching) == 1:
            maching[0].use(self)

class BaseItem(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def use(self, user):
        pass

class Room():
    def __init__(self, directionroom = {}):
        self.roommap = directionroom

    def getWalkRoom(self, direction):
        return self.roommap.get(direction, None)