# マイグレーション(仮、未完成)

import asyncio
import asyncpg
import os

if os.path.isfile("../.env"):
	from dotenv import load_dotenv
	load_dotenv("../.env")

async def create_table():
	# データベースに接続
	connection = await asyncpg.connect(os.getenv("database_url"))

	try:
		# テーブルを作成
		await connection.execute('''
			CREATE TABLE IF NOT EXISTS user (
				id SERIAL PRIMARY KEY,
				name TEXT,
				age INT
			)
		''')
		print("テーブルが作成されました")
	finally:
		# 接続を閉じる
		await connection.close()

# イベントループを実行してテーブルを作成
asyncio.run(create_table())
