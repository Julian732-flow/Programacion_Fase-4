class BaseModel:
    _id_counter = 1

    def __init__(self):
        self._id = BaseModel._id_counter
        BaseModel._id_counter += 1

    @property
    def id(self):
        return self._id