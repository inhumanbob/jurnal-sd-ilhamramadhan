import time
from views.dashboard_component import render_dashboard

# Simulasi State
app_state = {"items": [], "is_loading": True}

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False

if __name__ == "__main__":
    # 1. Menampilkan state awal (Data belum ada, is_loading = True)
    render_dashboard(app_state["items"], app_state["is_loading"])
    
    print("\n[Sistem] Mengambil data dari Backend...\n")
    time.sleep(2) # Memberikan jeda 2 detik seolah-olah sedang loading
    
    # 2. Simulasi data masuk dari Backend
    mock_data = [{"id": 101, "name": "Produk A"}, {"id": 102, "name": "Produk B"}]
    update_state(mock_data)
    
    # 3. Menampilkan state akhir (Data sudah ada, is_loading = False)
    render_dashboard(app_state["items"], app_state["is_loading"])