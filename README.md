# 🐍 python-backend-ai

> A structured, test-driven engineering progression from **Python 3.12 fundamentals & OOP** to **production FastAPI backends, PostgreSQL databases, and applied AI engineering** — built in public, one commit per session.

**Author:** [Sujoy Behera](https://github.com/SujoyBehera) · B.Tech CSE @ SRM KTR (Batch of 2029)

---

## 🎯 Architecture & Learning Philosophy

This repository follows a **2-Tier Project-Reinforced Architecture**:
1. **🛠️ Bite-Sized Micro-Projects (Every 3–4 Sessions):** Focused multi-file tools built from scratch to immediately apply core concepts.
2. **🏆 Flagship Milestone Capstones (End of Each Phase):** Production-grade systems tested with `pytest`, documented, and deployed.

---

## 🛠️ Tech Stack

| Layer | Technologies | Status |
| :--- | :--- | :--- |
| **Language & Core** | Python 3.12, Type Hints, OOP, `@dataclass`, JSON I/O | ✅ Active |
| **Testing & Tooling** | `pytest`, `assert`-driven checks, `venv`, Git Branching | ✅ Active |
| **HTTP & Web Scraping** | `requests`, `BeautifulSoup4`, `.env` (`python-dotenv`) | ⏳ Module 1.3 (Next) |
| **Backend Framework** | FastAPI, Pydantic v2, REST CRUD, `async/await`, `TestClient` | ⏳ Phase 2 |
| **Database & Security** | PostgreSQL, SQLAlchemy 2.0, Alembic, Argon2 (`pwdlib`), JWT | ⏳ Phase 3 |
| **DevOps & Cloud** | Docker, `docker-compose`, GitHub Actions CI, Cloud Deploy | ⏳ Phase 3 |
| **Applied AI & RAG** | Google Gemini SDK (`google-genai`), `pgvector`, Redis, Agents | ⏳ Phase 4 |

---

## 📁 Repository Structure

```text
python-backend-ai/
├── dailypractice/                         # Daily hands-on modules & assertion checks
│   ├── day6_check.py                      # Virtual environment (.venv) & sys.prefix verification
│   ├── helpers.py                         # Typed string/tag cleaning utilities & safe mutable defaults
│   ├── day8_main.py                       # Module imports & mutable default argument tests
│   ├── models.py                          # OOP APIKey class with rate-limiting state & methods
│   ├── day9_main.py                       # Instance isolation & rate-limit assertion suite
│   ├── day10_models.py                    # @dataclass (ServerConfig) & class inheritance (Developer)
│   └── day10_main.py                      # Dataclass equality & method overriding assertions
│
├── micro_project_01_expense_tracker_cli/  # 🛠️ Micro-Project 1: Personal Expense Tracker CLI
│   ├── expense_models.py                  # Custom InvalidExpenseError & @dataclass Expense model
│   └── tracker.py                         # ExpenseTracker engine with validation & JSON persistence
│
├── requirements.txt                       # Pinned environment dependencies (pytest)
├── .gitignore                             # Excludes .venv/, __pycache__/, and .env secrets
└── README.md
```

---

## ✅ Progression Log

### 🟢 Phase 1: Python Foundations, Local Dev Tooling & HTTP
- [x] **Module 1.1 — Core Python, Debugging & JSON I/O (Days 1–5):**
  - Lists, list comprehensions, crash-proof dictionary lookups (`.get()`), frequency counter pattern, string normalization (`.strip()`, `.lower()`, `.split()`), `set` deduplication, mutability & `.copy()`, traceback debugging, `try/except`, `assert`, and `json` file I/O.
  - 🏆 **Exam 1 Passed:** `9.5 / 10`
- [x] **Module 1.2 — Local Environment, Git, Type Hints & OOP (Days 6–10):**
  - Local Python 3.12 & `.venv` isolation, Git/GitHub workflow (`.gitignore`, branching, merging, conflict resolution), type hints, multi-file imports, OOP classes (`__init__`, `self`), inheritance (`super()`), and `@dataclass`.
- [ ] 🛠️ **Micro-Project 1 (Day 10.1 — In Progress):** *Personal Finance & Expense Tracker CLI* (`micro_project_01_expense_tracker_cli/`)
- [ ] **Module 1.3 — HTTP, Resilient APIs, Web Scraping & `pytest` (Days 11–16):** Upcoming

---

## 🚀 Run Locally

```powershell
# 1. Clone the repository
git clone https://github.com/SujoyBehera/python-backend-ai.git
cd python-backend-ai

# 2. Create and activate the virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run daily verification scripts
python dailypractice/day8_main.py
python dailypractice/day9_main.py
python dailypractice/day10_main.py
```

---

## 📜 Commit Convention

`feat:` new feature/module · `fix:` bug fix · `test:` assertions/unit tests · `docs:` documentation · `refactor:` folder/code restructuring

---

*Built with consistency: learn → build → test → commit.*
