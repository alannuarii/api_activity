import random
import string

def generate_random_code():
    # Menggabungkan angka dan huruf
    characters = string.digits + string.ascii_letters
    
    # Menghasilkan kombinasi acak sebanyak 6 digit
    random_code = ''.join(random.choice(characters) for i in range(6))
    
    return random_code