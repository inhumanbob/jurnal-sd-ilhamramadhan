def fetch_data_from_api(api_function):
    print("[System] Mencoba menghubungkan ke API...")
    try:
        response = api_function()
        if response["status"] == "success":
            return response["data"]
        else:
            # Mengambil pesan error dari dictionary response Backend
            pesan_error = response.get("message", "Terjadi kesalahan yang tidak diketahui.")
            raise Exception(pesan_error)
    except Exception as e:
        print(f"[Error] Gagal Integrasi: {e}")
        return None

def render_dashboard(data_list):
    print("--- DASHBOARD APLIKASI ---")
    if not data_list:
        print("[!] Data Kosong. Silakan sinkronisasi dengan Backend.")
    else:
        for item in data_list:
            print(f"- Item ID: {item['id']} | Nama: {item['name']}")