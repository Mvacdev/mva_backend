from rest_framework import serializers

from rest_framework import serializers
from apps.integration.models import (
    MainPage, MainScreenFeatureBlock, MainScreenFeature, MainSelect, MainSelectOption,
    CardSection, Card, PricingSection, PricingPlan, PricingFeature, BannerSection,
    CalculatorSection, ReviewSection, ReviewCard, YouTubeFeedSection, YouTubeVideo,
    FAQSection, FAQItem, PartnerSection, Partner, TitreSection, Footer, SocialLink,
    FooterNote
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


class MainSelectOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSelectOption
        fields = '__all__'


class MainSelectSerializer(serializers.ModelSerializer):
    options = MainSelectOptionSerializer(many=True)

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

    class Meta:
        model = PricingSection
        fields = '__all__'


class BannerSectionSerializer(serializers.ModelSerializer):
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
