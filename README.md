# College Information Chatbot

## Project Overview
The College Information Chatbot is a web-based chatbot system designed to provide students with essential information about their college, including the exam schedule, time table, courses offered, and other academic-related details. This chatbot is built using a front-end UI in HTML, CSS, and JavaScript, while the backend is developed using Django.

## Features
- **Exam Schedule Access**: Provides students with upcoming exam dates and schedules.
- **Time Table Information**: Displays class schedules for different courses.
- **Course Details**: Provides information about available courses, syllabus, and faculty details.
- **General Queries**: Answers frequently asked questions about the college, including admission details, contact information, and facilities.
- **Interactive Chatbot**: Users can interact with the chatbot in a conversational format to retrieve the required information quickly.
- **Voice Recognition**: Enables users to interact with the chatbot using voice commands for a hands-free experience.

## Tech Stack
### Frontend:
- HTML
- CSS
- JavaScript (for chatbot UI interactivity)

### Backend:
- Django (Python framework for handling requests and responses)
- Django REST Framework (for creating API endpoints)
- SQLite / PostgreSQL (for storing college-related data)

## Installation Guide
1. **Clone the Repository**
   ```bash
   git clone https://github.com/KLI888/College-Bot.git
   cd college-chatbot
   ```
2. **Set up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Start the Server**
   ```bash
   python manage.py runserver
   ```
6. **Access the Application**
   Open `http://127.0.0.1:8000/` in your web browser.

## Usage
- Open the chatbot UI in your browser.
- Type your query in the chatbot input field or use voice commands.
- The chatbot will respond with relevant information from the college database.

## API Endpoints
- `GET /api/exam-schedule/` - Fetches exam schedules.
- `GET /api/timetable/` - Retrieves class schedules.
- `GET /api/courses/` - Provides details of available courses.
- `GET /api/faqs/` - Returns frequently asked questions and answers.

## Future Enhancements
- **NLP Integration**: Improve chatbot responses using Natural Language Processing.
- **Authentication System**: Allow students to log in and access personalized data.
- **Admin Panel**: Enable college staff to update schedules and courses dynamically.


## License
This project is licensed under the MIT License.

## Contact
For any queries or contributions, please contact **krushnaborase40@gmail.com**.

