import os
import json
from datetime import datetime, timedelta
import platform

# Ödev verilerini yükleme
with open('assignments.json', 'r') as f:
    assignments = json.load(f)

# Şu anki tarih ve saat
now = datetime.now()

# Her ödevi kontrol et
for assignment in assignments:
    due_date = datetime.strptime(assignment['due_date'], "%Y-%m-%d %H:%M:%S")
    reminder_time = due_date - timedelta(minutes=1)
    
    # Süre dolmuşsa sesli uyarı gönder
    if now >= reminder_time:
        message = f"Dikkat! '{assignment['name']}' ödevinin son süresine 1 dakika kaldı!"
        if platform.system() == "Darwin":
            # macOS için
            os.system(f'say "{message}"')
        elif platform.system() == "Linux":
            # Linux için
            os.system(f'spd-say "{message}"')
        elif platform.system() == "Windows":
            # Windows için
            os.system(f'powershell [console]::beep(1000,500)')
    else:
        print(f"'{assignment['name']}' ödevinin son süresine henüz 1 dakika kalmadı.")