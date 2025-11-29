# Elevul 2 — Cronometrul și animația exercițiilor (partea ta)

Acest fișier este doar pentru tine. Vei lucra exclusiv în fișierele `seconds.py`, `runner.py`, `sits.py` și vei testa din aplicația principală.

Obiectivele tale, în ordine:
1) Să înțelegi și să comentezi clar ce fac clasele Seconds (cronometru), Runner (animație) și Sits (contor).
2) Să adaugi un mesaj vizibil în ultimele 5 secunde la cronometru.
3) Să afișezi „Gata!” când timpul s-a terminat.
4) Să verifici că animația numără corect genuflexiunile.

----------------------------------------------------------------

## 1. Deschidere proiect și fișierele tale

1. Deschide VS Code.
2. File → Open Folder → alege folderul proiectului.
3. Deschide pe rând fișierele: `seconds.py`, `runner.py`, `sits.py`.
4. Nu modifica alte fișiere.

----------------------------------------------------------------

## 2. `seconds.py` — cronometru simplu

Caută funcțiile din clasă și adaugă comentarii deasupra lor. Ideile sunt mai jos.

### 2.1. Constructorul clasei

Cod din proiect:
```python
class Seconds(Label):
    done = BooleanProperty(False)
  
    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        my_text = "Seconds elapsed: " + str(self.current)
        super().__init__(text=my_text)
```

Comentariu pe care să îl adaugi deasupra:
```python
# Creează un cronometru care pornește de la 0 și merge până la 'total' secunde.
# Afișează textul pe ecran (moștenește comportamentul unei etichete Label).
```

### 2.2. Metoda `restart`

Cod din proiect:
```python
def restart(self, total, **kwargs):
    self.done = False
    self.total = total
    self.current = 0
    self.text = "Seconds elapsed: " + str(self.current)
    self.start()
```

Comentariu de adăugat:
```python
# Resetează cronometrul la 0, setează noul total și pornește din nou.
```

### 2.3. Metoda `start`

Cod din proiect:
```python
def start(self):
    Clock.schedule_interval(self.change, 1)
```

Comentariu de adăugat:
```python
# Pornește cronometru: apelează 'change' o dată pe secundă.
```

### 2.4. Metoda `change` — aici faci și modificările cerute

Cod din proiect (original):
```python
def change(self, dt):
    self.current += 1
    self.text = "Seconds elapsed: " + str(self.current)
    if self.current >= self.total:
        self.done = True
        return False
```

Modifică astfel:
1) Pentru ultimele 5 secunde (când se apropie finalul), schimbă mesajul afișat.
2) Când s-a terminat, scrie „Gata!”.

Varianta nouă sugerată:
```python
def change(self, dt):
    self.current += 1
    if self.total - self.current <= 5 and self.current < self.total:
        self.text = "Aproape gata: " + str(self.current)
    else:
        self.text = "Seconds elapsed: " + str(self.current)
    if self.current >= self.total:
        self.done = True
        self.text = "Gata!"
        return False
```

Salvează fișierul: Ctrl + S.

----------------------------------------------------------------

## 3. `runner.py` — animația butonului (ritmul genuflexiunilor)

Găsești două lucruri importante: animația și numărarea mișcărilor.

Fragmente din proiect:
```python
self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2)
                + Animation(pos_hint={'top': 1.0}, duration=steptime/2))
self.animation.on_progress = self.next
```

Adaugă un comentariu deasupra:
```python
# Creează o animație sus-jos. Când o mișcare completă se termină (step == 1.0),
# metoda next crește contorul 'value' cu 1.
```

La metoda `next` există deja logica:
```python
def next(self, widget, step):
    if step == 1.0:
        self.value += 1
        if self.value >= self.total:
            self.animation.repeat = False
            self.finished = True
```

Adaugă un comentariu:
```python
# O creștere completă (sus-jos) = o genuflexiune. Când ajungem la total, oprim.
```

Nu adăuga cod în plus aici. Doar comentează să înțelegi.

----------------------------------------------------------------

## 4. `sits.py` — contorul de genuflexiuni

Codul important:
```python
def next(self, *args):
    self.current += 1
    remain = max(0, self.total - self.current)
    my_text = "Squats left: " + str(remain)
    self.text = my_text
```

Comentariu de adăugat deasupra:
```python
# La fiecare mișcare (anunțată de Runner), scade câte au mai rămas și afișează.
```

----------------------------------------------------------------

## 5. Testare din aplicație

1. Deschide `main_app.py`.
2. Rulează aplicația: Ctrl + F5.
3. Mergi la pasul cu genuflexiunile (Sits).
4. Apasă „Start”.
5. Verifică două lucruri:
   - În ultimele 5 secunde de cronometru apare mesajul „Aproape gata”.
   - După ce timpul s-a terminat, apare „Gata!”.
6. Verifică că numărul „Squats left” scade până la 0.

Dacă toate se văd corect, ai terminat partea ta.

----------------------------------------------------------------

Ai terminat. Partea ta ține de timp, mișcare și afișare clară a stării.
