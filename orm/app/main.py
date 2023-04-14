# import mysql.connector
# ~~
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="coffee_machine_management"
#
# my_cursor = mydb.cursor()
#
# my_cursor.close()
import uvicorn
from fastapi import FastAPI

from db.database import get_db

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "Kitty!"}


db = get_db()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
