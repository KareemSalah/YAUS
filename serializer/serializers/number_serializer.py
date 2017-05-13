from .serializer_interface import serializer


class NumberSerializer(serializer):
    """This serializer provides a number as a counter for the next short url"""

    @staticmethod
    def __read():
        print("implemented")

    @staticmethod
    def __update():
        print("implemented")

    @staticmethod
    def get_new_serial():
        print("implemented")
