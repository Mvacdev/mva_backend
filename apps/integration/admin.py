from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedModelAdmin

from .models import (
    Button, MainScreenFeatureBlock, MainScreenFeature, MainSelect, MainSelectOption, CardSection, Card,
    PricingSection, PricingPlan, PricingFeature, BannerSection, CalculatorSection, ReviewSection,
    ReviewCard, YouTubeFeedSection, YouTubeVideo, FAQSection, FAQItem, PartnerSection, Partner,
    TitreSection, Footer, SocialLink, FooterNote, MainPage
)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'title']
    list_display = ('id', 'title', 'background_image', 'rating', 'video_url')
    # raw_id_fields = ['main_screen_feature_block']

    fieldsets = (
        ('MetaInfo', {'fields': (
            'seo_title', 'seo_description',
        )}),
        ('Main Screen Section', {'fields': (
            'background_image', 'rating', 'title', 'video_url', 'video_text', 'video_preview',
        )}),
        ('Blocks', {'fields': (
            'main_screen_feature_block', 'main_screen_select', 'marketing_section', 'feature_section', 'steps_section',
            'pricing_section', 'banner_section', 'calculator_section', 'why_chose_us_section', 'review_section',
            'youtube_feed_section', 'faq_section', 'partner_section', 'titre_section', 'banner_section_2'
        )}),
        ('Footer', {'fields': (
            'footer',
        )}),
    )


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('text', 'url')


class MainScreenFeatureInline(admin.TabularInline):  # TODO: INLINE
    fields = ('icon', 'text')
    model = MainScreenFeature
    extra = 0


@admin.register(MainScreenFeatureBlock)
class MainScreenFeatureBlockAdmin(admin.ModelAdmin):
    list_display = ('id',)
    inlines = [MainScreenFeatureInline]


@admin.register(MainScreenFeature)
class MainScreenFeatureAdmin(admin.ModelAdmin):
    list_display = ('block', 'icon', 'text')


class MainSelectOptionInline(admin.TabularInline):  # TODO: INLINE
    fields = ('main_select', 'text')
    model = MainSelectOption
    extra = 0


@admin.register(MainSelect)
class MainSelectAdmin(admin.ModelAdmin):
    list_display = ('button',)
    inlines = [MainSelectOptionInline]


@admin.register(MainSelectOption)
class MainSelectOptionAdmin(admin.ModelAdmin):
    list_display = ('main_select', 'text')


class CardInline(admin.TabularInline):  # TODO: INLINE
    list_display = ('section', 'icon', 'subtitle', 'text')
    model = Card
    extra = 0


@admin.register(CardSection)
class CardSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_hidden')
    inlines = [CardInline]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('section', 'icon', 'subtitle', 'text')


class PricingFeatureInline(NestedTabularInline):
    list_display = ('text', 'star_rating')
    model = PricingFeature
    extra = 0


class PricingPlanInline(NestedTabularInline):
    list_display = ('title',)
    model = PricingPlan
    inlines = [PricingFeatureInline]
    extra = 0


@admin.register(PricingSection)
class PricingSectionAdmin(NestedModelAdmin):
    list_display = ('title', 'button')
    inlines = [PricingPlanInline]


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('section', 'title')


@admin.register(PricingFeature)
class PricingFeatureAdmin(admin.ModelAdmin):
    list_display = ('plan', 'text', 'star_rating')


@admin.register(BannerSection)
class BannerSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'button', 'image')


@admin.register(CalculatorSection)
class CalculatorSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'background_image')


class ReviewCardInline(admin.TabularInline):
    list_display = ('name', 'rating', 'text', 'car_name', 'car_image')
    model = ReviewCard
    extra = 0


@admin.register(ReviewSection)
class ReviewSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button', 'rating_icon', 'rating_star')
    inlines = [ReviewCardInline]


@admin.register(ReviewCard)
class ReviewCardAdmin(admin.ModelAdmin):
    list_display = ('section', 'name', 'rating', 'text', 'car_name', 'car_image')


class YouTubeVideoInline(admin.TabularInline):
    list_display = ('preview_image', 'title', 'views_info', 'video_link')
    model = YouTubeVideo
    extra = 0


@admin.register(YouTubeFeedSection)
class YouTubeFeedSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subscriber_count', 'channel_link')
    inlines = [YouTubeVideoInline]


@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('feed', 'preview_image', 'title', 'views_info', 'video_link')


class FAQItemInline(admin.TabularInline):
    list_display = ('category', 'question', 'answer')
    model = FAQItem
    extra = 0


@admin.register(FAQSection)
class FAQSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [FAQItemInline]


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('section', 'category', 'question', 'answer')


class PartnerInline(admin.TabularInline):
    list_display = ('name', 'logo')
    model = Partner
    extra = 0


@admin.register(PartnerSection)
class PartnerSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [PartnerInline]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('section', 'name', 'logo')


@admin.register(TitreSection)
class TitreSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


class SocialLinkInline(admin.TabularInline):
    list_display = ('icon', 'url')
    model = SocialLink
    extra = 0


class FooterNoteInline(admin.TabularInline):
    list_display = ('rating', 'text')
    model = FooterNote
    extra = 0


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')
    inlines = [SocialLinkInline, FooterNoteInline]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('footer', 'icon', 'url')


@admin.register(FooterNote)
class FooterNoteAdmin(admin.ModelAdmin):
    list_display = ('footer', 'rating', 'text')
