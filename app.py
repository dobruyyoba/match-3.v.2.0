from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Монтируем папку с экспортированными файлами Godot
app.mount("/game", StaticFiles(directory="/home/acer/match-3/web-macth3"), name="game")

