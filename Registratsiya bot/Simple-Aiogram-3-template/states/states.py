from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    address = State()
    photo = State()
    email = State()
    house_number = State()
   

