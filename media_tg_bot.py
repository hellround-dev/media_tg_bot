import logging
import os
import asyncio
import time
from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv("TOKEN")
DOWNLOAD_DIR = "/Users/hellround/Desktop/Media"

dp = Dispatcher()
bot: Bot = None
count = 0

process_status = {
    "chat_id": None,
    "msg_id": None,
    "last_file_time": 0.0,
    "is_running": False,
    "timeout_task": None
}

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

lock = asyncio.Lock()


async def wait_for_batch_end():
    await asyncio.sleep(4.0)

    global count
    print(f"\n Перенос фоток завершен!😇\n✅ Успешно сохранено : {count} файлов.")

    async with lock:
        if process_status["chat_id"] and process_status["msg_id"]:
            try:
                await bot.edit_message_text(
                    chat_id=process_status["chat_id"],
                    message_id=process_status["msg_id"],
                    text=f"Перенос фоток завершен!😇\n✅ Успешно сохранено : {count} файлов."
                )
            except Exception as e:
                print(f"Ошибка отправки финала: {e}")

        process_status["msg_id"] = None
        process_status["is_running"] = False
        count = 0



async def handle_progress(message: types.Message):
    global count
    current_time = time.time()
    process_status["chat_id"] = message.chat.id

    async with lock:
        if not process_status["is_running"] or process_status["msg_id"] is None:
            process_status["is_running"] = True
            msg = await message.answer(f"Нашел много крутых фоток 😄\n📂 Перенесено: {count}")
            process_status["msg_id"] = msg.message_id
            process_status["last_file_time"] = current_time

            if process_status["timeout_task"] and not process_status["timeout_task"].done():
                process_status["timeout_task"].cancel()
            process_status["timeout_task"] = asyncio.create_task(wait_for_batch_end())
            return

    if current_time - process_status["last_file_time"] > 4.0:
        try:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=process_status["msg_id"],
                text=f"Перенос фото, нужно чуть-чуть подождать 😇\n📂 Уже успешно скопировано: {count} файлов"
            )
            process_status["last_file_time"] = current_time
        except Exception:
            pass

    async with lock:
        if process_status["timeout_task"] and not process_status["timeout_task"].done():
            process_status["timeout_task"].cancel()
        process_status["timeout_task"] = asyncio.create_task(wait_for_batch_end())


@dp.message(F.photo)
async def photo_handler(message: types.Message):
    global count
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)

    unique_suffix = time.time_ns()
    file_name = f"photo_{unique_suffix}_{photo.file_id[:8]}.jpg"
    destination = os.path.join(DOWNLOAD_DIR, file_name)

    await bot.download_file(file_info.file_path, destination)
    count += 1

    print(f"Перенеслось {count} файла(ов)")
    await handle_progress(message)


@dp.message(F.video)
async def video_handler(message: types.Message):
    global count
    video = message.video
    file_info = await bot.get_file(video.file_id)

    unique_suffix = time.time_ns()
    original_name = video.file_name if video.file_name else f"video_{video.file_id[:8]}.mp4"
    file_name = f"{unique_suffix}_{original_name}"
    destination = os.path.join(DOWNLOAD_DIR, file_name)

    await bot.download_file(file_info.file_path, destination)
    count += 1

    print(f"Перенеслось {count} файла(ов)")
    await handle_progress(message)


@dp.message(F.document)
async def document_handler(message: types.Message):
    global count
    document = message.document
    if document.mime_type.startswith(('image/', 'video/')):
        file_info = await bot.get_file(document.file_id)

        unique_suffix = time.time_ns()
        file_name = f"{unique_suffix}_{document.file_name}"
        destination = os.path.join(DOWNLOAD_DIR, file_name)

        await bot.download_file(file_info.file_path, destination)
        count += 1

        print(f"Перенеслось {count} файла(ов)")
        await handle_progress(message)


async def main():
    global bot
    print("Инициализация сети...")
    bot = Bot(token=TOKEN)
    print("Бот запущен и готов устанавливать файлы")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
