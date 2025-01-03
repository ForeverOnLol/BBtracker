import dotenv
from telethon import TelegramClient

env_path = '.env'
dotenv.load_dotenv(env_path)

api_id = input('Введите API_ID с https://my.telegram.org/apps:').strip()
api_hash = input('Введите API_HASH с https://my.telegram.org/apps:').strip()
target_phrase = input('Введите слово, повторения которого будет отслеживаться:').strip()


dotenv.set_key(env_path, 'API_ID', api_id)
dotenv.set_key(env_path, 'API_HASH', api_hash)
dotenv.set_key(env_path, 'TARGET_PHRASE', target_phrase)

client = TelegramClient('anon', int(api_id), api_hash)
client.start()
client.disconnect()
