# Note Taking App

A Django web application for taking notes that utilizes local storage for data persistence. This application demonstrates Django backend development skills including CRUD operations, pagination, and a responsive design.

## Features

- **Create New Notes**: Add new notes via a user-friendly form.
- **View Notes**: Display notes with pagination (10 notes per page).
- **Edit Notes**: Modify existing notes.
- **Delete Notes**: Remove notes permanently.
- **Search Functionality**: Filter notes by title or content.
- **Timestamps**: View creation or last modification time for each note.

## Technical Requirements

### Back-End

- **Framework**: Django for the backend.
- **Database**: SQLite (default) or any other database supported by Django.
- **Local Storage**: Use Django's database system to store notes.

### Front-End

- **Templates**: Django templates for rendering HTML.
- **CSS & Bootstrap**: Responsive design using Bootstrap or custom CSS.

## Features

- **CRUD Operations**:
  - **Create**: Add new notes via a form.
  - **Read**: Fetch and display notes from the database.
  - **Update**: Modify existing notes.
  - **Delete**: Remove notes permanently.

- **Pagination**:
  - Implement pagination to manage and navigate through lists of notes, displaying 10 notes per page.

- **Search Functionality**:
  - Provide a search bar to filter notes by title or content.

- **Timestamps**:
  - Record and display the creation or last modification time for each note.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django (install via pip)
- SQLite (comes bundled with Django) or any other database (optional)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/priyamjha/Django-To-Do-Application.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd simple_note_app
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Open your browser and go to:**

   ```
   http://localhost:8000
   ```

## Usage

- **Home Page**: Displays a paginated list of notes with options to edit or delete, a search bar at the top, and a button to add new notes.
- **Note Item**: Each note displays the title, a brief content excerpt, and the timestamp.
- **Note Form**: A modal or dedicated page for adding or editing note details.
