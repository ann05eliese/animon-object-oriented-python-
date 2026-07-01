# Animon Battle Arena

An interactive, turn-based battle simulation built in **Python**. The system uses an object-oriented card-game architecture where players load customized decks, manage active creature states, calculate combat interactions, and track game metrics over an automated lifecycle.

---

## Features

**Class Inheritance Matrix:** Utilizes a core base class (`Animon`) to establish generic creature profiles, then derives specific sub-classes (`FireAnimon`, `WaterAnimon`, `GrassAnimon`) that override combat mechanics to execute distinct type-advantage multipliers[cite: 2].
* **Modular Software Composition:** Employs explicit object composition by decoupling the `Trainer` state from the underlying array-backed `Deck` module[cite: 4, 9]. The `Trainer` layer completely encapsulates the storage logic, delegating deck actions (drawing, adding, and shuffling) to specialized custom class handlers[cite: 4, 9].
* **Robust CSV Parsing & Data Loading:** Implements an automated data-ingestion pipeline that opens exterior configuration files (like `deck1.csv` and `deck2.csv`), sanitizes raw data strings into corresponding numerical datatypes via `.isdigit()`, and instantiates appropriate polymorphic objects dynamically.
* **Custom Error Handling Pipeline:** Features a specialized structural error architecture leveraging native exceptions (`DeckFullError`, `DeckEmptyError`, `InvalidStatError`) to securely catch out-of-bounds metrics, guard state arrays from memory overruns, and gracefully handle empty structural queues[cite: 2, 4, 5, 6, 7].
* **Automated Battle Logs & Diagnostics:** Runs continuous checking loops via an `Arena` orchestration class that captures structural game states, calculates ever changing health totals, handles variable state and game resetting, and automatically dumps runtime diagnostics into a permanent local file (`battlelog.txt`)[cite: 3].

### Core Game Loop & Entities
* **`main.py`:** The primary file orchestrating the program execution[cite: 8]. It processes command-line arguments to resolve input configurations, handles deck initialization, handles error-free shuffling, and starts the simulation thread[cite: 8].
* **`arena.py` (`Arena`):** Manages the game lifecycle[cite: 3]. It handles turn progression, aggregates damage arrays, detects round completions, evaluates win-loss outcomes, and exports game summaries[cite: 3].
* **`trainer.py` (`Trainer`):** Manages individual player status variables, controlling historical data snapshots, tracking health thresholds, and checking living/dead status[cite: 9].
* **`deck.py` (`Deck`):** Serves as an indexable list wrapper tracking internal cards[cite: 4]. Overrides fundamental magic dunder methods (`__len__`, `__iter__`, `__contains__`, `__str__`) to seamlessly integrate with standard Python collection operations[cite: 4].
* **`animon.py` (`Animon`):** Defines base stats and structural metadata[cite: 2]. It calculates baseline damage formulas and relies on the animon type to override as to scale multi-element combat modifiers[cite: 2].

### Custom Exception Suite
* **`invalid_stat_error.py`:** Catches invalid negative numbers passed into power or defense constructors[cite: 2, 7].
* **`deck_full_error.py`:** Prevents cards from overflowing structural deck size restrictions[cite: 4, 6].
* **`deck_empty_error.py`:** Interrupts array parsing routines if a trainer attempts to draw a piece from an exhausted pile[cite: 3, 4, 5].
