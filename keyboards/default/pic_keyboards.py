from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        # [
        #     KeyboardButton(text='Kun tabrigi')
        # ],
        [
            KeyboardButton(text='🧔🏻 Yigitlar uchun'),
            KeyboardButton(text='🧕🏻 Qizlar uchun')
        ],
        [
            KeyboardButton(text='🕋 Juma tabriklari'),
            # KeyboardButton(text='🥳 Tug`ilgan kun 🥳')
        ]
    ]
)
