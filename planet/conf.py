"""Planet configuration file."""


class PricingType:
    """Pricing Types."""
    HOURLY = 0
    DAILY = 1
    MONTHLY = 2
    QUARTERLY = 4
    SEMI_ANNUALLY = 5
    ANNUALLY = 6
    BIENNIALLY = 7
    TRIENNIALLY = 8


SECTION_TEMPLATES = (
    ('planet/cms/sections/feature_icon.html', 'Features with Icons'),
    ('planet/cms/sections/feature_images_title.html',
     'Feature with Images & and Title.'),
    ('planet/cms/sections/feature_images_title.html', 'Simple FAQ'),
    ('planet/cms/sections/feature_image.html', 'Features with Image')
)
