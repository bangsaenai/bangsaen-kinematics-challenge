import sys
import os
import json
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR) if os.path.basename(CURRENT_DIR) == "src" else CURRENT_DIR

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.koopman_decoder import KoopmanDecoderEngine

def main():
    print("=" * 65)
    print("⚡ BANGSAEN AI LABS - KINEMATICS LOG DECODER ENGINE v2.0")
    print("🔒 Sovereign Hardware-Bound Cryptographic Vector Space")
    print("=" * 65)
    
    start_time = time.time()
    
    print("[*] Accessing In-Memory Hardware Cryptographic Salt...")
    
    
    json_path = os.path.join(ROOT_DIR, "data", "breached_kinematics_logs.json")
    print(f"[*] Loading State Vectors from {json_path}...")
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data_payload = json.load(f)
            vector_data = data_payload.get("vectors", [])
    except FileNotFoundError:
        print(f"❌ [ERROR]: ไม่พบไฟล์ {json_path} (โปรดรัน generate_challenge_data.py ก่อน)")
        return

    
    decoder = KoopmanDecoderEngine()
    result_text = decoder.decode(vector_data)
    
    elapsed_time = (time.time() - start_time) * 1000
    
    print("\n" + "=" * 65)
    print(f"🔓 DECODING RESULT (Execution Time: {elapsed_time:.2f} ms):")
    print("=" * 65)
    print(result_text)
    print("=" * 65)

if __name__ == "__main__":
    main()