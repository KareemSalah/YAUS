# TODO: this file will implemented later, to create an interface for other ways of implementing the read/update operations


class serializer():
    """Serializer class provides a mechanism to retrieve a serial and update it"""

    @staticmethod
    def read(self):
        """Please notice that this will be run concurrently in a multi-threaded or perhaps a distributed system"""
        raise RuntimeError("Not implemented")

    @staticmethod
    def update(self):
        """Please notice that this will be run concurrently in a multi-threaded or perhaps a distributed system"""
        raise RuntimeError("Not implemented")
