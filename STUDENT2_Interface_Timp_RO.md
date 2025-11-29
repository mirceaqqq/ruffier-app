# Student 2 — **Interfață Kivy, Timp & Animații**
**Branch recomandat:** `feature-ui-runner`  
**Fișiere principale:** `runner.py`, `seconds.py`, `sits.py`

---

## 🎯 Obiectiv
Tu ești responsabil de **experiența vizuală** a utilizatorului în fazele cronometrate și de exerciții. Trebuie să explici clar prin UI „ce se întâmplă acum” și „când se termină”, evitând erorile de dublare a evenimentelor.

---

## 🧱 Ce există deja (și trebuie înțeles)
- **`Seconds` (seconds.py)**  
  - E un `Label` actualizat cu `Clock.schedule_interval(self.change, 1)`.  
  - Când `current >= total`, setează `done=True` și **returnează `False`** din `change` pentru a opri programarea la următorul tick.  
  - `restart(total)` resetează starea și pornește din nou timerul.

- **`Runner` (runner.py)**  
  - Folosește `Animation` pentru a mișca un buton („urcă/coboară”).  
  - Crește `value` cu **1** la fiecare ciclu complet (`step == 1.0` în callback-ul `on_progress`).  
  - Când `value >= total`, oprește repetarea animației și setează `finished=True`.

- **`Sits` (sits.py)**  
  - Ține scorul de genuflexiuni făcute și afișează „Squats left: X”.  
  - Este actualizat prin `self.run.bind(value=self.lbl_sits.next)` din ecranul de exerciții.

---

## 🛠️ Task-uri cerute
1. **Feedback vizual pentru ultimele secunde (Seconds):**
   - Când `current >= total - 5`, evidențiază urgența (ex.: adaugă „‼️”, majuscule sau schimbă culoarea labelului folosind proprietatea `color`).  
   - Comentează în cod ce ai schimbat și de ce.

2. **Metodă sigură de restart (Runner):**
   - Adaugă `restart(total: int | None = None)` care:  
     - Oprește animația curentă (dacă rulează),  
     - Resetează `value`, `finished`,  
     - (opțional) actualizează `total`,  
     - Reporneste animația dacă `autorepeat` este `True`.  
   - Comentează pericolele dublării animațiilor dacă nu oprești înainte.

3. **Evită dublu-binding (CheckSits):**
   - În documentația ta, propune un tipar defensiv: înainte să faci `bind`, fă `unbind` sau setează un flag local pe ecran pentru a nu lega de două ori, în cazul în care utilizatorul reintră pe ecran.  
   - Explică (într-un comentariu) că `on_enter`/`on_pre_enter` pot fi apelate de mai multe ori într-o sesiune.

4. **(Opțional) Semnal sonor:**
   - Folosește `kivy.core.audio.SoundLoader` pentru un beep la fiecare increment de `value`.  
   - Ține cont de situația în care fișierul audio nu e găsit (guard cu `if sound:`).  
   - Parametrizare prin `__init__` (ex.: `beep_sound_path=None`).

5. **Documentează `Clock` și `Animation`:**
   - În docstring, explică: „de ce `Clock` nu e *hard real-time*” și că pot apărea mici derapaje — acceptabile pentru aplicație educațională.  
   - Explică rolul lui `Animation(...).repeat = True` și semnificația lui `on_progress` (valorile `step` în [0.0, 1.0]).

---

## ✅ Livrabile
- `runner.py`, `seconds.py`, `sits.py` actualizate cu docstring-uri clare și comentarii.
- Mică notă în `runner.py` la început despre acuratețea temporizării și potențialul drift.

---

## 🧪 Plan de testare manuală
1. Rulează aplicația și mergi la ecranul de genuflexiuni.  
2. Apasă **Start** → animația rulează, `Sits` scade de la 30 la 0.  
3. Verifică faptul că **`finished`** devine True și butonul „Continue” se activează.  
4. Ieși și reintră în ecran → confirmă că **nu** s-au dublat binding-urile (nu se numără de două ori).  
5. Schimbă temporar `total=5` pentru a verifica feedback-ul ultimelor 5 secunde.

---

## 🧭 Workflow Git (minim)
```bash
git checkout -b feature-ui-runner
# editezi runner.py, seconds.py, sits.py
git add runner.py seconds.py sits.py
git commit -m "feat(ui): feedback ultimele secunde; restart Runner; comentarii Clock/Animation"
git push origin feature-ui-runner
# creezi Pull Request către 'main' și ceri review
```

---

## ✅ Criterii de acceptare
- [ ] `Seconds` evidențiază ultimele 5 secunde.
- [ ] `Runner.restart()` este sigur (nu dublează animații).
- [ ] Binding-ul pentru `Sits.next` nu se dublează la reintrare.
- [ ] Codul este explicat prin docstring-uri clare.

---

## 🌟 Bonus (opțional)
- Etichetă suplimentară cu progresul `value/total`.  
- Funcționalitate **Pauză/Rezumă** pentru timer (documentează limitările).
