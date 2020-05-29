from threading import Thread


class StoppableThread(Thread):
    def __init__(self):
        super().__init__()
        self.exit_thread = False
        self.pause_thread = False

    def stop(self):
        """ Stop thread.
        """
        self.exit_thread = True

    def pause(self):
        """ Pause thread.
        """
        self.pause_thread = True

    def unpause(self):
        """ Unpause thread.
        """
        self.pause_thread = False