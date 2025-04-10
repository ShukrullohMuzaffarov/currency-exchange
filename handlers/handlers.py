from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import kb_exchange
from utils import currency_exchange

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("оброго времени суток добро пожаловать в бот для просмотра вальют", reply_markup=kb_exchange)


@router.message(F.text == "💲 ➡️ 🇺🇿")
async def enter_summa(msg: Message, state: FSMContext):
    await state.update_data(valyuta=msg.text)
    await msg.answer("Summani kiriting: ")


@router.message(F.text == "🇺🇿 ➡️ 💲")
async def uzs_enter_summa(msg: Message, state: FSMContext):
    await state.update_data(valyuta=msg.text)
    await msg.answer("Summani kiriting: ")


@router.message(F.text.isdigit())
async def usd_to_sum(msg: Message, state: FSMContext):
    summa = int(msg.text)
    data = await state.get_data()
    if data and ["valyuta"] == ' $ ➡️ uz':
        kurs = await currency_exchange("USD", "UZS")
        await msg.answer(f"{summa} --> UZS = {summa * kurs} USZ")
        await state.clear()
    else:
        kurs = await currency_exchange("USD", "UZS")
        await msg.answer(f"{summa} --> UZS = {summa * kurs} USD")
        await state.clear()