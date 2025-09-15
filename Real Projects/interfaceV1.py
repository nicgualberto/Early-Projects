import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path
import uuid
from datetime import datetime

DB_PATH = Path("progress.json")

def load_db():
    if not DB_PATH.exists():
        return []
    with DB_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)
    
def save_db(entries):
    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

def short_id(full_id):
    return full_id[:8]

def add_entry():
    topic = entry_topic.get()
    notes = entry_notes.get("1.0", tk.END).strip()
    
    if not topic:
        messagebox.showwarning("Aviso", "O campo Tópico não pode ficar vazio!")
        return
    
    entry = {
        "id": uuid.uuid4().hex,
        "date": datetime.now().isoformat(timespec="seconds"),
        "topic": topic,
        "notes": notes,
        "duration_min": 30
    }
    entries = load_db()
    entries.append(entry)
    save_db(entries)
    
    messagebox.showinfo("Sucesso", f"Salvo : {short_id(entry['id'])} - {topic}")
    entry_topic.delete(0, tk.END)
    entry_notes.delete("1.0", tk.END)
    
def show_entries():
    entries = load_db()
    text_list.delete("1.0", tk.END)
    for e in entries:
        text_list.insert(tk.END, f"{short_id(e['id'])} | {e['date']} | {e['topic']}\nNotas: {e['notes']}\n\n")
        

#interface gráfica
root = tk.Tk()
root.title("Registro de Progresso")

tk.Label(root, text="Tópico:").pack()
entry_topic = tk.Entry(root, width=40)
entry_topic.pack()

tk.Label(root, text="Notas:").pack()
entry_notes = tk.Text(root, height=5, width=40)
entry_notes.pack()

tk.Button(root, text="Salvar sessão", command=add_entry).pack(pady=5)
tk.Button(root, text="Mostrar sessões", command=show_entries).pack(pady=5)

text_list = tk.Text(root, height=15, width=60)
text_list.pack()

root.mainloop()