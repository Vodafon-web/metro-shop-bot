import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Берём токен из переменных окружения Railway для безопасности
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_keyboard():
    kb = [
        [InlineKeyboardButton(text="🪖 Сеты и Броня 6 ур.", callback_data="armor")],
        [InlineKeyboardButton(text="🔫 Оружие (Вышка / СФ)", callback_data="weapons")],
        [InlineKeyboardButton(text="🗺️ Сопровождение 7-8 карты", callback_data="boost")],
        [InlineKeyboardButton(text="💬 Написать оператору", url="https://t.me/ТВОЙ_ТЕЛЕГРАМ_НИК")] # Поменяй на свой юзернейм
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 **Добро пожаловать в Metro Shop PUBG Mobile!**\n\n"
        "Выбери нужный раздел ниже:",
        reply_markup=main_keyboard(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "armor")
async def show_armor(callback: types.CallbackQuery):
    text = (
        "🪖 **Доступная броня и сеты:**\n\n"
        "• Фулл 6 сет (обычный) — в наличии\n"
        "• Фулл 6 сет Стальной Фронт — в наличии\n"
        "• Фулл 6 сет Кобра — в наличии\n\n"
        "Для заказа нажмите кнопку связи с оператором."
    )
    await callback.message.edit_text(text, reply_markup=main_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "weapons")
async def show_weapons(callback: types.CallbackQuery):
    text = (
        "🔫 **Оружие и модификации:**\n\n"
        "• МК14 Вышка / СФ / КБ\n"
        "• Заряженные пушки и обвесы\n\n"
        "Для заказа напишите оператору."
    )
    await callback.message.edit_text(text, reply_markup=main_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "boost")
async def show_boost(callback: types.CallbackQuery):
    text = (
        "🗺️ **Сопровождение / Буст:**\n\n"
        "• Вынос лута на 7/8 карте\n"
        "• Гарантированный фарм и помощь с квестами\n"
    )
    await callback.message.edit_text(text, reply_markup=main_keyboard(), parse_mode="Markdown")
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот успешного запущен на Railway!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
