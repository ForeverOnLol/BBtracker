import asyncio
import sys
import threading
from telethon import TelegramClient, events
import config
from ui import Application
from structures import Storage

is_all_active_threads = {'value': True}


async def wait_until_disconnect(client):
    while is_all_active_threads['value']:
        await asyncio.sleep(1)
    print('Дисконект сессии')
    client.disconnect()

def run_tg_thread(storage: Storage):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    client = TelegramClient('anon.session', config.api_id, config.api_hash)

    @client.on(events.NewMessage(pattern=config.target_phrase))
    async def send_handler(event):
        storage.update()

    client.start()
    try:
        tasks = [
            loop.create_task(wait_until_disconnect(client=client)),
            loop.create_task(client.run_until_disconnected()),
        ]

        loop.run_until_complete(asyncio.wait(tasks))
    except (RuntimeError, TypeError):
        pass


def run_ui_thread(storage: Storage):
    window = Application(storage)
    window.mainloop()
    is_all_active_threads['value'] = False


if __name__ == '__main__':
    storage = Storage()

    ui_thread = threading.Thread(target=run_ui_thread, args=(storage,), daemon=True)
    ui_thread.start()
    scrapper_thread = threading.Thread(target=run_tg_thread, args=(storage,))
    scrapper_thread.start()

    ui_thread.join()
    scrapper_thread.join()
    sys.exit()
