# 🐍 python-backend-ai

> A structured, test-driven progression from **Python fundamentals** to **production backend APIs** and **applied AI engineering** — built in public, one commit per learning session.

**Author:** [Sujoy Behera](https://github.com/SujoyBehera) · B.Tech CSE @ SRM KTR (Batch of 2029)

---

## 🎯 Goal

Build real, tested, deployable backend systems in Python — and layer practical AI features (LLM APIs, RAG, tool-calling agents) on top of them.

## 🛠️ Tech Stack

| Area | Tools |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Backend** *(upcoming)* | FastAPI, Pydantic v2 |
| **Database** *(upcoming)* | PostgreSQL, SQLAlchemy 2.0, Alembic |
| **Testing** | `pytest`, `assert`-driven checks |
| **Security** *(upcoming)* | JWT, Argon2/Bcrypt password hashing |
| **DevOps** *(upcoming)* | Docker, GitHub Actions, cloud deployment |
| **AI** *(upcoming)* | Gemini SDK, structured outputs, `pgvector` RAG, tool calling |

> Items marked *(upcoming)* are on the roadmap and are only claimed once I've passed that module's exam.

## 🗺️ Roadmap

| Phase | Focus | Status |
| :--- | :--- | :--- |
| **1** | Python foundations, local tooling, Git, OOP, HTTP & `pytest` | 🟡 In progress |
| **2** | FastAPI, Pydantic validation, REST CRUD, `async/await`, API testing | ⏳ Next |
| **3** | PostgreSQL, SQLAlchemy, auth (JWT), authorization, Docker, deployment | ⏳ Planned |
| **4** | LLM APIs, structured outputs, embeddings, RAG, agent guardrails | ⏳ Planned |

## ✅ Progress So Far

- **Module 1.1 — Core Python** *(complete, graded exam passed)*: lists, dicts, sets, comprehensions, string cleaning, mutability, `try/except`, `assert`, file & JSON I/O
- **Module 1.2 — Local Dev & OOP** *(in progress)*: virtual environments, Git/GitHub workflow, type hints, modules, classes

## 🚀 Run Locally

```powershell
git clone https://github.com/SujoyBehera/python-backend-ai.git
cd python-backend-ai

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest
```

## 📁 Repository Layout

```text
python-backend-ai/
├── practice.py         # daily practice scripts
├── requirements.txt    # pinned dependencies
├── .gitignore          # excludes .venv, __pycache__, .env
└── README.md
```

*(The layout will grow into `app/`, `tests/`, and `docs/` as the FastAPI milestones begin.)*

## 📜 Commit Convention

`feat:` new capability · `fix:` bug fix · `test:` tests · `docs:` documentation · `refactor:` restructuring

---

*Built with consistency: learn → build → test → commit.*
