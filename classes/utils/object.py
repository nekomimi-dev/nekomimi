import secrets
import string

class ObjectUtils():
	@classmethod
	def generateID() -> str:
		"""
		NyanやLetter、Poll用の10文字のIDを生成します
		"""
		characters = string.ascii_lowercase + string.digits
		random_string = ''.join(secrets.choice(characters) for _ in range(10))
		return random_string
