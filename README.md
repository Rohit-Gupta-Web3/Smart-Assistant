# 🧠 Smart Conversational Assistant with Memory

A Django + Django REST Framework-based AI chatbot that integrates HuggingFace models to hold memory-aware conversations. Frontend is designed to impress.

---

## 📦 Project Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML/CSS + Bootstrap (or Gradio/React optional)
- **AI Model**: HuggingFace Transformers (e.g., DialoGPT, Falcon)
- **Database**: PostgreSQL (recommended for Render)
- **Deployment**: Render.com

---

## 🚀 Getting Started (Local Development)

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/smart-assistant.git
cd smart-assistant
```

### 2. Create virtual environment & install requirements

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
HUGGINGFACE_MODEL=gpt2
```

### 4. Apply migrations and run

```bash
python manage.py migrate
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

---

## 🔌 API Endpoints (DRF)

| Endpoint              | Method   | Description                            |
| --------------------- | -------- | -------------------------------------- |
| `/api/start-session/` | POST     | Start a new chat session               |
| `/api/chat/`          | POST     | Send a message and receive AI response |
| `/api/memory/`        | GET/POST | Retrieve or update session memory      |
| `/api/history/`       | GET      | View full message history              |

---

## 🧠 AI Model (Transformers)

In `transformers_model/model.py`, you can load your model like this:

```python
from transformers import pipeline
chatbot = pipeline("text-generation", model="gpt2")
```

Replace with `DialoGPT`, `Falcon`, or any supported conversational model.

---

## 🌐 Deployment to Render.com

### 1. Push code to GitHub

Make sure your code is pushed to a public or private GitHub repo.

### 2. Create a Render Web Service

- Go to [Render.com](https://render.com/)
- Click **New Web Service**
- Connect to your GitHub repo
- Use the following build settings:

**Build Command:**

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command:**

```bash
gunicorn config.wsgi:application
```

**Environment:**

- Add environment variables in the Render dashboard (SECRET\_KEY, DEBUG=False, DATABASE\_URL, etc.)

**PostgreSQL DB:**

- Add a Render PostgreSQL service and connect `DATABASE_URL` to your Django settings.

---

## 📁 Folder Structure

```
smart_assistant/
├── manage.py
├── requirements.txt
├── README.md

├── config/                        # Django project config
│   ├── __init__.py
│   ├── settings.py               # Main settings
│   ├── urls.py                   # Project-level routing
│   └── wsgi.py / asgi.py

├── chatbot/                      # Main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                # DB models: Session, Message, UserMemory
│   ├── views.py                 # Django views
│   ├── api_views.py             # Chat API endpoint
│   ├── serializers.py           # (If using DRF or custom response structure)
│   ├── urls.py                  # App-level URLs
│   ├── forms.py                 # Input forms (if using Django forms)
│   └── memory.py                # Context memory handler (cache or DB based)

├── templates/                   # HTML templates
│   ├── base.html                # Layout base
│   └── chat.html                # Chat interface

├── static/                      # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── img/

├── transformers_model/          # AI Model logic
│   ├── __init__.py
│   ├── model.py                 # Load + respond using HuggingFace
│   └── utils.py                 # Tokenization, cleaning, filters

├── tests/                       # Unit and integration tests
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   └── test_chatbot.py

├── .env                         # Secrets for local dev
└── .gitignore

```

---

## ✅ To Do Checklist for Students

- &#x20;Implement models and API endpoints
- Add HuggingFace model integration
- Design sleek chat UI (Tailwind or Gradio)
- Deploy to Render with PostgreSQL
- Submit GitHub + live demo + README + short video

---

## 👏 Mentorship Tip

Make the assistant charming, like a product you want to show off. Think beyond basic Q&A: memory, personality, even jokes or Easter eggs!

