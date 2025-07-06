from fastapi import FastAPI
from main import app  # importa tu instancia de FastAPI
from vercel_python import make_handler

handler = make_handler(app)
