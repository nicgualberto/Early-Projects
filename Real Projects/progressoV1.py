import json
import uuid
from datetime import datetime
from pathlib import Path
import csv

DB_PATH = Path("progress.json")

def load_db():
    if not DB_PATH.exists():
        return []
    with DB_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_db(entries):
    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

def now_iso():
    return datetime.now().isoformat(timespec="seconds")

def short_id(full_id):
    return full_id[:8]


def make_entry(date_iso, duration_min, topic, subtopic, resource, difficulty, rating, notes, code_path, tags, completed):
    return {
        "id": uuid.uuid4().hex,
        "date": date_iso,
        "duration_min": int(duration_min),
        "topic": topic.strip(),
        "subtopic": subtopic.strip(),
        "resource": resource.strip(),
        "difficulty": int(difficulty),
        "rating": int(rating),
        "notes": notes.strip(),
        "code_path": code_path.strip(),
        "tags": [t.strip() for t in tags.split(",")] if tags else [],
        "completed": bool(completed)
    }

def interactive_add():
    print("\033[1;36mRegistrar nova sessão - deixe em branco valores padrão!\033[m")
    date_input = input(f"\033[1;33mData\033[m (ISO) [{now_iso()}]: ").strip() or now_iso()
    duration = input("\033[1;34mDuração\033[m (minutos) [30]: ").strip() or "30"
    topic = input("\033[1;35mTópico\033[m (ex: Python - Fundamentos): ").strip() or "Sem tópico"
    subtopic = input("\033[1;36mSubtópico\033[m (ex: listas, dicionários): ").strip() or ""
    resource = input("\033[1;37mRecurso\033[m (ex: Gustavo - Mundo 2, URL): ").strip() or ""
    difficulty  = input("\033[1;31mDificuldade\033[m 1-5 [3]: ").strip() or "3"
    rating = input("\033[1;32mAuto - Avaliação 1-5 [0 se não quiser]: ").strip() or "0"
    notes = input("\033[1;33mNotas rápidas\033[m: ").strip() or ""
    code_path = input("\033[1;34mCaminho do código salvo (se houver)\033[m: ").strip() or ""
    tags = input("\033[1;35mTags\033[m (separar por vírgula, ex: listas,exercícios): ").strip() or ""
    completed = input("\033[1;34mSessão completa? (s/n) [S]\033[m: ").strip().lower() != "n"

    entry = make_entry(date_input, duration, topic, subtopic, resource, difficulty, rating, notes, code_path, tags, completed)
    entries = load_db()
    entries.append(entry)
    save_db(entries)
    print(f"\033[1;36mSalvo: {short_id(entry['id'])} - {entry['topic']} ({entry['duration_min']} min)\033[m")

def list_all_entries():
    entries = load_db()
    if not entries:
        print("\033[1;31mNenhuma entrada registrada ainda!\033[m\n")
        return
    print("\n\033[1;37mSessões Registradas\033[m:\n")
    print(f"{'ID':8} {'Data':19} {'Tópico':30} {'Min':4} {'Dif':3} {'RT':2} {'Tags'}")
    print("-"*80)
    for e in entries:
        print(f"{short_id(e['id']):8} {e['date'][:19]} {e['topic'][:30]:30} {e['duration_min']:4} {e['difficulty']:3} {e['rating']:2} {', '.join(e['tags'])}")
    print("-"*80 + "\n")

def search_entries():
    term = input("\033[1;33mDigite o termo para buscar:\033[m ").strip().lower()
    entries = load_db()
    matches = [e for e in entries if term in e['topic'].lower() 
               or term in e['subtopic'].lower() 
               or term in e['notes'].lower() 
               or any(term in t.lower() for t in e['tags'])]
    if not matches:
        print(f"\033[1;31mNenhum resultado para: {term}\033[m\n")
        return
    print(f"\n\033[1;37mResultados para '{term}'\033[m:\n")
    for e in matches:
        print(f"{short_id(e['id'])} | {e['date'][:19]} | {e['topic']} / {e['subtopic']} | {e['duration_min']}min | tags: {', '.join(e['tags'])}")
    print("")

def stats():
    entries = load_db()
    if not entries:
        print("\033[1;31mSem dados para estatísticas.\033[m\n")
        return
    total = sum(e['duration_min'] for e in entries)
    sessions = len(entries)
    avg = total / sessions
    freq = {}
    for e in entries:
        freq[e['topic']] = freq.get(e['topic'], 0) + 1
    most_topic = max(freq.items(), key=lambda kv: kv[1])
    print("\033[1;36m=== Estatísticas ===\033[m")
    print(f"Sessões: {sessions}")
    print(f"Tempo total: {total} minutos ({total/60:.1f} horas)")
    print(f"Tempo médio por sessão: {avg:.1f} min")
    print(f"Tópico mais frequente: {most_topic[0]} ({most_topic[1]} sessões)\n")

def export_csv():
    path = input("\033[1;33mDigite o nome do arquivo CSV para exportar:\033[m ").strip()
    if not path.endswith(".csv"):
        path += ".csv"
    entries = load_db()
    if not entries:
        print("\033[1;31mSem entradas para exportar.\033[m\n")
        return
    keys = ["id","date","duration_min","topic","subtopic","resource","difficulty","rating","notes","code_path","tags","completed"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        for e in entries:
            row = [e.get(k) if k != "tags" else ";".join(e.get("tags",[])) for k in keys]
            writer.writerow(row)
    print(f"\033[1;36mExportado para {path}!\033[m\n")

def show_notes():
    entries = load_db()
    if not entries:
        print("\033[1;31mNenhuma sessão foi registrada ainda!\033[m")
        return
    
    print("\n\033[1;36m=== Notas Registradas ===\033[m\n")
    for e in entries:
        if e['notes']:
            print(f"{short_id(e['id'])} | {e['date'][:19]} | {e['topic']}")
            print(f"Notas: {e['notes']}\n")
def menu():
    while True:
        print("\033[1;34m=== PROGRESSO EM PROGRAMAÇÃO ===\033[m")
        print("1. Adicionar sessão")
        print("2. Listar sessões")
        print("3. Buscar por termo")
        print("4. Estatísticas")
        print("5. Exportar CSV")
        print("6. Ler notas")
        print("0. Sair")
        choice = input("\033[1;33mEscolha uma opção:\033[m ").strip()
        if choice == "1":
            interactive_add()
        elif choice == "2":
            list_all_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            stats()
        elif choice == "5":
            export_csv()
        elif choice == "6":
            show_notes()
        elif choice == "0":
            print("\033[1;36mSaindo...\033[m")
            break
        else:
            print("\033[1;31mOpção inválida. Tente novamente.\033[m\n")

if __name__ == "__main__":
    menu()
