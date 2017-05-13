from django.db import transaction
from serializer.models import NumberSerializer


class NumberSerializer():
    """This serializer provides a number as a counter for the next short url"""

    @staticmethod
    def get_new_serial():
        """This function retrieves the counter, saves a copy of it, increment it, then return it, all atomic"""
        serial = 0

        # Notice that I use select_for_update() inside transaction to make sure that no one else can read the counter
        with transaction.atomic():
            serial_row = NumberSerializer.objects.select_for_update(nowait=False).filter(pk=1).first()
            serial = serial_row.url_num
            serial_row.url_num = serial_row.url_num+1
            serial_row.save()

        return serial