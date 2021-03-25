try:
    import readline as _readline  # lets us use the up and down arrows
except ImportError:
    import pyreadline as _readline
import abc
import shlex


class Playable(abc.ABC):
    @abc.abstractmethod
    def play(self):
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


class Player(BaseEntity, Playable):
    def __init__(self, start_room, cmd_map):
        BaseEntity.__init__(self, "NuKitty cat", start_room)
        self.cmd_map = cmd_map

    def play(self):
        while True:
            action = shlex.split(input(f"{self.name} is in {self.room.roomname} > "))
            action_func = self.cmd_map.get(action[0], None)
            if action_func:
                action_func(self, action)
            else:
                print("sorry, but i do not understand.")


class BaseItem(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def use(self, user):
        pass


# TODO: lock directions
class Room:
    def __init__(
        self,
        roomname="A Normal Room",
        description="Nothing special here, just a room",
        directionroom={},
        items=[],
    ):
        self.roommap = directionroom
        self.roomname = roomname
        self.roomdesc = description

    def getWalkRoom(self, direction):
        return self.roommap.get(direction, None)


class Game:
    def __init__(self, player):
        self.player = player

    def play(self):
        self.player.play()


# underscore b/c we dont use cmd
def act_nuke(player, _cmd):
    print("BOOM!")


# A handy way to exit the game
def exit_game(player, _cmd):
    raise EOFError


def main():
    # everything you run on startup is in here (unless its global init)
    start_room = Room()
    cmd_map = {"nuke": act_nuke, "exit": exit_game}
    player = Player(start_room, cmd_map)
    game = Game(player)
    try:
        game.play()
    except BaseException as e:
        print("\nBye!")


if __name__ == "__main__":
    main()
