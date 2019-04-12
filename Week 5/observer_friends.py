import abc

# The object that is being observed.
# ROLE: SUBJECT
class SocialMedia:
    """
    Holds a collection of objects that share an common interface.
    Send a notification to its observers when its state changes.
    """
    def __init__(self):
        self._observers = set()

    # Allows an object to register itself as an observer.
    def attach(self, observer):
        self._observers.add(observer)
        self._notify()

    # Allows an object to stop observing.
    def detach(self, observer):
        self._observers.discard(observer)
        self._notify()

    # Calls the interface defined method that all the observers share.
    def _notify(self):
        print("Updating all observers:")
        for observer in self._observers:
            observer.update(self.friendCount - 1)
        print()

    @property
    def friendCount(self):
        return len(self._observers)

# Interface or Abstract class that defines the method that the subject can call
# that all the observers will implement.
# ROLE: INTERFACE
class Observer(abc.ABC):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def update(self, arg):
        pass

# Inherits the Observer protocol.
# ROLE: OBSERVER
class Friend(Observer):
    """
    Implements the Observer interface.
    """
    def __init__(self, name):
        super().__init__(name)

    def update(self, arg):
        self._observer_state = arg
        print(self.name + " you now have " + str(arg) + " friends.")

# Testing code.
def main():
    socialMedia = SocialMedia()

    matthew = Friend("Matthew")
    shekhar = Friend("Shekhar")
    rodney = Friend("Rodney")

    socialMedia.attach(matthew)
    socialMedia.attach(shekhar)
    socialMedia.attach(rodney)

    socialMedia.detach(shekhar)
    socialMedia.detach(rodney)

if __name__ == "__main__":
    main()
