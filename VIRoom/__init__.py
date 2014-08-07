#!/usr/bin/env python


from __future__ import absolute_import

from multiprocessing import Process


class VIRoom(Process):

    @staticmethod
    def main():
        viroom = VIRoom()
        viroom.start()

    def __init__(self):
        super(VIRoom, self).__init__(name="VIRoom Main")

    def run(self):
        print self.name, 'Started'

        print self.name, 'Stopped'


def main():
    VIRoom.main()

