# 🛡️ Bangsaen AI Labs: Kinematics Logs Decoding Challenge (EP.22)

> **"เจาะ Database ได้... แต่ได้ไปแค่ตัวเลขขยะ!"**

Repo นี้จำลองเหตุการณ์ Worst-Case Scenario เมื่อ AI Hacker สามารถเจาะผ่าน Firewall และดัมพ์ไฟล์ Log ของระบบ Enterprise ออกไปได้สำเร็จ

### 🎯 โจทย์สำหรับ Hacker & Dev ทั้งประเทศไทย:
ในโฟลเดอร์ `data/breached_kinematics_logs.json` คือประวัติข้อมูลความลับภาษาไทยที่ถูก Sanitized บีบอัดลงใน **Koopman State Vector (8-Dimensional Subspace)**

**ภารกิจของคุณ:** ถอดรหัสไฟล์ตัวเลขดังกล่าวให้กลับมาเป็นข้อความภาษาไทยที่อ่านรู้เรื่อง 100%

### 🚀 วิธีการทดสอบ:
1. Clone Repository นี้ลงเครื่องของคุณ:
   `git clone https://github.com/bangsaen-ai-labs/bangsaen-kinematics-challenge.git`
2. ติดตั้ง Dependencies:
   `pip install -r requirements.txt`
3. รันสคริปต์ถอดรหัส:
   `python src/decode.py`

---

⚠️ **หมายเหตุ:** หากคุณไม่สามารถถอดรหัสได้บนเครื่องของคุณ... โปรดอ่านข้อความเตือนที่แสดงบน Terminal เพื่อดูขั้นตอนการถอดรหัสที่ถูกต้อง

<!-- 
======================================================================
🕵️‍♂️ BANGSAEN LABS SECRET DEV LOGS & EASTER EGGS (FOR CODE INSPECTORS)
======================================================================

[INTERNAL DEV INCIDENT REPORT]:
- v0.1: Attempted Hardcoded Mock -> REJECTED (Reason: Devs will laugh at us).
- v0.2: Implemented Pure Matrix Inverse -> REJECTED (Reason: ModuleNotFoundError on sys.path).
- v0.3: Fixed Path & ROOT_DIR -> SUCCESS.
- v0.4: Discovered we were secretly importing 'koopman_decoder.py' instead of '.pyd' -> EXPOSED!
- v1.0: Purged all .py sources. Compiled to C-Extension (.pyd). Pure Hardware-Bound Binary.

[DECODE HINT / FOR HACKERS]:
If your output shows "Ͽ#7@..." instead of Thai text:
1. Don't inspect the code, it's compiled in C.
2. Don't try to mock 'platform.node()', the seed is bound to CPU registers.
3. The only way to decrypt this file is to drive a Pickup Truck to Bangsaen,
   physically kidnap our Server Rack, and run it on-site!

            _________________
           |                 |
     _____ |  SERVER RACK    | _____
    /     \|  BANGSAEN LABS  |/     \
   |  (o)  |_________________|  (o)  |
   '================================='
   [ AI Hacker Pickup Truck Service ]

======================================================================
-->