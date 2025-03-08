import re
import os

from bs4 import BeautifulSoup
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from trix_editor.fields import TrixEditorField

from apps.core.utils import get_min_read_time


def svg_validator(value):
    pass


def image_validator(value):
    ext = os.path.splitext(value.name)[1]  # Get file extension
    if ext.lower() not in [".svg", ".png", ".jpeg", "jpg"]:
        raise ValidationError("Only Image files are allowed.")


class TitleDescriptionBlock(models.Model):
    title = models.CharField(max_length=255, help_text='Page title')
    description = models.TextField(help_text='Page description')


class ImageBlock(models.Model):
    image = models.ImageField(upload_to='images/', help_text='Single image')


class Button(models.Model):
    text = models.CharField(max_length=50, help_text='Text')
    url = models.URLField(max_length=500)


class MainScreenFeatureBlock(models.Model):
    def __str__(self):
        return f'MainScreenFeatureBlock {self.id}'


class MainScreenFeature(models.Model):
    block = models.ForeignKey(MainScreenFeatureBlock, on_delete=models.CASCADE, related_name='features')
    icon = models.FileField(upload_to='main_page/icons/', help_text='Icon', validators=[image_validator])
    text = models.CharField(max_length=255, help_text='Text')


class MainSelect(models.Model):
    button = models.ForeignKey(Button, on_delete=models.SET_NULL, null=True, blank=True)


class MainSelectOption(models.Model):
    main_select = models.ForeignKey(MainSelect, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255, help_text='Text')


class CardSection(models.Model):
    title = models.CharField(max_length=255, help_text='Section title')
    is_hidden = models.BooleanField(default=False, help_text='Hide this section')


class Card(models.Model):
    section = models.ForeignKey(CardSection, on_delete=models.CASCADE, related_name='cards')
    icon = models.FileField(upload_to='card/icons/', help_text='Icon', blank=True, null=True, validators=[image_validator])
    subtitle = models.CharField(max_length=255, help_text='Subtitle', blank=True)
    text = models.TextField(help_text='Text')


class PricingSection(models.Model):
    title = models.CharField(max_length=255, help_text='Pricing section title')
    button = models.ForeignKey(Button, on_delete=models.SET_NULL, null=True, blank=True)


class PricingPlan(models.Model):
    section = models.ForeignKey(PricingSection, on_delete=models.CASCADE, related_name='plans')
    title = models.CharField(max_length=100, help_text='Plan title')


class PricingFeature(models.Model):
    plan = models.ForeignKey(PricingPlan, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=255, blank=True, null=True, help_text='Feature text')
    star_rating = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(3)], help_text='Star rating (1-3)'
    )


class BannerSection(models.Model):
    title = models.CharField(max_length=255, help_text='Banner title')
    text = models.TextField(help_text='Banner text')
    button = models.ForeignKey(Button, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='main_page/banners/', help_text='Banner image')


class CalculatorSection(models.Model):
    title = models.CharField(max_length=255, help_text='Calculator section title')
    background_image = models.ImageField(
        upload_to='main_page/calculator/',
        help_text='Background image',
        null=True, blank=True
        # validators=[lambda img: validate_image_size(img, 1440, 699)]
    )


class ReviewSection(models.Model):
    title = models.CharField(max_length=255, help_text='Section title')
    button = models.ForeignKey(Button, on_delete=models.SET_NULL, blank=True, null=True)
    # rating_title = models.CharField(max_length=25) ???
    rating_icon = models.FileField(upload_to='icons/', help_text='Company icon', null=True, blank=True, validators=[image_validator])
    rating_star = models.DecimalField(
        max_digits=2, decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text='Rating 0-5',
        null=True, blank=True
    )
    # Иконка: гугл – отметка(5.0)


class ReviewCard(models.Model):
    section = models.ForeignKey(ReviewSection, on_delete=models.CASCADE, related_name='review_cards')
    name = models.CharField(max_length=255, help_text='Name')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], help_text='Rating (0-5)')
    text = models.TextField(help_text='Review text')
    car_name = models.CharField(max_length=255, help_text='Car name')
    car_image = models.ImageField(
        upload_to='car_images/',
        help_text='Car image (165x165)',
        # validators=[lambda img: validate_image_size(img, 165, 165)]
    )


class YouTubeFeedSection(models.Model):
    title = models.CharField(max_length=255, help_text='Section title')
    subscriber_count = models.CharField(max_length=50, help_text='Subscriber count with label', blank=True)
    channel_link = models.URLField(help_text='YouTube channel link', blank=True)


class YouTubeVideo(models.Model):
    feed = models.ForeignKey(YouTubeFeedSection, on_delete=models.CASCADE, related_name='videos')
    preview_image = models.ImageField(upload_to='main_page/youtube_previews/', help_text='Video preview image', blank=True, null=True)
    title = models.CharField(max_length=255, help_text='Video title')
    views_info = models.CharField(max_length=255, help_text='Views and time info', blank=True)
    video_link = models.URLField(help_text='YouTube video link')
    duration = models.CharField(max_length=8, help_text='6:32 (for example)', blank=True)


class FAQSection(models.Model):
    title = models.CharField(max_length=255, help_text='FAQ title')


class FAQItem(models.Model):
    section = models.ForeignKey(FAQSection, on_delete=models.CASCADE, related_name='items')
    category = models.CharField(max_length=50, choices=[('customer', 'Customer'), ('seller', 'Seller')], help_text='FAQ category', default="customer")
    question = models.CharField(max_length=255, help_text='Question')
    answer = models.TextField(help_text='Answer')


class FAQAlternativeItem(models.Model):
    section = models.ForeignKey(FAQSection, on_delete=models.CASCADE, related_name='alternative_items')
    question = models.CharField(max_length=255, help_text='Question')
    answer = models.TextField(help_text='Answer')


class PartnerSection(models.Model):
    title = models.CharField(max_length=255, help_text='Section title')


class Partner(models.Model):
    section = models.ForeignKey(PartnerSection, on_delete=models.CASCADE, related_name='partners')
    name = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(
        upload_to='main_page/partners/',
        help_text='Partner logo (190x120)',
        # validators=[lambda img: validate_image_size(img, 190, 120)]
    )


class TitreSection(models.Model):
    title = models.CharField(max_length=255, help_text='Section title')
    # text = models.TextField(help_text='Section text')
    # text = TrixEditorField(max_length=10000, help_text='Section text')
    text = CKEditor5Field(max_length=20000, help_text='Section text')


class Footer(models.Model):
    address = models.CharField(max_length=255, help_text='Address')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=20, help_text='Phone number')
    phone_help_text = models.CharField(max_length=100, blank=True, help_text='(Lundy au bended, 9h-18h)')
    contacts_title = models.CharField(max_length=100, blank=True, help_text='Pour un contact rapide, voici nos informations :')


class SocialLink(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='social_links')
    icon = models.FileField(upload_to='main_page/social_icons/', help_text='Social media icon', validators=[image_validator])
    url = models.URLField(help_text='Social media link')


class FooterNote(models.Model):
    footer = models.OneToOneField(Footer, on_delete=models.CASCADE, related_name='note')
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)], help_text='Rating (0-5)'
    )
    text = models.CharField(max_length=255, help_text='Footer note text')


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Unique tag name')

    def __str__(self):
        return self.name


class MainPage(models.Model):
    # ---- MetaInfo -----
    seo_title = models.CharField(max_length=100, help_text='SEO Title', blank=True)
    seo_description = models.CharField(max_length=500, help_text='SEO Description', blank=True)
    # ---- MainScreen section -----
    background_image = models.ImageField(upload_to='main_page/backgrounds/', help_text='Background image', blank=True, null=True, default=None)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text='Rating 0.0-5.0',
        blank=True, null=True
    )
    title = models.CharField(max_length=255, help_text='Main page title', blank=True)
    video_url = models.URLField(help_text='Video URL', blank=True)
    video_text = models.CharField(max_length=255, help_text='Video text', blank=True)
    video_preview = models.ImageField(upload_to='main_page/video_previews/', help_text='Video preview img', blank=True, null=True)
    # ***** BLOCKS ******
    main_screen_feature_block = models.OneToOneField(MainScreenFeatureBlock, on_delete=models.SET_NULL, blank=True, null=True)
    main_screen_select = models.OneToOneField(MainSelect, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- MarketingSection ----- OK
    marketing_section = models.OneToOneField(CardSection, on_delete=models.SET_NULL, blank=True, null=True, related_name='main_page_marketing')
    # ---- FeatureSection ----- OK
    feature_section = models.OneToOneField(CardSection, on_delete=models.SET_NULL, blank=True, null=True, related_name='main_page_feature')
    # ---- StepsSection -----
    steps_section = models.OneToOneField(CardSection, on_delete=models.SET_NULL, blank=True, null=True, related_name='main_page_steps')
    # ---- PricingSection -----
    pricing_section = models.OneToOneField(PricingSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- BannerSection -----
    banner_section = models.OneToOneField(BannerSection, on_delete=models.SET_NULL, blank=True, null=True, related_name='banner_section_1')
    # ---- CalculatorSection -----
    calculator_section = models.OneToOneField(CalculatorSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- WhyChoseUsSection -----
    why_chose_us_section = models.OneToOneField(CardSection, on_delete=models.SET_NULL, blank=True, null=True, related_name='main_page_why_chose_us')
    # ---- ReviewSection -----
    review_section = models.OneToOneField(ReviewSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- YouTubeFeedSection -----
    youtube_feed_section = models.OneToOneField(YouTubeFeedSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- FAQSection -----
    faq_section = models.OneToOneField(FAQSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- PartnerSection -----
    partner_section = models.OneToOneField(PartnerSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- TitreSection -----
    titre_section = models.OneToOneField(TitreSection, on_delete=models.SET_NULL, blank=True, null=True)
    #  ---- BannerSection -----
    banner_section_2 = models.OneToOneField(BannerSection, on_delete=models.SET_NULL, blank=True, null=True, related_name='banner_section_2')
    #  ---- Footer -----
    footer = models.OneToOneField(Footer, on_delete=models.SET_NULL, blank=True, null=True)


class InfoPage(models.Model):
    # ---- MetaInfo -----
    seo_title = models.CharField(max_length=100, help_text='SEO Title', blank=True)
    seo_description = models.CharField(max_length=500, help_text='SEO Description', blank=True)
    # ***** BLOCKS ******
    title_desc_block = models.OneToOneField(TitleDescriptionBlock, on_delete=models.SET_NULL, blank=True, null=True)
    image_block = models.OneToOneField(ImageBlock, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- FAQSection -----
    faq_section = models.OneToOneField(FAQSection, on_delete=models.SET_NULL, blank=True, null=True)
    #  ---- Footer -----
    footer = models.OneToOneField(Footer, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        abstract = True


class ContactPage(InfoPage):
    pass


class EstimationPage(InfoPage):
    pass


class TitrePage(models.Model):
    # ---- MetaInfo -----
    seo_title = models.CharField(max_length=100, help_text='SEO Title', blank=True)
    seo_description = models.CharField(max_length=500, help_text='SEO Description', blank=True)
    # ***** BLOCKS ******
    # ---- TitreSection -----
    titre_section = models.OneToOneField(TitreSection, on_delete=models.SET_NULL, blank=True, null=True)
    #  ---- Footer -----
    footer = models.OneToOneField(Footer, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        abstract = True


class PoliticsPage(TitrePage):
    pass


class CookiesPage(TitrePage):
    pass


class MentionPage(TitrePage):
    pass


class Franchises(InfoPage):
    why_need_franchise = models.OneToOneField(CardSection, on_delete=models.SET_NULL, blank=True, null=True)
    banner = models.OneToOneField(BannerSection, on_delete=models.SET_NULL, blank=True, null=True)


class BlogPage(models.Model):
    # ---- MetaInfo -----
    seo_title = models.CharField(max_length=100, help_text='SEO Title', blank=True)
    seo_description = models.CharField(max_length=500, help_text='SEO Description', blank=True)
    # ---- General
    title_desc_block = models.OneToOneField(TitleDescriptionBlock, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- YouTubeFeedSection -----
    youtube_feed_section = models.OneToOneField(YouTubeFeedSection, on_delete=models.SET_NULL, blank=True, null=True)
    # ---- ReviewSection -----
    review_section = models.OneToOneField(ReviewSection, on_delete=models.SET_NULL, blank=True, null=True)
    #  ---- Footer -----
    footer = models.OneToOneField(Footer, on_delete=models.SET_NULL, blank=True, null=True)
    # TODO: Put into Article page ------------
    # ---- Why Chose Us -----
    why_chose_us_section = models.OneToOneField(CardSection, on_delete=models.SET_NULL, blank=True, null=True)
    #  ---- BannerSection -----
    banner_section = models.OneToOneField(BannerSection, on_delete=models.SET_NULL, blank=True, null=True)


class Article(models.Model):
    blog = models.ForeignKey(BlogPage, on_delete=models.CASCADE, related_name="articles")
    # ---- MetaInfo -----
    # seo_title = models.CharField(max_length=100, help_text='SEO Title', blank=True)
    # seo_description = models.CharField(max_length=500, help_text='SEO Description', blank=True)
    # ---- General
    title = models.CharField(max_length=100, help_text='Article title')
    description = models.TextField(max_length=1000, blank=True)
    main_img = models.ImageField(upload_to='blog/images/', help_text='Article main image')
    text = TrixEditorField(max_length=5000, help_text='Article text', blank=True)
    parsed_text = models.TextField(max_length=5000, help_text='Parsed article text', blank=True)
    read_time = models.PositiveSmallIntegerField(default=0, help_text='Article read time in minutes')
    author = models.CharField(max_length=50, help_text='The author of the article')
    pub_date = models.DateTimeField(default=timezone.now, help_text='Publication date')
    tags = models.ManyToManyField(Tag, related_name="articles", blank=True)
    plan = models.TextField(max_length=5000, blank=True, help_text='Article plan')

    def parse_editor_text(self, editor_text):
        # Создаем объект BeautifulSoup для удобной работы с HTML
        soup = BeautifulSoup(editor_text, 'html.parser')

        # Найдем все заголовки h1 и обработаем их
        sections = []
        section_id = 1
        for h1 in soup.find_all('h1'):
            # Извлекаем текст заголовка (например "1. Préparation correcte du véhicule")
            title = h1.get_text(strip=True)
            section_title = title.split(' ', 1)[1] if len(title.split(' ', 1)) > 1 else title
            section_id_str = f"section{section_id}"

            # Ищем следующий блок текста, который идет после заголовка
            next_div = h1.find_next('div')
            section_content = next_div.get_text(separator=" ", strip=True) if next_div else ''

            # Формируем HTML для текущего раздела
            section_html = f'''
            <section class="post__section" id="{section_id_str}">
              <h2>{section_title}</h2>
              <p>{section_content}</p>
            '''

            # Ищем возможные изображения в блоках figure и добавляем их в отдельную секцию
            images = []
            for figure in next_div.find_all('figure'):
                img = figure.find('img')
                if img:
                    img_src = img.get('src', '')
                    img_alt = img.get('alt', '')
                    caption = figure.find('figcaption').get_text(strip=True) if figure.find('figcaption') else ''
                    images.append({
                        'src': img_src,
                        'alt': img_alt,
                        'caption': caption
                    })

            # Если есть изображения, добавляем их в отдельную секцию
            for image in images:  # <figcaption>{image['caption']}</figcaption>
                section_html += f'''
                </section>
                <section class="post__section">
                  <div class="post__image">
                    <img class="post__image-elem" src="http://206.81.17.158{image['src']}" alt="{image['alt']}">
                  </div>
                </section>
                <section class="post__section">
                '''
            section_html += '</section>'
            sections.append(section_html)
            section_id += 1

        # Теперь формируем итоговый HTML с добавленными секциями
        post_html = "\n".join(sections)

        return post_html

    # def extract_plan_and_update_text(self):
    #     """Finds h2 headings, creates anchors and updates article text."""
    #     soup = BeautifulSoup(self.text, "html.parser")
    #     plan = []
    #
    #     for h1 in soup.find_all("h1"):
    #         title = h1.get_text(strip=True)
    #         anchor = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')
    #         h1["id"] = anchor
    #         plan.append({"title": title, "anchor": f"#{anchor}"})
    #
    #     return plan, str(soup)

    def generate_toc(self, parsed_text):
        # Ищем все секции с id и заголовками
        sections = re.findall(r'<section class="post__section" id="([^"]+)">.*?<h2>(.*?)</h2>', parsed_text, re.DOTALL)

        # Формируем таблицу содержания
        toc = '<section class="post__toc">\n  <h2 class="post__toc-title">Plan de l’article</h2>\n  <ul class="post__toc-list">'

        for section in sections:
            section_id, title = section
            toc += f'\n    <li class="post__toc-item">\n      <a href="#{section_id}">{title}</a>\n    </li>'

        toc += '\n  </ul>\n</section>'

        return toc

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.read_time = get_min_read_time(self.text)
        # self.plan, self.text = self.extract_plan_and_update_text()
        self.parsed_text = self.parse_editor_text(self.text)
        self.plan = self.generate_toc(self.parsed_text)
        # if not self.seo_title:
        #     self.seo_title = self.title
        # if not self.seo_description:
        #     self.seo_description = self.description
        super().save(*args, **kwargs)
