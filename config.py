import dotenv
import os


dotenv.load_dotenv()
# Use your own values from my.telegram.org
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
target_phrase = os.environ.get('TARGET_PHRASE')