import os, json

FILE_PATH = os.path.expanduser("~/.cli_notes.json")

def load_notes():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(FILE_PATH, "w+", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def add_note(added_note):
    notes = load_notes()
    title = added_note.title

    titles = [note['Titre'] for note in notes]
    while title in titles:
        try:
            t, nb = title.split("_")
            title = t + "_" + str(int(nb)+1)
        except:
            title = title + "_1"

    notes.append({'Titre' : title, 'Date de Création' : added_note.creation, "Contenu" : added_note.content})
    save_notes(notes)
    return

def delete_note(title):
    notes = load_notes()
    for index, note in enumerate(notes):
        if note['Titre'] == title:
            del notes[index]
            save_notes()
            return
    print("Note introuvable.")
    return

def list_notes():
    notes = load_notes()
    for note in notes:
        print(note["Titre"])

def open_note(title):
    notes = load_notes()
    for note in notes:
        if note["Titre"] == title:
            print(note["Titre"], "-", note["Date de Création"])
            print(note["Contenu"])
            return
    print("Note introuvable.")
    return

def modif_note(title):
    pass
