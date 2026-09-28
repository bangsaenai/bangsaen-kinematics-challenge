import hashlib
import platform
import uuid

BANGSAEN_SERVER_HWID_HASH = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

def get_system_hwid():
    """ดึงข้อมูลฮาร์ดแวร์ประจำเครื่อง (CPU, Motherboard, MAC)"""
    raw_info = f"{platform.node()}-{platform.processor()}-{uuid.getnode()}"
    return hashlib.sha256(raw_info.encode()).hexdigest()

def verify_hardware_signature():
    current_hwid = get_system_hwid()
    # ถ้าไม่ใช่เครื่องที่บางแสน ให้ Return False
    is_valid = (current_hwid == BANGSAEN_SERVER_HWID_HASH)
    return is_valid, current_hwid