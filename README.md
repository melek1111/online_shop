# Aurora Tech — Electronics Store

A learning e-commerce project built with Python, Django, SQLite, and Django REST Framework.
The store focuses on consumer electronics such as smartphones, laptops, headphones, cameras,
smartwatches, monitors, and accessories.

## Features

- User registration, login, and logout
- Product catalog and product detail pages
- Search by product name or description
- Filters by category, brand, price, and average rating
- Product ratings and written reviews
- Authenticated shopping cart
- Increase/decrease quantities and remove cart items
- Automatic cart total calculation
- Django Admin panel
- REST API for products, categories, brands, and reviews
- Demo electronics catalog seed command

## Tech Stack

- Python
- Django
- Django ORM
- SQLite
- Django Authentication
- Django Admin
- Django REST Framework
- HTML5, CSS3, Bootstrap 5

## Setup (Windows)

1. Extract the project and open the folder in VS Code.
2. Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
py -m pip install -r requirements.txt
```

4. Create and apply database migrations:

```bash
py manage.py makemigrations shop
py manage.py migrate
```

5. Create an administrator account:

```bash
py manage.py createsuperuser
```

6. (Optional) Add sample electronics products:

```bash
py manage.py seed_store
```

The seed command creates demo categories, brands, and products. Running it again will not
duplicate products that already exist.

7. Start the development server:

```bash
py manage.py runserver
```

Open the store at http://127.0.0.1:8000/

- Admin panel: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/

## Admin Catalog Management

You can add or edit categories, brands, and products through the Django Admin panel.
Each product must be assigned to an existing category and brand. Product images are loaded
from the image URL stored in the product record.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products/` | List products |
| GET | `/api/products/{id}/` | Retrieve one product |
| GET | `/api/categories/` | List categories |
| GET | `/api/brands/` | List brands |
| GET | `/api/reviews/` | List reviews |
| POST | `/api/reviews/` | Create a review (authentication required) |

### Product Filters

Example:

```text
/api/products/?search=phone&category=1&brand=1&min_price=10&max_price=500&min_rating=4
```

Supported query parameters:

- `search`: Search product names and descriptions.
- `category`: Filter by category ID.
- `brand`: Filter by brand ID.
- `min_price`: Minimum product price.
- `max_price`: Maximum product price.
- `min_rating`: Minimum average rating.

## Project Note

This project uses its own Django database. It does not currently integrate with the EverREST API.
The catalog entries are demonstration data; product names, descriptions, prices, and stock values
can be edited from Django Admin.
