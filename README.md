# Inventory Management System

This Django project is a simple inventory management system that allows you to manage and query product information. It provides a RESTful API to list products and filter them based on various criteria.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/inventory.git
cd inventory
```

2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install project dependencies:
```bash
pip install -r requirements.txt
```

## Running the Development Server

To start the Django development server, run the following command:
```bash
python manage.py runserver
```

The server will be accessible at http://127.0.0.1:8000/.

Applying Database Migrations
Before running the server, apply database migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## API Endpoints

List all products: GET /products/
Filter products by name, category, minimum price, and maximum price:
GET /products/?name=<name>&category=<category>&min_price=<min_price>&max_price=<max_price>
## Usage

To populate the database with sample data, you can use the Django admin interface or create products using the Django shell.