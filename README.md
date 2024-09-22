# TechStore Platform

TechStore Platform is a web-based application built to help tech gadget store owners manage their businesses online by reconnecting them with their customers. The platform is designed to provide seamless management of stores, products, and orders in an organized and user-friendly way. It allows providers (store owners) to manage their inventories, while customers can browse stores and place orders directly on the platform.

## Key Features
- **Store Management**: Providers can create, update, and delete stores with details such as name, location, contact information, and images.
- **Product Management**: Providers can manage product inventories, including adding, updating, and deleting products, each associated with a store.
- **Order Management**: Customers can browse products and place orders from any store.
- **Search Functionality**: Customers can search for products based on category or store name.
- **User Authentication**: Both providers and customers must be authenticated using JWT (JSON Web Tokens) for secure access.
- **Rate Limiting**: Protects the platform from abuse by limiting the number of requests per user.
- **Image Management**: Handles file uploads for store and product images.
- **Flask Swagger Integration**: Provides automatic API documentation for ease of use.

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: SQLAlchemy for ORM, with support for PostgreSQL or SQLite
- **Authentication**: JWT (JSON Web Token) for secure user authentication
- **Rate Limiting**: Flask-Limiter for request rate limiting
- **Image Upload**: Custom utilities for managing product and store images
- **API Documentation**: Swagger (via Flasgger) for auto-generated API documentation
- **Containerization**: Docker and Docker Compose for development and deployment
- **Testing**: Pytest for unit testing

## Project Overview
TechStore Platform consists of two main user roles: **Providers** (store owners) and **Customers**. Providers can manage their stores and product inventories, while customers can search for products and place orders.

### Provider Features
- Register and manage stores
- Add, update, and delete products in their stores
- Upload and manage product images
- View and manage customer orders

### Customer Features
- Search for products by category or store name
- Browse stores and view product details
- Place orders from stores
- View order status and history

## Setup and Installation

### Prerequisites
- Python 3.8+
- PostgreSQL or SQLite for database management
- Docker (optional, for containerization)

### Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/TechStore-Platform.git
    cd TechStore-Platform
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add:
    ```env
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///your_database.db
    JWT_SECRET_KEY=your_jwt_secret
    ```

5. **Initialize the database**:
    ```bash
    flask db upgrade
    ```

6. **Run the application**:
    ```bash
    flask run
    ```

7. **Access the app**:
    Navigate to `http://127.0.0.1:5000` in your browser.

## Deployment

### Using Docker
1. **Build and run the container**:
    ```bash
    docker-compose up --build
    ```

2. **Access the application**:
    Once the container is running, the application will be available at `http://localhost:5000`.

## Contributing
If you want to contribute to TechStore Platform, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and create a pull request.

## Authors
Ibrahim Hanafi - https://github.com/hima890
Ruba Salih - https://github.com/Ruba-Salih
Mohamed Alamen https://github.com/Mohamed-SE23

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
