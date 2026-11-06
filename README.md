# Aurora Online Store — Django

A learning project: an online store built with Python, Django, and Django REST Framework.

## Features

- User registration, login, and logout (Django Authentication)
- Product listing and product detail pages
- Product search by name
- Product filtering by category, brand, price, and rating
- Product ratings and text reviews
- Shopping cart for authenticated users
- Update product quantities and remove items from the cart
- Automatic calculation of the total cart price
- Django Admin Panel
- REST API for products, categories, brands, and reviews

## Installation and Setup (Windows)

1. Extract the ZIP archive and open the project folder in VS Code.

2. Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

3. Install the required packages:

```bash
py -m pip install -r requirements.txt
```

4. Create and apply database migrations:

```bash
py manage.py makemigrations shop
py manage.py migrate
```

5. Create a superuser account:

```bash
py manage.py createsuperuser
```

6. Start the development server:

```bash
py manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

**Admin Panel:** http://127.0.0.1:8000/admin/

**API Root:** http://127.0.0.1:8000/api/

## Adding Your First Products

Log in to the Django Admin Panel and add the following:

1. Categories
2. Brands
3. Products

Each product must be assigned to an existing category and brand.

You can provide a full image URL in the product's image field.

## API Endpoints

| Method | Endpoint              | Description                                       |
| ------ | --------------------- | ------------------------------------------------- |
| GET    | `/api/products/`      | Retrieve all products                             |
| GET    | `/api/products/{id}/` | Retrieve a specific product                       |
| GET    | `/api/categories/`    | Retrieve all categories                           |
| GET    | `/api/brands/`        | Retrieve all brands                               |
| GET    | `/api/reviews/`       | Retrieve all reviews                              |
| POST   | `/api/reviews/`       | Create a product review (authentication required) |

### Product Filtering

Products can be filtered using query parameters:

```text
/api/products/?search=phone&category=1&brand=1&min_price=10&max_price=500&min_rating=4
```

Available filters:

- `search` — Search products by name or description.
- `category` — Filter by category ID.
- `brand` — Filter by brand ID.
- `min_price` — Set the minimum price.
- `max_price` — Set the maximum price.
- `min_rating` — Set the minimum average rating.

## Technologies Used

- Python
- Django
- Django ORM
- SQLite
- Django Authentication
- Django Admin
- Django REST Framework
- HTML5
- CSS3
- Bootstrap 5

## Note

This project uses its own Django database and does not integrate with the EverREST API.
