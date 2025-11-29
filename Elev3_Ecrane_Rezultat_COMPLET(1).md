# Elevul 3 — Ecranele aplicației și rezultatul final (versiune completă și explicată)

Tu ești elevul care face ca **aplicația să funcționeze ca un tot unitar**.  
Toți ceilalți colegi lucrează la calcule sau cronometre, dar tu ești cel care **leagă totul**: ecrane, butoane și fluxul complet.  
Vei lucra doar în fișierul `main_app.py`.

----------------------------------------------------------------

## 1. Ce trebuie să știi înainte

Aplicația are 5 ecrane (pagini). Fiecare este o clasă proprie. Toate sunt adăugate într-un `ScreenManager`, care decide ce ecran se vede pe rând.

| Clasa | Rol | Ce face |
|-------|------|----------|
| `InstrScr` | Introducere date | Cere nume și vârstă |
| `PulseScr` | Primul test | Cronometru 15s, măsurare puls P1 |
| `CheckSits` | Exerciții | 30 genuflexiuni (cronometru + animație) |
| `PulseScr2` | Al doilea test | Puls P2 și P3 (două etape de măsurare) |
| `Result` | Rezultat final | Afișează numele, scorul și interpretarea |

----------------------------------------------------------------

## 2. Ce face ScreenManager

`ScreenManager` e ca un „controler” care gestionează toate paginile.  
În cod, apare așa:

```python
sm = ScreenManager()
sm.add_widget(InstrScr(name='instr'))
sm.add_widget(PulseScr(name='pulse1'))
sm.add_widget(CheckSits(name='sits'))
sm.add_widget(PulseScr2(name='pulse2'))
sm.add_widget(Result(name='result'))
return sm
```

Asta înseamnă: adaugă 5 ecrane și pornește cu primul (`instr`).  
Când vrem să schimbăm ecranul, se folosește o linie ca aceasta:
```python
self.manager.current = 'pulse1'
```

----------------------------------------------------------------

## 3. Ce trebuie să faci tu

1. Să scrii comentarii scurte și clare la începutul fiecărei clase, ca să înțelegi ce face.
2. Să corectezi salvarea numelui și vârstei, pentru ca toate ecranele să le vadă.
3. Să explici ce face fiecare metodă importantă.
4. Să rulezi aplicația și să verifici dacă trecerea între ecrane merge corect.

----------------------------------------------------------------

## 4. Deschide proiectul

1. Deschide **VS Code**.
2. Mergi la **File → Open Folder**.
3. Alege folderul proiectului (cel care are `main_app.py`).
4. Dă clic pe fișierul **`main_app.py`** în bara din stânga.

----------------------------------------------------------------

## 5. Adaugă explicații la începutul fiecărei clase

### a) `InstrScr` — Introducerea datelor

Caută linia:
```python
class InstrScr(Screen):
```

Scrie deasupra ei:
```python
# Ecranul 1 - Introducerea datelor (nume și vârstă).
# După completare, apasă butonul Start și trece la testul 1 (PulseScr).
```

Caută funcția `next(self)` din această clasă.

Adaugă la începutul ei linia:
```python
global name, age
```

Explicație:
- `global` înseamnă că variabilele `name` și `age` devin vizibile pentru toate celelalte ecrane.
- Linia `self.manager.current = 'pulse1'` schimbă ecranul activ spre următorul test.

----------------------------------------------------------------

### b) `PulseScr` — Primul test (15 secunde)

Caută:
```python
class PulseScr(Screen):
```
Scrie deasupra:
```python
# Ecranul 2 - Primul test de puls (15 secunde).
# Cronometrul pornește când se apasă butonul Start.
# La final, elevul introduce pulsul și trece mai departe.
```

Explică în cod, cu comentarii:
- `self.lbl_sec = Seconds(15)` → creează un cronometru de 15 secunde.
- `self.lbl_sec.start()` → pornește cronometru.
- `self.in_result.text` → câmp unde se introduce valoarea măsurată (P1).
- `self.manager.current = 'sits'` → trece la ecranul următor (genuflexiuni).

----------------------------------------------------------------

### c) `CheckSits` — Exercițiile

Caută:
```python
class CheckSits(Screen):
```
Scrie deasupra:
```python
# Ecranul 3 - Exercițiile (30 genuflexiuni).
# Aici rulează cronometru și animația (Runner și Sits).
# Când s-au terminat genuflexiunile, se apasă Continue.
```

Comentarii în cod (explică logic):
- `self.run = Runner(total=30, steptime=1.5)` → rulează 30 de mișcări, fiecare durează 1.5 secunde.
- `self.run.bind(value=self.lbl_sits.next)` → de fiecare dată când se face o mișcare, se actualizează textul „Squats left”.
- `self.manager.current = 'pulse2'` → trece la următorul test.

----------------------------------------------------------------

### d) `PulseScr2` — Al doilea test (P2 și P3)

Caută:
```python
class PulseScr2(Screen):
```
Scrie deasupra:
```python
# Ecranul 4 - Al doilea test de puls.
# Aici se măsoară de două ori: o dată imediat după efort și o dată după pauză.
# Etapele: 15 secunde măsurare (P2), 30 secunde pauză, 15 secunde măsurare (P3).
```

Explică secvența logică:
- `self.stage` → etapa curentă (0, 1 sau 2).
- `self.lbl_sec.restart(30)` → repornește cronometru pentru pauză.
- `self.manager.current = 'result'` → la final trece la rezultatul final.

----------------------------------------------------------------

### e) `Result` — Afișarea rezultatului

Caută:
```python
class Result(Screen):
```
Scrie deasupra:
```python
# Ecranul 5 - Rezultatul final.
# Afișează numele și interpretarea calculată de funcția test() din ruffier.py.
```

Caută funcția `before(self)` și explică în cod:

```python
# Funcția before se execută automat când intrăm pe acest ecran.
# Folosește variabilele globale (name, age, p1, p2, p3) și afișează rezultatul.
```

Poți adăuga un mic mesaj de final după linia:
```python
self.instr.text = name + '\n' + test(p1, p2, p3, age)
```
Adaugă:
```python
self.instr.text += "\n\nMulțumim că ai folosit aplicația HeartCheck"
```

----------------------------------------------------------------

## 6. Testează aplicația complet

1. Apasă Ctrl + F5 pentru a rula.
2. Introdu un nume (de exemplu: Andrei) și o vârstă (de exemplu: 14).
3. Urmează toate etapele:
   - Primul puls (15 secunde)
   - Exercițiile (30 genuflexiuni)
   - Al doilea puls (15 secunde + 30 secunde pauză + 15 secunde)
   - Rezultatul final (cu nume și text explicativ)

Dacă aplicația merge dintr-un ecran în altul fără erori și afișează textul final, ai făcut totul corect.

----------------------------------------------------------------

## 7. Verificare logică finală

Verifică:
- Dacă numele și vârsta introduse la început apar în rezultat.
- Dacă ecranele se schimbă corect în ordine (instr → pulse1 → sits → pulse2 → result).
- Dacă textul final se actualizează diferit când modifici valorile pulsului.

Dacă toate acestea funcționează, ai terminat perfect.

----------------------------------------------------------------

Ai terminat. Partea ta leagă întreaga aplicație.  
Fără tine, celelalte părți nu ar lucra împreună.
