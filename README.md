# Aurora Online Store — Django

სასწავლო ონლაინ მაღაზია Python + Django + Django REST Framework-ზე.

## ფუნქციები
- რეგისტრაცია, შესვლა და გამოსვლა (Django Authentication)
- პროდუქტების სია და დეტალური გვერდი
- ძებნა სახელით
- ფილტრები: კატეგორია, ბრენდი, ფასი და რეიტინგი
- პროდუქტის შეფასება და ტექსტური Review
- ავტორიზებული მომხმარებლის კალათა
- კალათაში რაოდენობის შეცვლა, წაშლა და ჯამური ფასის დათვლა
- Django Admin
- REST API პროდუქტების, კატეგორიების, ბრენდებისა და შეფასებებისთვის

## გაშვება (Windows)

1. ZIP ამოარქივე და გახსენი საქაღალდე VS Code-ში.
2. ტერმინალში შექმენი ვირტუალური გარემო:

```bash
py -m venv .venv
.venv\\Scripts\\activate
```

3. დააყენე პაკეტები:

```bash
py -m pip install -r requirements.txt
```

4. შექმენი მონაცემთა ბაზის ცხრილები:

```bash
py manage.py makemigrations shop
py manage.py migrate
```

5. შექმენი ადმინისტრატორი:

```bash
py manage.py createsuperuser
```

6. გაუშვი სერვერი:

```bash
py manage.py runserver
```

გახსენი http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/
API root: http://127.0.0.1:8000/api/

## პირველი პროდუქტების დამატება
შედი Admin-ში და დაამატე Category, Brand და Product. პროდუქტს სჭირდება კატეგორია და ბრენდი.
სურათისთვის შეგიძლია მიუთითო სურათის სრული URL (მაგ. https://...).

## API endpoints
- `GET /api/products/`
- `GET /api/products/{id}/`
- `GET /api/categories/`
- `GET /api/brands/`
- `GET /api/reviews/`
- `POST /api/reviews/` (ავტორიზაცია აუცილებელია)

პროდუქტების ფილტრები API-ში: `?search=phone&category=1&brand=1&min_price=10&max_price=500&min_rating=4`

## ტექნოლოგიები
Python, Django, Django ORM, SQLite, Django Authentication, Django Admin,
Django REST Framework, HTML, CSS, Bootstrap 5.

შენიშვნა: ეს პროექტი იყენებს საკუთარ Django მონაცემთა ბაზას და არა EverREST API-ს.
