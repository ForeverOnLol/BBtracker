import dotenv
from telethon import TelegramClient

env_path = '.env'
dotenv.load_dotenv(env_path)

api_id = input('Введите API_ID с https://my.telegram.org/apps:').strip()
api_hash = input('Введите API_HASH с https://my.telegram.org/apps:').strip()

dotenv.set_key(env_path, 'API_ID', api_id)
dotenv.set_key(env_path, 'API_HASH', api_hash)

client = TelegramClient('anon', int(api_id), api_hash)
client.start()
client.disconnect()
