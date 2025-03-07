from rest_framework import serializers

from rest_framework import serializers
from apps.integration.models import (
    MainPage, MainScreenFeatureBlock, MainScreenFeature, MainSelect, MainSelectOption,
    CardSection, Card, PricingSection, PricingPlan, PricingFeature, BannerSection,
    CalculatorSection, ReviewSection, ReviewCard, YouTubeFeedSection, YouTubeVideo,
    FAQSection, FAQItem, PartnerSection, Partner, TitreSection, Footer, SocialLink,
    FooterNote, Button, ContactPage, EstimationPage, Franchises, TitleDescriptionBlock, ImageBlock, Tag, Article,
    BlogPage
)

# class MainPageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MainPage
#         fields = '__all__'
#         depth = 2


class MainScreenFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainScreenFeature
        fields = '__all__'


class MainScreenFeatureBlockSerializer(serializers.ModelSerializer):
    features = MainScreenFeatureSerializer(many=True)

    class Meta:
        model = MainScreenFeatureBlock
        fields = '__all__'


class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = '__all__'


class MainSelectOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainSelectOption
        fields = '__all__'


class MainSelectSerializer(serializers.ModelSerializer):
    options = MainSelectOptionSerializer(many=True)
    button = ButtonSerializer()

    class Meta:
        model = MainSelect
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardSectionSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = CardSection
        fields = '__all__'


class PricingFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingFeature
        fields = '__all__'


class PricingPlanSerializer(serializers.ModelSerializer):
    features = PricingFeatureSerializer(many=True)

    class Meta:
        model = PricingPlan
        fields = '__all__'


class PricingSectionSerializer(serializers.ModelSerializer):
    plans = PricingPlanSerializer(many=True)
    button = ButtonSerializer()

    class Meta:
        model = PricingSection
        fields = '__all__'


class BannerSectionSerializer(serializers.ModelSerializer):
    button = ButtonSerializer()

    class Meta:
        model = BannerSection
        fields = '__all__'


class CalculatorSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorSection
        fields = '__all__'


class ReviewCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCard
        fields = '__all__'


class ReviewSectionSerializer(serializers.ModelSerializer):
    review_cards = ReviewCardSerializer(many=True)
    button = ButtonSerializer()

    class Meta:
        model = ReviewSection
        fields = '__all__'


class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = '__all__'


class YouTubeFeedSectionSerializer(serializers.ModelSerializer):
    videos = YouTubeVideoSerializer(many=True)

    class Meta:
        model = YouTubeFeedSection
        fields = '__all__'


class FAQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = '__all__'


class FAQSectionSerializer(serializers.ModelSerializer):
    items = FAQItemSerializer(many=True)

    class Meta:
        model = FAQSection
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class PartnerSectionSerializer(serializers.ModelSerializer):
    partners = PartnerSerializer(many=True)

    class Meta:
        model = PartnerSection
        fields = '__all__'


class FooterNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterNote
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class TitreSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitreSection
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)
    note = FooterNoteSerializer()

    class Meta:
        model = Footer
        fields = '__all__'


class TitleDescriptionBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleDescriptionBlock
        fields = '__all__'


class ImageBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBlock
        fields = '__all__'


class MainPageSerializer(serializers.ModelSerializer):
    main_screen_feature_block = MainScreenFeatureBlockSerializer()
    main_screen_select = MainSelectSerializer()
    marketing_section = CardSectionSerializer()
    feature_section = CardSectionSerializer()
    steps_section = CardSectionSerializer()
    pricing_section = PricingSectionSerializer()
    banner_section = BannerSectionSerializer()
    calculator_section = CalculatorSectionSerializer()
    why_chose_us_section = CardSectionSerializer()
    review_section = ReviewSectionSerializer()
    youtube_feed_section = YouTubeFeedSectionSerializer()
    faq_section = FAQSectionSerializer()
    partner_section = PartnerSectionSerializer()
    titre_section = TitreSectionSerializer()
    banner_section_2 = BannerSectionSerializer()
    footer = FooterSerializer()

    class Meta:
        model = MainPage
        fields = '__all__'


class ContactPageSerializer(serializers.ModelSerializer):
    title_desc_block = TitleDescriptionBlockSerializer()
    image_block = ImageBlockSerializer()
    faq_section = FAQSectionSerializer()
    footer = FooterSerializer()

    class Meta:
        model = ContactPage
        fields = '__all__'


class EstimationPageSerializer(serializers.ModelSerializer):
    title_desc_block = TitleDescriptionBlockSerializer()
    image_block = ImageBlockSerializer()
    faq_section = FAQSectionSerializer()
    footer = FooterSerializer()

    class Meta:
        model = EstimationPage
        fields = '__all__'


class FranchisesSerializer(serializers.ModelSerializer):
    title_desc_block = TitleDescriptionBlockSerializer()
    why_need_franchise = CardSectionSerializer()
    image_block = ImageBlockSerializer()
    faq_section = FAQSectionSerializer()
    banner = BannerSectionSerializer()
    footer = FooterSerializer()

    class Meta:
        model = Franchises
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'main_img', 'text', 'read_time', 'author', 'pub_date', 'tags', 'plan']


class BlogPageSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(read_only=True, many=True)
    title_desc_block = TitleDescriptionBlockSerializer()
    youtube_feed_section = YouTubeFeedSectionSerializer()
    review_section = ReviewSectionSerializer()
    footer = FooterSerializer()
    all_tags = serializers.SerializerMethodField()
    why_chose_us_section = CardSectionSerializer()
    banner_section = BannerSectionSerializer()

    class Meta:
        model = BlogPage
        fields = [
            'id', 'seo_title', 'seo_description', 'title_desc_block', 'youtube_feed_section', 'review_section', 'footer',
            'all_tags', 'why_chose_us_section', 'banner_section'
        ]

    def get_all_tags(self, obj):
        return Tag.objects.values_list('name', flat=True)
