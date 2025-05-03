# 📘 Kursinio darbo ataskaita – Wordle Solver (OOP projektas)

## 1. Įžanga

### a. Kas yra ši aplikacija?

Ši programa yra interaktyvus Wordle žaidimo sprendėjas, paremtas objektinio programavimo principais. Ji padeda žaidėjui spėti žodį, remiantis įvestais spėjimais ir gauta grįžtamojo ryšio informacija (G = green, Y = yellow, B = gray).

### b. Kaip paleisti programą?

1. Turėti įdiegtą Python 3.10+.
2. Atsisiųsti visą projektą iš GitHub: `git clone https://github.com/Rokusena/Kursinis`
3. Paleisti terminale:

```bash
python src/main.py
```

### c. Kaip naudotis programa?

* Įvedi 5 raidžių žodį (pvz. `alert`)
* Įvedi feedback iš Wordle (pvz. `BGYGB`)
* Programa pateikia geriausias spėjimo strategijas ir kitą žodį
* Kartoji, kol atspėji žodį arba išeini įrašęs `exit`

---

## 2. Pagrindinė analizė

### ✅ 2.1 OOP principai su kodo pavyzdžiais:

**Encapsulation (duomenų paslėpimas):**

```python
class WordleSolver:
    def __init__(self, wordlist):
        self.full_wordlist = wordlist.get_words()
        self.possible_words = self.full_wordlist.copy()
```

> Žodžių sąrašas laikomas viduje, nepasiekiamas tiesiogiai iš išorės.

**Abstraction (abstrakti klasė):**

```python
class SolverStrategy:
    def top_guesses(self, possible_words, n):
        raise NotImplementedError()
```

> Strategijos bendras šablonas, kurį įgyvendina skirtingos strategijos (polimorfizmas).

**Inheritance (paveldėjimas):**

```python
class FrequencySolverStrategy(SolverStrategy):
    def top_guesses(self, possible_words, n=10):
        ...
```

> Ši klasė paveldi `SolverStrategy` ir perrašo `top_guesses()` metodą.

**Polymorphism (elgsena priklauso nuo paveldėtos klasės):**

```python
context = StrategyContext(FrequencySolverStrategy())
context.top_guesses(words, 10)
```

> Kontekstas naudoja tą patį metodą `top_guesses()`, nors strategijos gali skirtis.

### 🎯 2.2 Strategijos šablonas (Strategy Pattern)

```python
class StrategyContext:
    def __init__(self, strategy: SolverStrategy):
        self.strategy = strategy

    def top_guesses(self, possible_words, n=10):
        return self.strategy.top_guesses(possible_words, n)
```

> Leidžia greitai keisti algoritmą (pvz. galima sukurti `RandomSolverStrategy`).

### 📂 2.3 Failų valdymas

```python
wordlist = WordList("data/words.txt")
with open("guess_log.txt", "a") as log_file:
    log_file.write(f"Guess: {guess}, Feedback: {feedback}
")
```

> Programoje įkeliami visi galimi žodžiai iš failo, o naudotojo spėjimai saugomi tekstiniame faile.

### 🧪 2.4 Testavimas su `unittest`

```python
def test_invalid_symbols_or_numbers(self):
    invalid_words = ["a1ert", "al!rt", "12345"]
    for word in invalid_words:
        self.assertFalse(word.isalpha() and len(word) == 5)
```

> Testas patikrina, ar įvestas žodis yra teisingas (5 raidės, be simbolių/skaičių).

---

## 3. Rezultatai ir santrauka

### a. Rezultatai:

* Programa sėkmingai sumažina žodžių sąrašą pagal `GYB` atsakymus
* Strategijos veikimas optimizuotas raidžių dažnio analize
* Vartotojas gauna TOP 10 efektyviausių žodžių kiekviename žingsnyje
* Vartotojo įvestis apsaugota nuo simbolių, pasikartojimų ar neteisingo ilgio

### b. Išvados:

* Programa sėkmingai realizuoja OOP ir strateginį dizaino šabloną
* Lengva palaikyti ir praplėsti su naujomis strategijomis
* Visi techniniai reikalavimai įgyvendinti

### c. Kaip būtų galima išplėsti programą?

* Sukurti grafinę sąsają (pvz. su Tkinter arba PyQt)
* Pridėti automatinį žaidimo simuliatorių
* Įgyvendinti daugiau strategijų (statistinę analizę, machine learning)

---

## 4. Naudoti šaltiniai ir įrankiai (pasirinktinai)

* Python 3.13
* `unittest`, `collections`, `random`
* Wordle oficialus žodynas (panaudota dalis žodžių)
* Git + GitHub versijavimo kontrolei
