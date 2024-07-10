import dotenv
import os


dotenv.load_dotenv()
# Use your own values from my.telegram.org
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
chat_name = os.environ.get('CHAT_NAME')