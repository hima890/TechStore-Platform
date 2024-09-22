# TechStore Platform

TechStore Platform is a web-based application designed to help tech gadget store owners and providers reconnect with their customers and audiences. The platform allows providers to add, manage, and update their products, while users can browse stores and products, place orders, and interact with stores directly. The application was developed using Flask for the backend and supports authentication, product management, store management, and more.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Store Management](#store-management)
  - [Product Management](#product-management)
  - [Order Management](#order-management)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User and Provider Authentication**: JWT-based authentication for secure access.
- **Store Management**: Providers can create, update, and delete stores.
- **Product Management**: Providers can add, update, and delete products with images.
- **Order Management**: Users can place orders for products and manage their orders.
- **Search**: Search products by category and store name.
- **Rate Limiting**: Limits API requests to prevent abuse.
- **Image Handling**: Product and store images are managed using file uploads.

## Technologies
- **Backend**: Flask (Python)
- **Database**: SQLAlchemy (PostgreSQL/SQLite)
- **Authentication**: Flask-JWT-Extended (JWT)
- **Image Handling**: Flask and custom utilities for saving, updating, and deleting images.
- **Rate Limiting**: Flask-Limiter
- **API Documentation**: Flasgger (Swagger for Flask)
- **Testing**: Pytest
- **Environment Management**: `dotenv` for environment variables.

## Project Structure

TechStore-Platform/ ├── app/ │ ├── models/ │ ├── APIs/ │ ├── utils/ │ └── swaggerFile/ ├── migrations/ ├── tests/ ├── config.py ├── .env ├── README.md

- `app/`: Main application directory containing models, APIs, utilities, and Swagger documentation.
- `models/`: Contains the database models for `User`, `Store`, `Product`, and `Order`.
- `APIs/`: Contains the API routes for `authentication`, `store`, `product`, and `order` management.
- `utils/`: Helper utilities for image handling, product ID generation, etc.
- `swaggerFile/`: Swagger documentation files for API endpoints.
- `migrations/`: Database migration files (using Flask-Migrate).
- `tests/`: Test files for API endpoints and models.

## Setup and Installation

### Requirements
- Python 3.8+
- PostgreSQL or SQLite (for local testing)
- Docker (Optional)

### Step-by-Step Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/TechStore-Platform.git
   cd TechStore-Platform

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate

3. **Install the dependencies:**
```bash
pip install -r requirements.txt

