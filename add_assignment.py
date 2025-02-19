import json
from datetime import datetime

# Yeni ödev bilgilerini al
assignment_name = input("Ödev adı: ")
due_date_str = input("Son teslim tarihi (YYYY-MM-DD HH:MM:SS): ")

# Ödev verilerini yükleme
with open('assignments.json', 'r') as f:
    assignments = json.load(f)

# Yeni ödevi ekleme
new_assignment = {
    "name": assignment_name,
    "due_date": due_date_str
}
assignments.append(new_assignment)

# Güncellenmiş ödev verilerini kaydetme
with open('assignments.json', 'w') as f:
    json.dump(assignments, f, indent=4)

print("Yeni ödev başarıyla eklendi.")