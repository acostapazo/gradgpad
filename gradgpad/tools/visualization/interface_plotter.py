from abc import ABC, abstractmethod

from gradgpad.foundations.scores import Scores

import numpy as np


class IPlotter(ABC):
    def valid_labels(self, np_labels):
        if np.any(np_labels == None):  # noqa
            return False
        else:
            return True

    def __repr__(self):
        return self.__class__.__name__

    @abstractmethod
    def show(self, scores: Scores):
        raise NotImplementedError

    @abstractmethod
    def create_figure(self, scores: Scores):
        raise NotImplementedError

    @abstractmethod
    def save(self, output_filename: str, scores: Scores):
        raise NotImplementedError
