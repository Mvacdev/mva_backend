# Generated by Django 4.2.19 on 2025-03-03 16:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import trix_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0005_remove_contactpage_background_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Unique tag name', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, help_text='SEO Title', max_length=100)),
                ('seo_description', models.CharField(blank=True, help_text='SEO Description', max_length=500)),
                ('footer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.footer')),
                ('review_section', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.reviewsection')),
                ('title_desc_block', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.titledescriptionblock')),
                ('youtube_feed_section', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.youtubefeedsection')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Article title', max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('main_img', models.ImageField(help_text='Article main image', upload_to='blog/images/')),
                ('text', trix_editor.fields.TrixEditorField(blank=True, help_text='Article text', max_length=5000)),
                ('read_time', models.PositiveSmallIntegerField(default=0, help_text='Article read time in minutes')),
                ('author', models.CharField(help_text='The author of the article', max_length=50)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Publication date')),
                ('plan', models.JSONField(blank=True, default=list, help_text='Article plan')),
                ('tags', models.ManyToManyField(blank=True, related_name='articles', to='integration.tag')),
                ('why_chose_us_section', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.cardsection')),
            ],
        ),
    ]
