import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

MANAGER_LINK = "https://t.me/managerVODAFON"

# Головне меню з кнопками
def main_keyboard():
    kb = [
        [InlineKeyboardButton(text="📱 Супроводи (7 і 9 картки)", callback_data="category_boost")],
        [InlineKeyboardButton(text="🪖 Броня та Шолом 6 ур.", callback_data="category_armor")],
        [InlineKeyboardButton(text="🔫 Зброя та Обвеси", callback_data="category_weapons")],
        [InlineKeyboardButton(text="🔥 Аксесуари", callback_data="category_accs")],
        [InlineKeyboardButton(text="💳 Буст балансу (Млн)", callback_data="category_balance")],
        [InlineKeyboardButton(text="🗡️ Мечі, Ножі, Керамбіт", callback_data="category_knives")],
        [InlineKeyboardButton(text="💬 Написати менеджеру", url=MANAGER_LINK)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

# Кнопка "Назад"
def back_keyboard():
    kb = [
        [InlineKeyboardButton(text="⬅️ Назад у меню", callback_data="main_menu")],
        [InlineKeyboardButton(text="✍️ Замовити в менеджера", url=MANAGER_LINK)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

# Команда /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 **Вітаємо у Metro Shop PUBG Mobile!**\n\n"
        "Оберіть потрібний розділ із прайсом нижче за допомогою кнопок або **напишіть своє запитання в чат** — наш консультант допоможе вам!\n\n"
        "⚠️ *При оплаті комісія за ваш рахунок, щоб сума була повною!*",
        reply_markup=main_keyboard(),
        parse_mode="Markdown"
    )

# Повернення в головне меню
@dp.callback_query(F.data == "main_menu")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "👋 **Головне меню Metro Shop**\n\n"
        "Оберіть категорію товарів:",
        reply_markup=main_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

# 1. Супроводи
@dp.callback_query(F.data == "category_boost")
async def show_boost(callback: types.CallbackQuery):
    text = (
        "📱 **СУПРОВОДИ METRO ROYALE**\n\n"
        "🔹 **7 карта** ➖ 70 грн💸\n"
        "└ *(9 млн радіка + від 2 Ф6+)*\n\n"
        "👑 **VIP 7 карта** ➖ 110 грн💸\n"
        "└ *(10 млн радіка + від 3 Ф6+)*\n\n"
        "👑 **VIP 9 карта** ➖ 115 грн💸\n"
        "└ *(12 млн радіка + 4-6 білетів + від 3 Ф6+)*\n\n"
        "🏆 **GOLD 7 карта** ➖ 125 грн💸\n"
        "└ *(15 млн радіка + від 4 Ф6+)*\n\n"
        "🏆 **GOLD 9 карта** ➖ 200 грн💸\n"
        "└ *(18 млн радіка + 8-12 білетів + від 5 Ф6+)*\n\n"
        "⚠️ *Комісія при оплаті за ваш рахунок!*"
    )
    await callback.message.edit_text(text, reply_markup=back_keyboard(), parse_mode="Markdown")
    await callback.answer()

# 2. Броня та Шоломи
@dp.callback_query(F.data == "category_armor")
async def show_armor(callback: types.CallbackQuery):
    text = (
        "🛍️ **РЕЧІ (БРОНЯ ТА ШОЛОМИ)**\n\n"
        "🪖 **Шоломи:**\n"
        "• 6 шлем ➖ 7 грн💸\n"
        "• 6 шлем КБ ➖ 8 грн💸\n"
        "• 6 шлем СФ ➖ 8 грн💸\n\n"
        "🧥 **Броня:**\n"
        "• 6 броня ➖ 8 грн💸\n"
        "• 6 броня КБ ➖ 9 грн💸\n"
        "• 6 броня СФ ➖ 9 грн💸\n\n"
        "🎒 **Рюкзак:**\n"
        "• 6 рюкзак ➖ 9 грн💸\n\n"
        "⚠️ *Комісія при оплаті за ваш рахунок!*"
    )
    await callback.message.edit_text(text, reply_markup=back_keyboard(), parse_mode="Markdown")
    await callback.answer()

# 3. Зброя
@dp.callback_query(F.data == "category_weapons")
async def show_weapons(callback: types.CallbackQuery):
    text = (
        "🔫 **ЗБРОЯ**\n\n"
        "• МК14 (покращена) ➖ 9 грн💸\n"
        "• МК14 (вишка) ➖ 15 грн💸\n"
        "• MG3 (вишка) ➖ 12 грн💸\n"
        "• JS9 (вишка) ➖ 13 грн💸\n\n"
        "‼️ **ЗА КОЖЕН ОБВЕС +1 грн💸**\n\n"
        "⚠️ *Комісія при оплаті за ваш рахунок!*"
    )
    await callback.message.edit_text(text, reply_markup=back_keyboard(), parse_mode="Markdown")
    await callback.answer()

# 4. Аксесуари
@dp.callback_query(F.data == "category_accs")
async def show_accs(callback: types.CallbackQuery):
    text = (
        "🔥 **АКСЕСУАРИ**\n\n"
        "👀 Тепловізор ➖ 5 грн💸\n"
        "☢️ Пластина ➖ 6 грн💸\n"
        "🎗️ Ремінь ➖ 2 грн💸\n"
        "👝 Подсумок ➖ 3 грн💸\n\n"
        "⚠️ *Комісія при оплаті за ваш рахунок!*"
    )
    await callback.message.edit_text(text, reply_markup=back_keyboard(), parse_mode="Markdown")
    await callback.answer()

# 5. Буст балансу
@dp.callback_query(F.data == "category_balance")
async def show_balance(callback: types.CallbackQuery):
    text = (
        "💳 **БУСТ БАЛАНСУ**\n\n"
        "💰 5 млн ➖ 10 грн🇺🇦\n"
        "💰 10 млн ➖ 30 грн🇺🇦\n"
        "💰 20 млн ➖ 110 грн🇺🇦\n"
        "💰 30 млн ➖ 150 грн🇺🇦\n"
        "💰 50 млн ➖ 300 грн🇺🇦\n\n"
        "‼️ *Більше не робимо, але якщо замовите — буде трохи дорожче.*\n"
        "⚠️ *Комісія при оплаті за ваш рахунок!*"
    )
    await callback.message.edit_text(text, reply_markup=back_keyboard(), parse_mode="Markdown")
    await callback.answer()

# 6. Ножі та Мечі
@dp.callback_query(F.data == "category_knives")
async def show_knives(callback: types.CallbackQuery):
    text = (
        "🗡️ **РІДКІСНА ЗБРОЯ / НОЖІ**\n"
        "*(Усі ножі/мечі залишаються у вас назавжди‼️)*\n\n"
        "‼️ **КЕРАМБІТ** ➖ 3100 ₴\n\n"
        "🗡️ **МЕЧ** ➖ 4200 грн 💲\n\n"
        "🏬 **НІЖ-МЕТЕЛЕК (Балісонг):**\n"
        "• Недоторканий (можна подарувати) ➖ 3100 грн *(НЕМАЄ В НАЯВНОСТІ)*\n"
        "• Оригінал (без напису) ➖ 650 грн\n"
        "• Дублікат (з напису «Получено от друга») ➖ 450 грн\n\n"
        "⚠️ *Комісія при оплаті за ваш рахунок!*"
    )
    await callback.message.edit_text(text, reply_markup=back_keyboard(), parse_mode="Markdown")
    await callback.answer()

# Розумний ШІ-консультант магазину
@dp.message(F.text)
async def smart_ai_consultant(message: types.Message):
    user_text = message.text.lower()
    
    # 1. Зброя, МК14, обвеси
    if any(word in user_text for word in ["мк", "mk", "зброя", "мк14", "mg3", "js9", "обвес", "пушка"]):
        reply = (
            "🔫 **Ціни на зброю:**\n"
            "• МК14 (покращена) ➖ 9 грн\n"
            "• МК14 (вишка) ➖ 15 грн\n"
            "• MG3 (вишка) ➖ 12 грн\n"
            "• JS9 (вишка) ➖ 13 грн\n\n"
            "‼️ *За кожен обвес +1 грн*\n"
            "⚠️ *Комісія при оплаті за ваш рахунок!*\n\n"
            "✍️ Для замовлення пишіть: @managerVODAFON"
        )
    # 2. Екіпіровка, броня, шоломи, 6 ур
    elif any(word in user_text for word in ["екіпіровку", "екіпіровка", "броня", "шлем", "шолом", "рюкзак", "6 ур", "весь шмот"]):
        reply = (
            "🛍️ **Ціни на екіпіровку (6 рівень):**\n"
            "• Шоломи: звичайний — 7 грн, КБ/СФ — 8 грн\n"
            "• Броня: звичайна — 8 грн, КБ/СФ — 9 грн\n"
            "• Рюкзак: 6 ур. — 9 грн\n\n"
            "⚠️ *Комісія при оплаті за ваш рахунок!*\n"
            "✍️ Замовити можна у менеджера: @managerVODAFON"
        )
    # 3. Супроводи на 7 та 9 карти
    elif any(word in user_text for word in ["карту", "карти", "супровід", "супроводи", "7", "9", "метро", "карт"]):
        reply = (
            "📱 **Супроводи Metro Royale:**\n"
            "🔹 7 карта ➖ 70 грн *(9 млн радіка + від 2 Ф6+)*\n"
            "👑 VIP 7 карта ➖ 110 грн *(10 млн радіка + від 3 Ф6+)*\n"
            "👑 VIP 9 карта ➖ 115 грн *(12 млн радіка + білети + Ф6+)*\n"
            "🏆 GOLD 7 карта ➖ 125 грн *(15 млн радіка + від 4 Ф6+)*\n"
            "🏆 GOLD 9 карта ➖ 200 грн *(18 млн радіка + білети + Ф6+)*\n\n"
            "✍️ Записатися на супровід: @managerVODAFON"
        )
    # 4. Ціни / замовлення загалом
    elif any(word in user_text for word in ["купити", "замовити", "цена", "ціна", "прайс", "коштує"]):
        reply = "🛒 Весь актуальний прайс-лист розбитий по категоріях у нашому головному меню (натисніть /start). Для замовлення звертайтесь до @managerVODAFON 🤝"
    # 5. Менеджер / зв'язок
    elif any(word in user_text for word in ["менеджер", "адмін", "власник", "продавець", "онлайн"]):
        reply = "👤 Наш менеджер на зв'язку! Напишіть йому для оформлення замовлення: @managerVODAFON 🚀"
    # 6. Загальна відповідь
    else:
        reply = (
            "🤖 Вітаю! Я помічник **VODAFON METRO SHOP**.\n"
            "Я можу підказати ціни на зброю, броню, супроводи та аксесуари.\n\n"
            "💬 З усіх питань придбання звертайтесь до менеджера: @managerVODAFON"
        )
        
    await message.answer(reply, parse_mode="Markdown")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущено успішно!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
