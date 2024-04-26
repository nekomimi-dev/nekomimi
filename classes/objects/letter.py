from datetime import datetime, timezone
from ..utils import ObjectUtils
from . import Poll
from . import Nyan

class Letter():
	"""
	このクラスは、nekomimiで「おてがみ」と言われるオブジェクトを管理しています。
	他のSNSでいう「ツイート」「ポスト」「ノート」「トゥート」です。
	"""
	def __init__(
		self,
		id:str = ObjectUtils.generateID(),
		nyan:Nyan = None,
		content:str = "",
		create:datetime = datetime.now(),
		reactions:list = [],
		poll:Poll = None,
		is_hidden:bool = False,
		attachments:list = [],
	):
		"""
		Letterを初期化します。
		"""
		self.id = id
		self.content = content
		self.create = create
		self.reactions = reactions
		self.poll = poll
		self.is_hidden = is_hidden
		self.attachments = attachments
