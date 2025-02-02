# FAQ Management System with Multilingual Support

This project is a backend system for managing FAQs with multilingual support. It allows users to create, retrieve, and manage FAQs in multiple languages using a REST API. The system integrates a WYSIWYG editor for formatting answers, supports automated translations, and implements caching for improved performance.

## Features

- **Multilingual FAQ Management**: Store FAQs with translations for multiple languages.
- **WYSIWYG Editor**: Use `django-ckeditor` for rich text formatting of answers.
- **REST API**: Fetch FAQs in different languages using query parameters.
- **Caching**: Implement Redis caching for faster translation retrieval.
- **Admin Panel**: User-friendly interface for managing FAQs.
- **Automated Translations**: Use Google Translate API for automated translations during FAQ creation.
- **Unit Tests**: Comprehensive test coverage for models and APIs.
- **Docker Support**: Easily deploy the application using Docker.

---

## Installation

### Prerequisites

- Python 3.8+
- Redis
- Docker (optional)
- Google Cloud API Key (for translation)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Rajatbisht12/Assignment.git
   cd faq_project
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add the following:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   REDIS_URL=redis://localhost:6379/0
   GOOGLE_TRANSLATE_API_KEY=your_google_translate_api_key
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Run Redis**
   Ensure Redis is running locally or update the `REDIS_URL` in `.env` to point to your Redis instance.

---

## API Usage

### Fetch FAQs

#### Default (English)
```bash
curl http://localhost:8000/api/faqs/
```

#### Fetch FAQs in Hindi
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

#### Fetch FAQs in Bengali
```bash
curl http://localhost:8000/api/faqs/?lang=bn
```

### Create a New FAQ
```bash
curl -X POST http://localhost:8000/api/faqs/ \
-H "Content-Type: application/json" \
-d '{
  "question": "What is Python?",
  "answer": "Python is a programming language."
}'
```

### Update an FAQ
```bash
curl -X PUT http://localhost:8000/api/faqs/1/ \
-H "Content-Type: application/json" \
-d '{
  "question": "What is Django?",
  "answer": "Django is a web framework for Python."
}'
```

### Delete an FAQ
```bash
curl -X DELETE http://localhost:8000/api/faqs/1/
```

---

## Admin Panel

Access the admin panel at `http://localhost:8000/admin/`. Use the superuser credentials to log in and manage FAQs.

To create a superuser:
```bash
python manage.py createsuperuser
```

---

## Caching

The system uses Redis to cache translations for faster retrieval. Ensure Redis is running and configured in the `.env` file.

---

## Automated Translations

The system uses the Google Translate API to automatically translate FAQs into supported languages during creation. Ensure the `GOOGLE_TRANSLATE_API_KEY` is set in the `.env` file.

---

## Running Tests

To run unit tests:
```bash
pytest
```

---

## Docker Support

### Build and Run with Docker

1. **Build the Docker Image**
   ```bash
   docker-compose build
   ```

2. **Run the Application**
   ```bash
   docker-compose up
   ```

3. **Access the Application**
   The API will be available at `http://localhost:8000/`.

---

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feat/your-feature-name
   ```
3. Commit your changes with clear and descriptive messages:
   ```bash
   git commit -m "feat: Add multilingual FAQ model"
   ```
4. Push your branch:
   ```bash
   git push origin feat/your-feature-name
   ```
5. Open a pull request and describe your changes.

---

## Code Quality

- Follow PEP8 guidelines for Python code.
- Use `flake8` for linting:
  ```bash
  flake8 .
  ```
- Write unit tests for all new features and bugfixes.

---

## Deployment

### Heroku

1. Install the Heroku CLI.
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create
   ```
4. Deploy the app:
   ```bash
   git push heroku main
   ```

### AWS (Optional)

Use AWS Elastic Beanstalk or EC2 to deploy the application. Follow the official AWS documentation for detailed instructions.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, please open an issue in the repository or contact the maintainer.

---

This `README.md` provides a comprehensive guide for setting up, using, and contributing to the FAQ Management System. It ensures clarity and ease of use for developers and stakeholders. 🚀