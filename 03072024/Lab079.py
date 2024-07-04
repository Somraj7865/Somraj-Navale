# Abstraction
from abc import ABC, abstractmethod


class pyatmb(ABC):

    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class shubham(pyatmb):
    def payfee(self):
        print("paid")


shu = shubham()
shu.payfee()
shu.enrolled()
