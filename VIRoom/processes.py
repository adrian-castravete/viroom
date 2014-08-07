#!/usr/bin/env python
# pylint: disable=missing-docstring


class Editor(Process):

    def __init__(self):
        super(Editor, self).__init__(name="VIRoom Editor")


class ErrorHandler(Process):

    def __init__(self):
        super(ErrorHandler, self).__init__(name="VIRoom Error Handler")

