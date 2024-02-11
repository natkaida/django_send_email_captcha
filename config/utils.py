import random

def random_word():
    ret = u''
    words = ["компьютер", "ноутбук", "монитор", "клавиатура", "смартфон",
    "мышь", "процессор", "дисплей", "адаптивный", "дизайн", "бэкенд"]
    ret += random.choice(words)
    return ret, ret 
