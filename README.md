# Animon Battle Arena

An interactive, turn-based battle game built in **Python**. The system uses an object-oriented card-game structure where players load customized decks, manage active animon states, calculate combat interactions, and tracks game data over an automated lifecycle.

---

## Features

**Class Inheritance:** Utilizes a core base class (`Animon`) to establish generic animon profiles, then derives specific sub-classes (`FireAnimon`, `WaterAnimon`, `GrassAnimon`) that override combat mechanics to execute a specifc animon type advantage.
* **Modules:** Employs explicit object composition by decoupling the `Trainer` state from the underlying array-backed `Deck` module[cite: 4, 9]. The `Trainer` layer completely encapsulates the storage logic, delegating deck actions (drawing, adding, and shuffling) to specialized custom class handler.
* ** CSV Parsing & Data Loading:** Implements an automated data processing that opens exterior files (like `deck1.csv` and `deck2.csv`), cleans raw data strings into corresponding numerical datatypes via `.isdigit()`, and instantiates appropriate polymorphic objects.
* **Custom Error Handling:** Features a specialized structural error architecture using exceptions (`DeckFullError`, `DeckEmptyError`, `InvalidStatError`) to safely catch out-of-bounds metrics, guard state arrays from memory overruns, and handle empty structural queues.
* **Automated Battle Logs & Diagnostics:** Runs continuous checking loops via the `Arena` class that captures structural game states, calculates changing health totals, handles variable state and game resetting, and automatically dumps runtime diagnostics into a permanent local file (`battlelog.txt`).

### Core Game Loop & Entities
* **`main.py`:** The primary file for the program executio. It processes command-line arguments to resolve input configurations, handles deck initialization, handles error-free shuffling, and starts the simulation thread.
* **`arena.py` (`Arena`):** Manages the game lifecycle. It handles turn progression, aggregates damage arrays, detects round completions, evaluates win-loss outcomes, and exports game summaries.
* **`trainer.py` (`Trainer`):** Manages individual player status variables, controlling data snapshots, tracking health thresholds, and checking living/dead status.
* **`deck.py` (`Deck`):** Serves as an indexable list tracking internal cards. Overrides fundamental magic dunder methods (`__len__`, `__iter__`, `__contains__`, `__str__`) to integrate with standard Python operations.
* **`animon.py` (`Animon`):** Defines base stats and structural metadata. It calculates baseline damage formulas and relies on the animon type to override as to scale multi-element combat modifiers[cite: 2].

### Custom Exception Suite
* **`invalid_stat_error.py`:** Catches invalid negative numbers passed into power or defense constructors[cite: 2, 7].
* **`deck_full_error.py`:** Prevents cards from overflowing structural deck size restrictions[cite: 4, 6].
* **`deck_empty_error.py`:** Interrupts array parsing routines if a trainer attempts to draw a piece from an exhausted pile[cite: 3, 4, 5].
