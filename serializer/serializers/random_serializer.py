from django.db import transaction, connection
from yaus_main.globals import *
from serializer.models import RandomHashes
from random import randint


class RandomSerializerEngine():
	"""This serializer generates a random string of hash_length digits (lowers, uppers, digits)"""

	@staticmethod
	def generate_random_lowercase_char():
		return chr(ord('a') + randint(0, 25))


	@staticmethod
	def generate_random_uppercase_char():
		return chr(ord('A') + randint(0, 25))


	@staticmethod
	def generate_random_digit():
		return chr(ord('0') + randint(0, 9))


	@staticmethod
	def get_random_hash(hash_length):
		"""This function generates a random hash of hash_length consisting of (lowers, uppers, digits)"""

		generated_hash = ""
		for i in range(0, int(hash_length)):
			letter_type = randint(1, 3)
			next_char = ''

			if letter_type == 1:
				next_char = RandomSerializerEngine.generate_random_lowercase_char()
			elif letter_type == 2:
				next_char = RandomSerializerEngine.generate_random_uppercase_char()
			else:
				next_char = RandomSerializerEngine.generate_random_digit()

			generated_hash = generated_hash + next_char

		return generated_hash


	@staticmethod
	def get_new_serial():
		counter = 1

		# Counter is used to get out of a race condition
		while counter < 10:
			counter += 1

			url_hash = RandomSerializerEngine.get_random_hash(hash_length)
			if RandomHashes.objects.filter(url_hash=url_hash) is not None and RandomHashes.objects.filter(url_hash=url_hash).first() is not None:
				continue

			with transaction.atomic():
				similar_hashes = RandomHashes.objects.select_for_update(nowait=False).filter(url_hash__istartswith=url_hash[0])

				if similar_hashes is None or similar_hashes.first() is None:
					random_hash_row = RandomHashes(url_hash=url_hash)
					random_hash_row.save()
					return url_hash
				else:
					found = False
					print(similar_hashes)
					for similar_hash in similar_hashes:
						if url_hash == similar_hash.url_hash:
							found = True
							break

					if not found:
						random_hash_row = RandomHashes(url_hash=url_hash)
						random_hash_row.save()
						return url_hash

		return None
