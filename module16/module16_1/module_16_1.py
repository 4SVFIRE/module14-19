from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница"


@app.get('/user/admin')
async def admin():
    return "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def get_user_by_id(user_id:int):
        return f"Вы вошли как пользователь № {user_id}"


@app.get('/user')
async def users(username:str, user_age:int):
    return f"Иформация о пользователе. Имя: {username}, возраст: {user_age}"