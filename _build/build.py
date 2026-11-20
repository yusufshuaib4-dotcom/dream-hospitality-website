#!/usr/bin/env python3
"""Builds the Dream Hospitality site pages.

Shared <head>, header and footer live here so every page stays consistent.
Edit page content below, then run:  python3 _build/build.py
(The _build folder is not published: GitHub Pages/Jekyll skips folders starting with "_".)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# SITE URL: interim GitHub Pages address. Replace with the company domain once confirmed
# (also update robots.txt and the base path in 404.html).
SITE = "https://yusufshuaib4-dotcom.github.io/dream-hospitality-website/"
COMPANY = "Dream Hospitality Sdn. Bhd."
REG = "202601013644 (1675742-D)"
ADDRESS_LINE = "Suite T-77, Exchange 106, Lingkaran TRX, 55188 Kuala Lumpur, Malaysia"
LASTMOD = "2026-11-20"

NAV = [
    ("index.html", "Home"),
    ("products.html", "Products"),
    ("consultancy.html", "Consultancy"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

ICONS = {
    "booking": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 15h3"/></svg>',
    "checkin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2.5"/><circle cx="12" cy="11" r="3"/><path d="M12 14v3"/></svg>',
    "guest": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M9 11h6M9 14h4"/></svg>',
    "pms": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18a4 4 0 0 1-.6-8A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9z"/><path d="M9 14h6"/></svg>',
    "assess": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    "select": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    "implement": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
    "support": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="2" y="14" width="5" height="6" rx="1.5"/><rect x="17" y="14" width="5" height="6" rx="1.5"/></svg>',
}


def icon(name):
    return f'<div class="icon" aria-hidden="true">{ICONS[name]}</div>'


def head(page, title, description):
    url = SITE if page == "index.html" else SITE + page
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#FBF8F2" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0E1617" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Dream Hospitality">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Dream Hospitality: hospitality software and IT services, Kuala Lumpur">
  <meta property="og:locale" content="en_MY">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="assets/img/mark.svg" type="image/svg+xml">
  <link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="stylesheet" href="assets/css/style.css">"""


ORG_JSONLD = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "{COMPANY}",
    "legalName": "DREAM HOSPITALITY SDN. BHD.",
    "url": "{SITE}",
    "logo": "{SITE}assets/img/apple-touch-icon.png",
    "identifier": "{REG}",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Suite T-77, Exchange 106, Lingkaran TRX",
      "postalCode": "55188",
      "addressLocality": "Kuala Lumpur",
      "addressRegion": "Wilayah Persekutuan Kuala Lumpur",
      "addressCountry": "MY"
    }}
  }}
  </script>"""


def header(page):
    current = ' aria-current="page"'
    items = "\n".join(
        f'        <li><a href="{href}"{current if href == page else ""}>{label}</a></li>'
        for href, label in NAV
    )
    return f"""
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <nav class="wrap nav" aria-label="Main">
      <a class="brand" href="index.html" aria-label="Dream Hospitality, home">
        <!-- PLACEHOLDER: swap for the approved logo when supplied -->
        <img src="assets/img/mark.svg" alt="" width="34" height="34">
        <span>Dream Hospitality</span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
      <ul class="nav-links" id="nav-links">
{items}
      </ul>
    </nav>
  </header>
"""


def footer():
    links = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for h, l in NAV[1:])
    return f"""
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <p class="footer-company">{COMPANY}</p>
        <p>Registration No. {REG}</p>
        <p>{ADDRESS_LINE}</p>
      </div>
      <nav aria-label="Footer">
        <ul class="footer-links">
{links}
        </ul>
      </nav>
      <div>
        <p>&copy; <span id="year">2026</span> {COMPANY} All rights reserved.</p>
        <!-- PRIVACY: link the notice here once approved: <p><a href="privacy-notice.html">Privacy Notice / Notis Privasi</a></p> -->
      </div>
    </div>
  </footer>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(label, title, lead):
    return f"""
    <section class="page-hero">
      <div class="wrap">
        <span class="eyebrow">{label}</span>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>"""


def cta_band(title="Let's talk about your property", text="Tell us about your property and the technology challenges you face. We'd like to hear from you.", btn="Contact us"):
    return f"""
    <section class="section">
      <div class="wrap">
        <div class="cta-band">
          <div>
            <h2>{title}</h2>
            <p>{text}</p>
          </div>
          <a class="btn btn-light" href="contact.html">{btn}</a>
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------- pages
PAGES = {}

PAGES["index.html"] = dict(
    title="Dream Hospitality | Hospitality software and IT services, Kuala Lumpur",
    description="Dream Hospitality Sdn. Bhd. develops booking, contactless check-in, guest experience and cloud property management software for hotels, resorts and vacation rental operators, and provides IT consultancy and support to hospitality businesses in Malaysia.",
    jsonld=True,
    body=f"""
    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <span class="eyebrow">Hospitality technology · Kuala Lumpur</span>
          <h1>Practical software for hotels, resorts and vacation rentals.</h1>
          <p class="lead">Dream Hospitality develops booking, check-in, guest experience and property management software for independent and boutique properties, and provides IT consultancy and support to hospitality businesses in Malaysia.</p>
          <div class="cta-row">
            <a class="btn btn-primary" href="contact.html">Talk to us</a>
            <a class="btn btn-ghost" href="products.html">See what we're building</a>
          </div>
        </div>
        <aside class="hero-card" aria-labelledby="hero-card-title">
          <h2 id="hero-card-title">Our product suite</h2>
          <ul>
            <li><span>AI-powered booking system</span><span class="tag">In development</span></li>
            <li><span>Contactless check-in</span><span class="tag">In development</span></li>
            <li><span>Guest experience app</span><span class="tag">In development</span></li>
            <li><span>Cloud property management</span><span class="tag">In development</span></li>
          </ul>
          <p class="note" style="margin:14px 0 0">First modules planned for launch in 2027.</p>
        </aside>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <div class="section-head">
          <span class="label">What we do</span>
          <h2>Software and support for hospitality businesses</h2>
          <p>We work in two areas: building software for hotels and rental operators, and helping hospitality businesses choose, set up and run their technology.</p>
        </div>
        <div class="grid grid-2">
          <a class="card card-link" href="products.html">
            <div class="card-top">{icon("pms")}<span class="tag">In development</span></div>
            <h3>Hospitality software</h3>
            <p>Booking, contactless check-in, a guest experience app and a cloud property management system: four connected modules offered mainly as subscriptions.</p>
            <span class="more">Explore products <span aria-hidden="true">→</span></span>
          </a>
          <a class="card card-link" href="consultancy.html">
            <div class="card-top">{icon("support")}</div>
            <h3>IT consultancy and support</h3>
            <p>Technology assessments, system selection, implementation and ongoing IT support for hospitality businesses.</p>
            <span class="more">About our consultancy <span aria-hidden="true">→</span></span>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="label">Who we serve</span>
          <h2>Built for independent operators and growing groups</h2>
          <p>Our focus is the Malaysian hospitality market, with plans to serve operators across Southeast Asia as we grow.</p>
        </div>
        <div class="grid grid-3">
          <div class="card">
            <h3>Independent and boutique hotels and resorts</h3>
            <p>Properties that want more direct bookings and simpler operations without enterprise-level complexity.</p>
          </div>
          <div class="card">
            <h3>Vacation rental and serviced apartment operators</h3>
            <p>Operators managing multiple units who need smooth self check-in and guest communication.</p>
          </div>
          <div class="card">
            <h3>Small and mid-sized hotel groups</h3>
            <p>Groups that need consistent systems, reporting and support across several properties.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap split">
        <div>
          <span class="label">Our approach</span>
          <h2>What we're building toward</h2>
          <p>Our work is guided by three outcomes for the properties we serve, delivered with local support.</p>
          <p><a href="about.html">More about us <span aria-hidden="true">→</span></a></p>
        </div>
        <ul class="checks">
          <li><strong>More direct bookings.</strong> Tools that help properties take bookings through their own channels.</li>
          <li><strong>Simpler operations.</strong> Fewer manual steps at the front desk and in housekeeping.</li>
          <li><strong>Better guest experience.</strong> Faster arrivals and easier communication before, during and after a stay.</li>
        </ul>
      </div>
    </section>
{cta_band()}""",
)


def product(id_, ic, name, summary, features):
    feats = "\n".join(f"              <li>{f}</li>" for f in features)
    return f"""
        <article class="product" id="{id_}">
          <div class="product-intro">
            <div class="card-top">{icon(ic)}<span class="tag">In development</span></div>
            <h2>{name}</h2>
            <p>{summary}</p>
          </div>
          <div class="product-features">
            <span class="label">Planned capabilities</span>
            <ul class="checks">
{feats}
            </ul>
          </div>
        </article>"""


PAGES["products.html"] = dict(
    title="Products | Dream Hospitality",
    description="Booking, contactless check-in, guest experience and cloud property management software for hotels, resorts and vacation rental operators, in development by Dream Hospitality.",
    body=page_hero(
        "Products · in development",
        "One connected platform for running a property",
        "We are building four modules that work together or on their own, designed for the way independent hotels and rental operators actually work. The first modules are planned for launch in 2027.",
    )
    + """
    <section class="section section-tight">
      <div class="wrap">
        <nav class="chip-nav" aria-label="Products on this page">
          <a href="#booking">Booking system</a>
          <a href="#check-in">Contactless check-in</a>
          <a href="#guest-app">Guest experience app</a>
          <a href="#pms">Property management</a>
        </nav>
        <div class="products">"""
    + product("booking", "booking", "AI-powered booking system",
              "A direct booking engine for hotel and rental websites, helping properties take more bookings through their own channels.",
              ["Direct booking engine for hotel and rental websites", "AI-assisted pricing suggestions", "Availability management", "Guest messaging"])
    + product("check-in", "checkin", "Contactless check-in",
              "A faster arrival for guests and fewer manual steps for the front desk.",
              ["Mobile pre-arrival registration", "ID capture", "Digital key integration", "Self check-in and check-out"])
    + product("guest-app", "guest", "Guest experience app",
              "A branded app that keeps guests informed and connected to the property during their stay.",
              ["Branded for each property", "Guest requests", "Property information and on-site services", "Guest feedback"])
    + product("pms", "pms", "Cloud property management system (PMS)",
              "The operational core of the property, in one cloud system.",
              ["Reservations", "Front desk", "Housekeeping", "Reporting"])
    + """
        </div>
        <p class="note">Product details describe planned functionality and may change before launch.</p>
        <!-- PLACEHOLDER: add launch dates, screenshots or pilot information once the company confirms them. -->
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap split">
        <div>
          <span class="label">How it will be offered</span>
          <h2>Subscription software with local support</h2>
          <p>Our software will be offered mainly on a subscription (SaaS) basis, with implementation, group licensing and support options around it.</p>
        </div>
        <ul class="checks">
          <li><strong>Subscriptions.</strong> The main way properties will use our software.</li>
          <li><strong>Implementation.</strong> Set-up and onboarding for each property.</li>
          <li><strong>Hotel group licences.</strong> Options for groups running several properties.</li>
          <li><strong>Support retainers.</strong> Ongoing support, based in Kuala Lumpur.</li>
          <li><strong>Guest payments stay with the property.</strong> Our booking software does not collect or hold guest funds. Payments are processed by licensed third-party payment providers and settled directly to the hotel or operator.</li>
        </ul>
      </div>
    </section>"""
    + cta_band("Interested in what we're building?", "Tell us about your property and what you need from your systems. Your input helps shape our products."),
)


def service(ic, name, text, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"""
          <div class="card">
            {icon(ic)}
            <h3>{name}</h3>
            <p>{text}</p>
            <ul>{lis}</ul>
          </div>"""


PAGES["consultancy.html"] = dict(
    title="IT Consultancy and Support | Dream Hospitality",
    description="Technology assessments, system selection, implementation and ongoing IT support for hotels, resorts and vacation rental operators in Malaysia.",
    body=page_hero(
        "IT consultancy and support",
        "Technology advice and support for hospitality businesses",
        "Choosing, setting up and running hotel systems takes time most operators don't have. We help hospitality businesses plan, implement and run the technology behind their operations.",
    )
    + """
    <section class="section section-tight">
      <div class="wrap">
        <div class="grid grid-2">"""
    + service("assess", "Technology assessments", "A clear review of the systems you use today, where they fall short and what to prioritise.",
              ["Review of current systems and workflows", "Gaps, risks and priorities", "Practical recommendations"])
    + service("select", "System selection", "Help comparing and choosing booking, property management and guest-facing tools that fit your property and budget.",
              ["Requirements for your property", "Comparison of suitable options", "Support with vendor decisions"])
    + service("implement", "Implementation", "Planning and delivery when you introduce new hospitality systems.",
              ["Project planning and set-up", "Data migration", "Staff onboarding"])
    + service("support", "Ongoing IT support", "Locally based support to keep day-to-day systems running.",
              ["Support for hospitality systems", "Troubleshooting and maintenance", "Support retainers"])
    + """
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <div class="section-head">
          <span class="label">How we work</span>
          <h2>From first review to ongoing support</h2>
          <p>Engagements can cover one step or all of them, depending on what your property needs.</p>
        </div>
        <ol class="steps">
          <li><span class="step-num">1</span><h3>Assess</h3><p>Understand your property, current systems and goals.</p></li>
          <li><span class="step-num">2</span><h3>Select</h3><p>Agree the right tools and a realistic plan.</p></li>
          <li><span class="step-num">3</span><h3>Implement</h3><p>Set up systems, move data and train your team.</p></li>
          <li><span class="step-num">4</span><h3>Support</h3><p>Keep systems running with ongoing local support.</p></li>
        </ol>
      </div>
    </section>"""
    + cta_band("Need help with your hotel technology?", "Tell us what you're working on and we'll discuss how we can help."),
)

PAGES["about.html"] = dict(
    title="About | Dream Hospitality",
    description="Dream Hospitality Sdn. Bhd. is a Malaysian hospitality technology company based in Kuala Lumpur, developing software and providing IT consultancy for hotels, resorts and vacation rental operators.",
    body=page_hero(
        "About us",
        "A Malaysian hospitality technology company",
        "Dream Hospitality Sdn. Bhd. is a private company incorporated in Malaysia in 2026 and based in Kuala Lumpur. We develop software for the hospitality industry and provide IT consultancy and support to hospitality businesses.",
    )
    + f"""
    <section class="section section-tight">
      <div class="wrap grid grid-2">
        <div class="card card-feature">
          <span class="label">Vision</span>
          <p class="quote">To be a trusted provider of practical, affordable hospitality technology in Malaysia and Southeast Asia.</p>
        </div>
        <div class="card card-feature">
          <span class="label">Mission</span>
          <p class="quote">To help hotels, resorts and vacation rental operators increase direct bookings, simplify operations and improve guest experience through reliable, locally supported software.</p>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap split">
        <div>
          <span class="label">Our market</span>
          <h2>Starting in Malaysia, growing across Southeast Asia</h2>
          <p>We focus first on hotels, resorts and rental operators in Malaysia, particularly independent and boutique properties, vacation rental and serviced apartment operators, and small and mid-sized hotel groups.</p>
          <p>As we grow, we plan to serve hospitality businesses in Singapore, Indonesia, Thailand, Vietnam and the Philippines.</p>
        </div>
        <div>
          <span class="label">Our commitments</span>
          <ul class="checks">
            <li><strong>Guest payments stay with the property.</strong> Our booking software does not collect or hold guest funds; payments are processed by licensed third-party providers and settled directly to the hotel or operator.</li>
            <li><strong>Personal data handled responsibly.</strong> We are committed to meeting our obligations under Malaysia's Personal Data Protection Act 2010.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
          <span class="label">Company details</span>
          <h2>Registered in Malaysia</h2>
          <p>Dream Hospitality Sdn. Bhd. is a private company limited by shares, registered with the Companies Commission of Malaysia (SSM).</p>
          <!-- PLACEHOLDER: leadership/team section can be added here once the company approves names, roles and photos. -->
        </div>
        <div class="card">
          <table class="facts">
            <tr><th scope="row">Company</th><td>{COMPANY}</td></tr>
            <tr><th scope="row">Registration No.</th><td>{REG}</td></tr>
            <tr><th scope="row">Incorporated</th><td>Malaysia, 2026</td></tr>
            <tr><th scope="row">Focus</th><td>Software development and IT consultancy for the hospitality industry</td></tr>
            <tr><th scope="row">Office</th><td>Suite T-77, Exchange 106, Lingkaran TRX, Kuala Lumpur</td></tr>
          </table>
        </div>
      </div>
    </section>"""
    + cta_band(),
)

PAGES["contact.html"] = dict(
    title="Contact | Dream Hospitality",
    description="Contact Dream Hospitality Sdn. Bhd., hospitality software and IT services, Exchange 106, Kuala Lumpur.",
    body=page_hero(
        "Contact",
        "Let's talk about your property",
        "Whether you run a boutique hotel, a resort or a portfolio of rental units, we'd like to hear what you need from your technology.",
    )
    + f"""
    <section class="section section-tight">
      <div class="wrap">
        <div class="contact-card">
          <div>
            <span class="label">Office</span>
            <address>
              {COMPANY}<br>
              Suite T-77, Exchange 106<br>
              Lingkaran TRX<br>
              55188 Kuala Lumpur<br>
              Malaysia
            </address>
            <!-- PLACEHOLDER: contact email and phone (to be confirmed by the company) -->
          </div>
          <div>
            <span class="label">Enquiries</span>
            <p>We welcome enquiries from hotels, resorts, vacation rental and serviced apartment operators, and hotel groups about our software and IT consultancy services.</p>
            <!-- PLACEHOLDER: enquiry form + PDPA consent line, once the form service and privacy notice are approved -->
          </div>
        </div>
      </div>
    </section>""",
)


def build():
    for page, p in PAGES.items():
        html = head(page, p["title"], p["description"])
        if p.get("jsonld"):
            html += ORG_JSONLD
        html += header(page) + '  <main id="main">' + p["body"] + "\n  </main>\n" + footer()
        (ROOT / page).write_text(html, encoding="utf-8")
    urls = "\n".join(
        f"  <url>\n    <loc>{SITE if pg == 'index.html' else SITE + pg}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n  </url>"
        for pg in PAGES
    )
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
        encoding="utf-8",
    )
    print("built:", ", ".join(PAGES))


if __name__ == "__main__":
    build()
