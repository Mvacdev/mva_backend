from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Button(models.Model):
    text = models.CharField(max_length=50, help_text='Text')
    url = models.URLField(max_length=500)


class MainScreenFeatureBlock(models.Model):
    def __str__(self):
        return f'MainScreenFeatureBlock {self.id}'


class MainScreenFeature(models.Model):
    block = models.ForeignKey(MainScreenFeatureBlock, on_delete=models.CASCADE, related_name='features')
    icon = models.ImageField(upload_to='main_page/icons/', help_text='Icon')
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
    icon = models.ImageField(upload_to='card/icons/', help_text='Icon', blank=True, null=True)
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
    rating_icon = models.ImageField(upload_to='icons/', help_text='Company icon', null=True, blank=True)
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


class FAQSection(models.Model):
    title = models.CharField(max_length=255, help_text='FAQ title')


class FAQItem(models.Model):
    section = models.ForeignKey(FAQSection, on_delete=models.CASCADE, related_name='items')
    category = models.CharField(max_length=50, choices=[('customer', 'Customer'), ('seller', 'Seller')], help_text='FAQ category', default="customer")
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
    text = models.TextField(help_text='Section text')


class Footer(models.Model):
    address = models.CharField(max_length=255, help_text='Address')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=20, help_text='Phone number')


class SocialLink(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='social_links')
    icon = models.ImageField(upload_to='main_page/social_icons/', help_text='Social media icon')
    url = models.URLField(help_text='Social media link')


class FooterNote(models.Model):
    footer = models.OneToOneField(Footer, on_delete=models.CASCADE, related_name='note')
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)], help_text='Rating (0-5)'
    )
    text = models.CharField(max_length=255, help_text='Footer note text')


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
    # BLOCKS
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

