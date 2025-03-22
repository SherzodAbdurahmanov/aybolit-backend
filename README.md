# Dr.Aibolit Medicine Reminder API

This project is a backend API for a mobile application designed to help animals (and their owners) remember to take their medication on time. The system allows users to create medication schedules and receive reminders about upcoming doses.

## Technologies Used
- Python 3.13
- Django 4.x
- Django REST Framework
- SQLite (default, can be switched to PostgreSQL)

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dr-aibolit-api.git
   cd dr-aibolit-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### 1. Create Schedule
**POST** `/api/schedule/`

**Request:**
```json
{
  "user": "1",
  "medication_name": "Antibiotic",
  "frequency": 3,
  "duration": 7,
  "taking_time": "2025-03-22T15:00:00Z"
}
```

**Response:**
```json
{
  "schedule_id": 1
}
```

---

### 2. Get All Schedule IDs
**GET** `/api/schedules/?user_id=1`

**Response:**
```json
{
  "schedules": [1, 2, 3]
}
```

---

### 3. Get Schedule Details and Today's Takings
**GET** `/api/schedule-detail/?user_id=1&schedule_id=1`

**Response:**
```json
{
  "schedule": {
    "id": 1,
    "user": "1",
    "medication_name": "Antibiotic",
    "frequency": 3,
    "duration": 7,
    "taking_time": "2025-03-22T15:00:00Z",
    "created_at": "2025-03-20T12:00:00Z"
  },
  "takings_for_today": ["15:00", "18:00", "21:00"]
}
```

---

### 4. Get Upcoming Takings Within an Hour
**GET** `/api/next_takings/?user_id=1`

**Response:**
```json
[
  {
    "id": 1,
    "user": "1",
    "medication_name": "Antibiotic",
    "frequency": 3,
    "duration": 7,
    "taking_time": "2025-03-22T15:00:00Z",
    "created_at": "2025-03-20T12:00:00Z"
  }
]
```

---

## Models

### User
| Field     | Type    | Description               |
|-----------|---------|---------------------------|
| user_id   | Char(50)| Primary Key, unique user  |

### Schedule
| Field            | Type           | Description                            |
|------------------|----------------|----------------------------------------|
| user             | FK to User     | User who takes the medication          |
| medication_name  | Char(255)      | Name of the medication                 |
| frequency        | PositiveInt    | Frequency of intake (hours)            |
| duration         | PositiveInt    | Duration in days (nullable)            |
| taking_time      | DateTime       | Start time for taking the medicine     |
| created_at       | DateTime       | Auto-filled when schedule is created   |

---

## Testing with Postman
1. Import collection (optional) or test endpoints manually.
2. Create schedule via POST `/api/schedule/`.
3. List schedule IDs via GET `/api/schedules/?user_id=1`.
4. Get detailed schedule via GET `/api/schedule-detail/?user_id=1&schedule_id=1`.
5. Get upcoming takings via GET `/api/next_takings/?user_id=1`.

---


