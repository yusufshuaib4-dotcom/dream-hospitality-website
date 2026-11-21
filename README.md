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

## Product details and property briefs

Four detail pages expand the planned product scope, with use cases, example journeys and FAQs. They are generated from `_build/enhancements.py`. The contact page includes a browser-only property brief builder with copy/download options. It sends no data and stores no answers.

`_build/site-config.json` holds the confirmed contact email/phone and privacy readiness. These are currently unset. The enquiry-email form is implemented but not displayed until the recipient email, approved privacy notice and privacy contact are confirmed. It prepares an email for the visitor to review and send in their own email app; it is not a server-delivered form. Before enabling it, replace the privacy draft's unresolved fields and approval status, and add its footer link. Automatic email delivery would require selecting and connecting a form service.

The crisp company logo is `assets/img/dream-hospitality-logo.svg`; the original supplied JPEG is retained. No domain settings were changed.
