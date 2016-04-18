# good-clean-read

source: https://github.com/hemangsk/Gravity

This is a one page site.

Put this in your `pelicanconf.py`:

```python
DEFAULT_PAGINATION = False

ARTICLE_SAVE_AS = ""
DRAFT_SAVE_AS = ""
PAGE_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
YEAR_ARCHIVE_SAVE_AS = ""
MONTH_ARCHIVE_SAVE_AS = ""
DAY_ARCHIVE_SAVE_AS = ""
```

Article title is shown as `h3` heading. For the content you should use smaller headings.

## TODO

* Add HTML anchor to article titles