# Workflow complet GitHub — echipa HeartCheck

Acest document explică pas cu pas cum să lucrați în echipă pe proiectul HeartCheck folosind **GitHub** și **VS Code**.

Scopul este ca fiecare elev să poată lucra pe partea lui (fișierul propriu), fără să strice munca celorlalți, iar la final toate părțile să fie unite într-un singur proiect complet.

----------------------------------------------------------------

## 1. Ce este GitHub (explicație scurtă)

GitHub este un site unde putem păstra codul online și colabora la el.

- „repository” = un folder online cu codul proiectului.
- „commit” = o salvare a unei modificări (ca un checkpoint).
- „branch” = o versiune separată a codului unde lucrează fiecare elev.
- „merge” = momentul în care un branch este unit cu proiectul principal.

----------------------------------------------------------------

## 2. Ce trebuie instalat (doar prima dată)

1. **Instalează Git**
   - Intră pe https://git-scm.com/download/win
   - Descarcă și instalează (apasă „Next” la tot).
   - După instalare, deschide VS Code și apasă `Ctrl + ~` (tilde) pentru a deschide terminalul.

2. **Verifică instalarea**
   Scrie în terminal:
   ```bash
   git --version
   ```
   Dacă apare ceva de genul `git version 2.x.x`, e bine.

3. **Conectează GitHub la calculator**
   - Creează un cont pe https://github.com/
   - În VS Code, mergi la „Source Control” (iconița cu ramuri) → „Sign in to GitHub”.
   - Conectează-te cu contul tău.

----------------------------------------------------------------

## 3. Configurarea proiectului local

### Variante:

#### a) Dacă profesorul a pus proiectul pe GitHub:

1. Deschide terminalul VS Code.
2. Scrie:
   ```bash
   git clone https://github.com/numele-profesorului/heartcheck.git
   ```
3. Așteaptă să se descarce.
4. După ce s-a terminat, scrie:
   ```bash
   cd heartcheck
   ```

#### b) Dacă profesorul v-a dat folderul local:

1. Deschide VS Code → File → Open Folder → selectează folderul proiectului.
2. Creează un repository Git în el:
   ```bash
   git init
   ```
3. Adaugă remote-ul (legătura cu GitHub):
   ```bash
   git remote add origin https://github.com/numele-profesorului/heartcheck.git
   ```

----------------------------------------------------------------

## 4. Crearea branch-urilor individuale

Fiecare elev lucrează pe un branch propriu:

| Elev | Branch | Fișier principal |
|-------|---------|------------------|
| Elev 1 | `ruffier-calcul` | `ruffier.py` |
| Elev 2 | `timer-animatii` | `seconds.py`, `runner.py`, `sits.py` |
| Elev 3 | `ecrane-rezultat` | `main_app.py` |

### Cum creezi și comuți pe branch-ul tău:

```bash
git checkout -b numele-branchului
```

Exemplu pentru Elevul 1:
```bash
git checkout -b ruffier-calcul
```

Apoi verifică cu:
```bash
git branch
```
Apare o listă cu branch-uri; cel activ are un asterisc (*).

----------------------------------------------------------------

## 5. Lucrul zilnic (modificare + salvare + urcare pe GitHub)

### 1️⃣ Fă modificările în fișierele tale
Editează doar fișierele de care răspunzi.

### 2️⃣ Salvează modificările
```bash
git add .
```

### 3️⃣ Creează un commit (adică o „salvare”)
```bash
git commit -m "Am terminat partea mea din proiect (ruffier.py completat)"
```

### 4️⃣ Trimite modificările pe GitHub
```bash
git push origin numele-branchului
```

Exemplu:
```bash
git push origin ruffier-calcul
```

----------------------------------------------------------------

## 6. Crearea Pull Request-ului (cererea de unire)

Când un elev termină partea lui:

1. Intră pe site-ul GitHub la proiect.
2. Vei vedea un mesaj: „Compare & pull request” → dă clic.
3. Completează o scurtă descriere, ex:
   > Am terminat partea de calcul Ruffier, am testat și merge.

4. Apasă „Create pull request”.

Profesorul (sau liderul echipei) va verifica modificările și le va uni în branch-ul principal (`main`).

----------------------------------------------------------------

## 7. Cum aduci ultimele modificări din proiectul principal

Dacă profesorul a acceptat pull request-ul și codul a fost unit, ceilalți elevi pot actualiza proiectul lor local cu ultimele schimbări:

```bash
git checkout main
git pull origin main
```

Apoi pot reveni la branch-ul propriu:
```bash
git checkout ruffier-calcul
```

----------------------------------------------------------------

## 8. Reguli simple de echipă

1. **Nu modifica fișierele colegilor.** Doar pe cele atribuite ție.
2. **Fă commit des**, de exemplu după fiecare funcție terminată.
3. **Scrie mesaje clare** la commit-uri, ex: `git commit -m "Adăugat funcția de restart la cronometru"`.
4. **Testează înainte de push**, adică rulează aplicația local și vezi dacă merge.
5. **Un singur branch principal (`main`)** — acolo se unește totul doar după verificare.

----------------------------------------------------------------

## 9. Exemplu complet pentru un elev (ex. Elevul 1)

1. Clonează proiectul:
   ```bash
   git clone https://github.com/numele-profesorului/heartcheck.git
   cd heartcheck
   ```

2. Creează branch-ul lui:
   ```bash
   git checkout -b ruffier-calcul
   ```

3. Editează fișierul `ruffier.py` și `test_ruffier.py`.

4. Salvează și trimite pe GitHub:
   ```bash
   git add .
   git commit -m "Am completat funcțiile Ruffier"
   git push origin ruffier-calcul
   ```

5. Pe site-ul GitHub, apasă **Compare & pull request**.

6. Profesorul verifică, apoi face **Merge**.

----------------------------------------------------------------

## 10. Sfaturi finale

- Lucrează doar din VS Code, nu direct din GitHub.
- Înainte să lucrezi, scrie `git pull origin main` ca să ai ultima versiune.
- Dacă apare un conflict (GitHub spune că fișierele s-au schimbat), cere ajutorul profesorului — nu forța comanda.

----------------------------------------------------------------

Dacă urmezi toți pașii de mai sus, toți trei veți putea lucra în același proiect fără să vă încurcați între voi.
