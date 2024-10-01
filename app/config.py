import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    
    # MongoDB URI configuration
    MONGO_URI = os.getenv(
        'MONGO_URI',
        'mongodb+srv://j1755532020:TcQMAqgqvXv72RVV@cluster0.rfluj.mongodb.net/nutrition_app'
    )