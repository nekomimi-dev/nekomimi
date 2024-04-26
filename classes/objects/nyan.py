from datetime import datetime, timezone
from ..utils import ObjectUtils

class Nyan():
	"""
	このクラスは、nekomimiで「ねこ」と言われるオブジェクトを管理しています。
	他のSNSでいう「ユーザー」です。
	"""
	def __init__(
		self,
		id:str = ObjectUtils.generateID(),
		screen_name:str = "",
		icon:str = "",
		header_picture:str = "",
		bio:str = "",
		create:datetime = None,
		location:str = "",
		birthday:datetime = None,
		additional = [],
	):
		self.id = id
		self.screen_name = screen_name
		self.icon = icon
		self.header_picture = header_picture
		self.bio = bio
		self.create = create
		self.location = location
		self.birthday = birthday
		self.additional = additional
