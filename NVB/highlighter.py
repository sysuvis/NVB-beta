import numpy as np
from NVB.consts import styles
from NVB.dnt import Type
from NVB.views.view import View


class HighLighter:
    def __init__(self, style=None, value=None, type=Type.Vector):
        self.style = styles[style] if style is not None else None
        self.value = []
        self.views = []
        self.mappings = []
        self.type = type
        if value is None:
            if type == Type.Scalar:
                self.value = 0
        else:
            self.update(value)

    def update(self, value):
        if self.type == Type.Scalar:
            self.value = value
        else:
            if isinstance(value, np.ndarray):
                value = value.tolist()
            if isinstance(value, list):
                self.value = value
            else:
                if value in self.value:
                    self.value.remove(value)
                else:
                    self.value.append(value)
        for view in self.views:
            if view.idx not in View.highlight_list:
                View.highlight_list.append(view.idx)
        for f in self.mappings:
            if self.type == Type.Scalar:
                f(self.value)
            else:
                f(self.value.copy())

    def add_mapping(self, f):
        self.mappings.append(f)

    def set_style(self, s):
        self.style = s

    def core(self):
        return self.style


# need to be generalized
# (Multi)HighLighter should carry other info in r.
class MultiHighLighter:
    def __init__(self, style, value=None, type=Type.Scalar, n=3):
        self.style = styles[style] if style is not None else None
        self.type = type
        if type == Type.Scalar:
            self.value = [-1, -1]
        elif type == Type.Vector:
            self.value = [[], [], [], []]
        else:
            self.value = [None, None]
        self.n = n
        self.intersect = []
        self.views = []
        self.mappings = []
        if value is not None:
            self.update(value)

    def update(self, value, idx=None):
        if idx is not None:
            self.value[idx] = value
        else:
            self.value = value
            # if len(value) == 3:
            #     self.value = value + []
            # else:
            #     self.value = value
        for view in self.views:
            if view.idx not in View.highlight_list:
                View.highlight_list.append(view.idx)
        for f in self.mappings:
            f(self.value.copy())

    def core(self):
        return self.style
