# Student 3 — **Integrare Ecrane, Rezultate & Workflow Repo**
**Branch recomandat:** `feature-main-app`  
**Fișiere principale:** `main.py`  
**Fișiere documentație:** `README.md` (tu îl creezi/îl menții)

---

## 🎯 Obiectiv
Tu ești responsabil ca **fluxul complet** al aplicației să funcționeze fără blocaje: de la introducerea datelor până la afișarea rezultatului. În plus, te ocupi de **igiena repo-ului**: README, pașii de rulare, politica de PR.

---

## 🧭 Sarcini în `main.py`
1. **Managerul de ecrane (ScreenManager):**  
   - Asigură-te că ecranele sunt înregistrate în ordinea corectă: `instr` → `pulse1` → `sits` → `pulse2` → `result`.  
   - Tranzițiile trebuie să aibă loc **doar** după finalizarea etapei curente (timer terminat, input valid).

2. **Variabile globale — *bug fix obligatoriu*:**  
   - Variabilele `name`, `age`, `p1`, `p2`, `p3` sunt la nivel de modul.  
   - În `InstrScr.next`, linia `name = self.in_name.text` creează o variabilă locală, nu actualizează globalul.  
     - **Fix:** adaugă `global name, age` la începutul metodei `next()`.  
     - Asigură `age` minim 7 (deja există fallback).

3. **Validarea intrărilor:**  
   - `check_int` este folosit corect pentru a converti text → int.  
   - Menține protecția: dacă `p1/p2/p3 <= 0`, setează la `0` și scrie în input (comportament existent).  
   - (Opțional) Afișează un mesaj scurt dacă inputul e invalid.

4. **Controlul butoanelor vs. timere:**  
   - Continuă să dezactivezi butoanele cât timp rulează timerele (`self.btn.set_disabled(True)`), apoi reactivează-le când `Seconds.done == True`.

5. **Ecranul de rezultat (`Result`):**  
   - În `before`, setează: `self.instr.text = (name or "Utilizator") + '\n' + test(p1, p2, p3, age)` pentru a evita string gol.  
   - (Opțional) Formatează indicele la 1 zecimală — dacă Student 1 adaugă utilitar `format_index`, folosește-l.

6. **Stilizare:**  
   - Păstrează `Window.clearcolor` și `btn_color` pentru consistență.  
   - Poți ajusta fără a complica (nu face ecrane noi în acest task).

---

## 📘 README.md — responsabilitatea ta
Creează un `README.md` în rădăcina proiectului, cu secțiuni clare:

### 1) Descriere
- Ce este testul Ruffier și ce face aplicația.

### 2) Instalare & Rulare (friendly pentru Arch)
```bash
python -m venv venv
source venv/bin/activate
pip install kivy
python main.py
```
*Alternativ (Arch):* `sudo pacman -S python-kivy`

### 3) Structura proiectului
- 1–2 fraze pentru fiecare fișier (`main.py`, `ruffier.py`, `runner.py`, `seconds.py`, `sits.py`, `instructions.py`).

### 4) Workflow echipă (GitHub)
- Denumire branch-uri:  
  `feature-ruffier-calculations`, `feature-ui-runner`, `feature-main-app`  
- Proces PR: 1 reviewer obligatoriu, fără self-merge.  
- Stil commit: **Conventional Commits** (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).

### 5) Rulare teste (Student 1)
```bash
pytest -q
```

### 6) Echipa
- Cine a lucrat la ce (1–2 linii per student).

### 7) Capturi/GIF
- 2–3 imagini sau un GIF scurt.

---

## 🧪 Plan de testare cap-coadă
1. **Instr**: Introdu nume + vârstă (testează și `< 7`, se corectează automat la 7).  
2. **Pulse #1**: Start → așteaptă 15s → introdu P1 → Continue.  
3. **Sits**: Start → verifică scăderea „Squats left” până la 0 → Continue.  
4. **Pulse #2**: Start → 15s măsurare → 30s pauză → 15s măsurare → introdu P2/P3 → End.  
5. **Result**: vezi numele și interpretarea corectă.  
6. Reia de la început și confirmă că starea se resetează unde e cazul.

---

## 🧭 Workflow Git (minim)
```bash
git checkout -b feature-main-app
# editezi main.py și creezi/scrii README.md
git add main.py README.md
git commit -m "fix: variabile globale name/age; docs: README inițial"
git push origin feature-main-app
# creezi Pull Request către 'main' și ceri review
```

---

## ✅ Criterii de acceptare
- [ ] Traseul `instr → pulse1 → sits → pulse2 → result` funcționează fără blocaje.  
- [ ] Bug-ul variabilelor globale este rezolvat.  
- [ ] `README.md` este complet și ușor de urmărit.  
- [ ] Instrucțiunile de instalare pe Arch (cu venv) sunt corecte.

---

## 🌟 Bonus (opțional)
- Buton **Reset** pe fiecare ecran pentru a relua etapa curentă.  
- Salvarea ultimului rezultat într-un fișier JSON și afișarea la pornire.
