THEME = "."
AUTHOR = "julz"
SITENAME = "Another GitHub Blog"
SITEURL = "https://julzhk.github.io"
PATH = "content"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_SOURCES = True
TYPOGRIFY = True
TYPOGRIFY_DASHES = "oldschool"
TIMEZONE = "Canada/Atlantic"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = 10
CATEGORIES_SAVE_AS = "categories/index.html"
CATEGORIES_URL = "categories/"
TAGS_SAVE_AS = "tags/index.html"
TAGS_URL = "tags/"
AUTHORS_SAVE_AS = "authors/index.html"
AUTHORS_URL = "authors/"
ARCHIVES_SAVE_AS = "archives/index.html"
ARCHIVES_URL = "archives/"
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_URL = "https://github.com/julzhk/github-blog"
DEFAULT_CATEGORY = "Tech"

FEED_DOMAIN = SITEURL

# Make the URLs of article permalink pages nicer.
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SOURCE_URL = "{article.url}index{OUTPUT_SOURCES_EXTENSION}"

# Make the URLs of period archive pages nicer.
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
DAY_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/index.html"
DAY_ARCHIVE_URL = "{date:%Y}/{date:%m}/{date:%d}/"

# Make the URLs of static pages nicer.
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SOURCE_URL = "{page.url}index{OUTPUT_SOURCES_EXTENSION}"

LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Oatcake", "https://github.com/seanh/oatcake"),
    ("GitHub", "https://github.com/seanh/sidecar"),
)

SOCIAL = [
    ("Mastodon", "https://mastodon.social/@seanh"),
    ("Pinboard", "https://pinboard.in/u:seanh"),
]

SIDECAR_MENU = [
    "HOME",
    "MENUITEMS",
    "PAGES",
    "TAGS",
    "ARCHIVES",
]

SIDECAR_TAGLINE = [
    "TIME",
    "AUTHORS",
    "TAGS",
]
