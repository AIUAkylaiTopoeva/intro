'''DRF'''
# API (Application programming interface)- место соприкосновения клиента и сервера. Прдеднозначено для взаимодействия между программами.


'''REST (representational state transfer) - стиль API, стандарт, которому следует API'''

'Принципы REST'
# 1. разграничение клиента и сервера.
# 2. отсутствие состояния (нет сохранения состояния) - сервер не должен хранить какую-либо ин-фу о клиенте.
# 3. кэшиорование 
# 4. многоуровневая система
# 5. единый интерфейс
# 6. код предоставляется по запросу

# REST full API - обычная API которая соответствует принципам REST


'''Django'''
# 1. Создаем виртуальное окружение(venv)

# 2. Активируем окружение

# 3. Создаем файл req.txt
# записываем :
# Django
# djangorestframework
# psycopg2-binary

# 4. Устанавливаем req.txt: pip3 install -r req.txt

# 5. django-admin startproject <project_name>  .   -> создание проекта, если не поставить точку будет вложенность директории

# 6. создание приложения: python3 manage.py startapp <app_name>

# 7. открываем файл settings.py и в INSTALLED_APPS регистрируем rest_framework, <app_name>

# 8. в файле settings.py настраиваем базу данных
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test',
#         'USER': 'user',
#         'HOST': 'localhost',
#         'PORT': 5432
# 
#     }
# }

#  нужно создать файл миграций: python3 manage.py makemigrations 
# python3 manage.py migrate ->чтобы применить изменения
# python3 manage.py createsuperuser - создание админа
# для запуска: python3 manage.py runserver

''''Models'''
# как проходит запрос
# 1. asgi/wsgi -> (те которые принимают и возврощают ответ)
# 2. setting -> middlewares
# 3. urls -> марщрутизаторы
# 4. views -> представления (функции, которые возвращают данные в нужном ФОРмате)
# 5. serializers (классы которые переводят файлы json в питон и наоборот)
# 6. models ->классы, которые обозначают как будет выглядеть наша таблица в db
# 7. managers (objects) -> классы которые работают с orm
# 8. db -> база данных

# =====Поля======

# CharField -> для строкового значения(обязательно нужно указывать max_length)
# SlugField -> для хранения slug( обычно используются в url) cодержит только буквы и числа
# TextField -> для хранения текста
# DecimalField -> для дробных чисел (max_digit: кол-во цифр целой части ; decimal_places: кол-во цифр после запятой)
# IntegerField -> для чисел
# BooleanField -> для bool значений
# DateField -> для дат (datetime.date)  можно передать аргументы : auto_now -> обновляется при изменении записи; auto_now_add -> задается 1 раз при создании
# TimeField -> для времени( auto_now, auto_now_add)
# DateTimeField -> для даты и времени
# EmailField -> для email
# FileField -> для файдов и принимает как аргументы (upload_to -> указание директории , где будет храниться файд
# ImageField -> для картинок ( upload_to)
# JSONField -> для хранения строк в формате json

'''Ключевые параметры для полей (опция)'''
# null -> если True, будет в бд записывать null, если данные не переданы
# blank -> если True, будет ставить пустую строку; не обязательно для заполнения
# default -> значение по умолчанию
# unique -> если True, в кодонке будет храниться только уникальнве значения
# primary key ->если True, будет идентификатором# foreing key -> если True, будет
# choices -> список с tuple (ограничиваем возможные варианты для запалнения


'''Связи'''
# ForeignKey -> связь один ко многим (обязательно указать модель на которую мы будем ссылатьсяб on_delete, related_name- для обратной связи)

# ManyToManyField -> многие ко многим (все тоже самое как и у ForeignKey)


'=======on_delete======'
# models.CASCADE ->каскадное удаление (если удалили главный объект, то удаляются зависящие от него)
# models.PROTECT -> возвращают ошибку при попытке удалить главный объект
# models.SET_NULL -> не удаляет зависящие обекты, а ставит null (mull=True)
# models.SET_DEFAULT -> если определен default, то ставит его
# models.DO_NOTHING -> ничего не делает, вызывается ошибка


#  from test2.models import Category, Post, Tag
#  c = Category(title="sport")
#  c.save
#  p  = Post(title='hello', text='', category=c)
#  p.save()

# p1 = Post.object,create  = 'hrllo2, taxt = '', category=c)
# SELECT * from test2 where id=2
# select * from test2_post;
# select text from test2_post;
 
# select count(*) from test2_post
#  p = Post.objects.all().count()
# Product.objects.all()
# # SELECT * FROM products;
#
# Product.objects.get(id=1)
# SELECT * FROM products WHERE id = 1;

# Product.objects.filter(условие1, условие2)
# SELECT * FROM products WHERE условие AND условие2;

# Product.objects.filter(Q(условие)|Q(условие2))
# SELECT * FROM products WHERE условие1 OR условие2;

# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)
# SELECT * FROM products WHERE NOT условие;

# Product.objects.filter(price__gt=50000) #больше
# SELECT * FROM products WHERE price > 50000;

# Product.objects.filter(price__lt=50000) #меньше
# SELECT * FROM products WHERE price < 50000;

# Product.objects.filter(price=50000) #равно
# SELECT * FROM products WHERE price = 50000;

# Product.objects.filter(~Q(price=50000))
# SELECT * FROM products WHERE NOT price = 50000;

# Product.objects.filter(price__gte=50000)
# SELECT * FROM products WHERE price >= 50000;

# Product.objects.filter(price__lte=50000)
# SELECT * FROM products WHERE price <= 50000;

# Product.objects.filter(category_id__in=['phones', 'notebooks'])
# SELECT * FROM product WHERE category_id IN ('phones', 'notebooks');

# Product.objects.filter(price__range=[20000, 50000])
# SELECT * FROM products WHERE price BETWEEN 20000 AND 50000;

# Product.objects.filter(name__exact='Iphone')
# # SELECT * FROM products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# # SELECT * FROM products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startswith='Iphone')
# # SELECT * FROM products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartswith='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphone')
# # SELECT * FROM products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphone')
# # SELECT * FROM products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphone')
# # SELECT * FROM products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphone')
# # SELECT * FROM products WHERE name ILIKE '%Iphone';

# Product.objects.order_by('price')
# # SELECT * FROM products ORDER BY price ASC;

# Product.objects.order_by('-price')
# SELECT * FROM products ORDER BY price DESC;

# Product.objects.only('name')
# SELECT name FROM products;

# Product.objects.only('name', 'price') #запрашивает указанные поля
# SELECT name, price FROM products;

# Product.objects.defer('name', 'price') #исключает указанные поля
# SELECT id, description, category_id FROM products;

# Product.objects.count()
# SELECT COUNT(*) FROM products;

# Product.objects.filter(...).count()
# SELECT COUNT(*) FROM products WHERE ...;

# Product.objects.create(name='Apple Iphone 12',
#                        description='awddwdawd',
#                        price=78000,
#                        category_id='phones')
# INSERT INTO products (name, description, price, category_id) VALUES \
    # ('Apple Iphone 12', 'dwadaafafaw', 78000, 'phones');

# Product.objects.bulk_create([
#     Product(...),
#     Product(...)
# ]) #множественное создание

# Product.objects.update(price=50000)
# UPDATE products SET price=50000;

# Product.objects.filter(...).update(price=50000)
#UPDATE products SET price=50000 WHERE ...;

# Product.objects.filter(id=1).update(price=50000)
#UPDATE products SET price=50000 WHERE id=1;

# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM products WHERE category_id = 'phones';

# Product.objects.filter(id=1).delete()
# DELETE FROM products WHERE id=1;

# product = Product.objects.get(id=1)
# product.delete()

'''related_name  : позволяет обращаться из связанных объектов к тем от которых эта связь(для обратного поиска) 
~ создает связь с обратной стороны 
~ сat = Category.objects.get(id=1)
~ cat.posts.all()  -> получение всех постов относящихся к данной категории'''

'''related_query_name
~ создает именованный атрибут, который позволяет делать запросы с использованием метода perfetch_related-> загружает связанные объекты(оптимизирует запросы в бд)
~ cat.posts.all()
'''
# QuerySet -> обекты полученные из бд, благодаря maneger (objects)

# Manager -> класс. предомтавляет методы для доступа к ORM Django(отправляет запрос в бд)
# default = objects
# (обновляем, получаем,удаляем, фильтруем данные из таблиц)

'many to many'
# >>> from test2.models import Post, Category, Tag
# >>> t = Tag.objects.create(title='tag1')
# >>> p = Post.objects.get(id=2)
# >>> p.tags.add(t)
# >>> p2 = Post.objects.get(id=4)
# >>> p2.tags.add(t)