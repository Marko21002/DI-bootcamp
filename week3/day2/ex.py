class Door:
    def __init__(self, is_opened) -> None:
        self.opened = is_opened

    def open(self):
        if self.open == 'open':
            print('door is open')
        else:
            print('door is closed')


class BlockedDoor(Door):
    def __init__(self, is_opened) -> None:
        super().__init__(is_opened)
        self.opened = 'blocked'


door = Door('open')
door.open()
door2 = BlockedDoor('blocked')
door2.open()
