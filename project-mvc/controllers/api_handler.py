import random

def get_users():
    # Simulasi server sibuk (peluang error 50%)
    is_error = random.choice([True, False])
    
    if is_error:
        # Mengembalikan JSON dengan pesan error
        return {
            "status": "error", 
            "message": "Server Timeout atau terblokir CORS! Coba lagi."
        }
    
    # Jika tidak error, kembalikan data normal
    return {
        "status": "success",
        "data": [
            {"id": 1, "name": "Admin"},
            {"id": 2, "name": "User"}
        ]
    }