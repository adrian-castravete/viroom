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

    def run(self):
        print self.name, 'Started'

        print self.name, 'Stopped'


def main():
    viroom = VIRoom()
    viroom.start()

