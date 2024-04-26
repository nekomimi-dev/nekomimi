from datetime import datetime, timezone
from . import Letter
from ..utils import ObjectUtils

class Poll():
	"""
	このクラスは、nekomimiで「しつもん」と言われるオブジェクトを管理しています。
	他のSNSでいう「投票」です。
	"""
	def __init__(
		self,
		letter:Letter,
		choices:list = [],
		during:datetime = None,
		is_multiple:bool = False,
	):
		self.letter = letter
		self.choices = choices
		self.during = during
		self.is_multiple = is_multiple
