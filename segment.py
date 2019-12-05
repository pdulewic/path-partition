#!/usr/bin/env python

import vector as vec
from abc import ABCMeta, abstractmethod

class Segment:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self, ax): raise NotImplementedError
