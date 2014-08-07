#!/usr/bin/env python
# pylint: disable=missing-docstring


"""Main Module

The main module of the editor. This is where the various processes are started.

"""


from __future__ import absolute_import

from multiprocessing import Process


class VIRoom(Process):

    """Main Process"""

    def __init__(self):
        super(VIRoom, self).__init__(name="VIRoom Main")

        self._running = False
        self._processes = []

    def run(self):
        print self.name, 'Started'

        self._start_editor_process()

        self._running = True
        while self._running:
            if len(self._processes) == 0:
                self._running = False

        print self.name, 'Stopped'

    def _start_editor_process(self):
        process = Editor()
        process.start()

        self._processes.append(process)


def main():
    viroom = VIRoom()
    viroom.start()

