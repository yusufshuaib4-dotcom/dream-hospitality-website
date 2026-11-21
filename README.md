# Dream Hospitality website

A static, responsive company website hosted on GitHub Pages at https://yusufshuaib4-dotcom.github.io/dream-hospitality-website/.

## Update content

The five main pages and sitemap are generated from `_build/build.py`:

```
python3 _build/build.py
```

Shared styling lives in `assets/css/style.css` and mobile navigation in `assets/js/main.js`. The privacy draft and 404 page are edited directly. GitHub Pages excludes `_build/` from the published site.

## Brand

The purple circular company logo supplied on 21 November 2026 is used unchanged in `assets/img/dream-hospitality-logo.jpeg`. The design uses purple, lavender, black and white. The favicon interprets its circular rings and star for small displays; the social preview is `assets/img/og-purple.png`.

## Content boundaries

Products remain in development, with first modules planned for 2027. Planned capabilities may change. The public site uses the TRX business address and company registration number. It excludes private identity, tax, financial, residential and registered-address information from the company profile.

Company confirmation is still needed for email, telephone, domain and final content. No enquiry form or analytics is enabled. `privacy-notice.html` remains an unapproved English/Malay draft, unlinked with `noindex, nofollow`; its direct URL is still publicly accessible. Approval of that notice and a responsible contact are needed before adding a form.

## Hosting

GitHub Pages publishes `main` from the repository root. When changing the domain, update `SITE` in the generator, `robots.txt`, and the absolute base paths in `404.html`, then rebuild.
