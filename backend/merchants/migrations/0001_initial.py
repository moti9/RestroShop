# Generated by Django 5.0.2 on 2024-04-10 19:30

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import merchants.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('gluten', 'Gluten'), ('dairy', 'Dairy'), ('eggs', 'Eggs'), ('soy', 'Soy'), ('peanuts', 'Peanuts'), ('tree_nuts', 'Tree Nuts'), ('fish', 'Fish'), ('shellfish', 'Shellfish'), ('sesame', 'Sesame'), ('mustard', 'Mustard'), ('celery', 'Celery'), ('lupin', 'Lupin'), ('molluscs', 'Molluscs'), ('sulfites', 'Sulfites'), ('meat', 'Meat'), ('poultry', 'Poultry'), ('wheat', 'Wheat'), ('corn', 'Corn'), ('yeast', 'Yeast'), ('lactose', 'Lactose'), ('onions', 'Onions'), ('garlic', 'Garlic'), ('tomatoes', 'Tomatoes'), ('citrus_fruits', 'Citrus Fruits'), ('chocolate', 'Chocolate'), ('coffee', 'Coffee'), ('tea', 'Tea'), ('alcohol', 'Alcohol'), ('other', 'Other'), ('na', 'Not Available')], default='other', max_length=50)),
            ],
            options={
                'verbose_name': 'Allergen',
                'verbose_name_plural': 'Allergens',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('indian', 'Indian'), ('chinese', 'Chinese'), ('italian', 'Italian'), ('mexican', 'Mexican'), ('japanese', 'Japanese'), ('american', 'American'), ('thai', 'Thai'), ('french', 'French'), ('spanish', 'Spanish'), ('greek', 'Greek'), ('korean', 'Korean'), ('vietnamese', 'Vietnamese'), ('german', 'German'), ('brazilian', 'Brazilian'), ('levantine', 'Levantine'), ('caribbean', 'Caribbean'), ('moroccan', 'Moroccan'), ('australian', 'Australian'), ('argentinian', 'Argentinian'), ('ethiopian', 'Ethiopian'), ('turkish', 'Turkish'), ('russian', 'Russian'), ('iranian', 'Iranian'), ('lebanese', 'Lebanese'), ('pakistani', 'Pakistani'), ('bangladeshi', 'Bangladeshi'), ('sri_lankan', 'Sri Lankan'), ('nepalese', 'Nepalese'), ('afghan', 'Afghan'), ('other', 'Other'), ('na', 'Not Available')], default='other', max_length=50)),
            ],
            options={
                'verbose_name': 'Cuisine',
                'verbose_name_plural': 'Cuisines',
            },
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('clothing', 'Clothing'), ('fruit_veg', 'Fruit & Vegetable'), ('dairy', 'Dairy'), ('gadgets', 'Gadgets'), ('garage', 'Garage'), ('restaurant', 'Restaurant'), ('sweet_bakery', 'Sweet & Bakery'), ('medical', 'Medical Store'), ('grocery', 'Grocery Store'), ('beauty', 'Beauty Products'), ('electronics', 'Electronics'), ('books', 'Books'), ('toys', 'Toys'), ('sports', 'Sports & Outdoors'), ('pet_supplies', 'Pet Supplies'), ('home_decor', 'Home Decor'), ('automotive', 'Automotive'), ('jewelry', 'Jewelry'), ('health_fitness', 'Health & Fitness'), ('music', 'Music'), ('video_games', 'Video Games'), ('furniture', 'Furniture'), ('office_supplies', 'Office Supplies'), ('other', 'Other'), ('na', 'Not Available')], default='other', max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('size_unit', models.CharField(choices=[('ml', 'Milliliter'), ('kg', 'Kilogram'), ('large', 'Large'), ('medium', 'Medium'), ('small', 'Small'), ('half', 'Half'), ('full', 'Full'), ('other', 'Other'), ('na', 'Not Available')], default='other', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('INR', 'Rupees'), ('USD', 'US Dollar'), ('EUR', 'Euro')], default='INR', max_length=3)),
            ],
            options={
                'verbose_name': 'Product variation',
                'verbose_name_plural': 'Product variations',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alt_contact_number', models.CharField(default='', max_length=15)),
                ('alt_email', models.EmailField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=255)),
                ('gstin', models.CharField(default='', max_length=50)),
                ('category', models.CharField(choices=[('shop', 'Shop'), ('restaurant', 'Restaurant')], default='shop', max_length=25)),
                ('description', models.TextField(default='', max_length=2000)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_available_at', models.ManyToManyField(to='merchants.postalcode')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(default='', max_length=255)),
                ('address_line2', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('postal_code', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=50)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='business_documents/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])])),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='business_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png']), merchants.models.validate_image_dimensions])),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='business_logo/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png']), merchants.models.validate_image_dimensions])),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='owner_documents/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])])),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('product_code', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('description', models.TextField(default='')),
                ('meta_data', models.TextField(blank=True, default='', null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('categories', models.ManyToManyField(to='merchants.productcategory')),
                ('product_variant', models.ManyToManyField(to='merchants.productvariation')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png']), merchants.models.validate_image_dimensions])),
                ('is_trashed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.product')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='merchants.review')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('merchants.review',),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='merchants.review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product Review',
                'verbose_name_plural': 'Product Reviews',
            },
            bases=('merchants.review',),
        ),
        migrations.CreateModel(
            name='RestaurantProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='merchants.product')),
                ('preparation_time', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, null=True)),
                ('available_from', models.TimeField(blank=True, null=True)),
                ('available_until', models.TimeField(blank=True, null=True)),
                ('allergens', models.ManyToManyField(to='merchants.allergen')),
                ('cuisines', models.ManyToManyField(to='merchants.cuisine')),
            ],
            options={
                'verbose_name': 'Restaurant Product',
                'verbose_name_plural': 'Restaurant Products',
            },
            bases=('merchants.product',),
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='merchants.product')),
                ('brand', models.ManyToManyField(to='merchants.productbrand')),
            ],
            options={
                'verbose_name': 'Shop Product',
                'verbose_name_plural': 'Shop Products',
            },
            bases=('merchants.product',),
        ),
    ]