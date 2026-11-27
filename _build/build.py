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
LASTMOD = "2026-11-27"

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
  <meta name="theme-color" content="#09090d" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#09090d" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Dream Hospitality">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}assets/img/og-purple.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Dream Hospitality: hospitality software and IT services, Kuala Lumpur">
  <meta property="og:locale" content="en_MY">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="assets/img/mark.svg" type="image/svg+xml">
  <link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="stylesheet" href="assets/css/style.css?v=4">"""


ORG_JSONLD = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "{COMPANY}",
    "legalName": "DREAM HOSPITALITY SDN. BHD.",
    "url": "{SITE}",
    "logo": "{SITE}assets/img/dream-hospitality-logo.svg",
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
        <img src="assets/img/dream-hospitality-logo.svg" alt="" width="64" height="60">
        <span>Dream<span class="brand-sub">Hospitality</span></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links"><span>Menu</span><span aria-hidden="true" class="menu-icon"></span></button>
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
        <a class="footer-brand" href="index.html"><img src="assets/img/dream-hospitality-logo.svg" alt="Dream Hospitality" width="96" height="90"></a><p class="footer-company">{COMPANY}</p>
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
  <script src="assets/js/main.js?v=4" defer></script>
</body>
</html>
"""


def page_hero(label, title, lead):
    return f"""
    <section class="page-hero">
      <div class="wrap page-hero-grid">
        <div><span class="eyebrow">{label}</span>
        <h1>{title}</h1>
        <p class="lead">{lead}</p></div>
        <div class="orbit" aria-hidden="true"><span>✦</span></div>
      </div>
    </section>"""


def cta_band(title="Hospitality technology, closer to home.", text="Based at Exchange 106 in Kuala Lumpur. Find our business address and the latest contact information.", btn="Prepare a property brief"):
    return f"""
    <section class="section">
      <div class="wrap">
        <div class="cta-band">
          <div>
            <h2>{title}</h2>
            <p>{text}</p>
          </div>
          <a class="btn btn-light" href="contact.html#property-brief">{btn}</a>
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------- pages
PAGES = {}

PAGES["index.html"] = dict(
    title="Dream Hospitality | Hospitality technology, thoughtfully built",
    description="Hospitality software in development and IT consultancy for hotels, resorts and vacation rental operators. Based in Kuala Lumpur, Malaysia.",
    jsonld=True,
    body=f"""
    <section class="hero">
      <div class="wrap hero-grid">
        <div class="hero-copy">
          <span class="eyebrow">Hospitality technology · Kuala Lumpur</span>
          <h1>Behind every<br>better stay.<br><em>Better technology.</em></h1>
          <p class="lead">Thoughtful software and practical IT support for the people who make hospitality happen.</p>
          <div class="cta-row"><a class="btn btn-primary" href="products.html">Explore our products</a><a class="text-link" href="consultancy.html">Discover our consultancy</a></div>
        </div>
        <div class="hero-identity">
          <div class="identity-caption"><span>Dream Hospitality</span><span>Malaysia · Est. 2026</span></div>
          <img class="hero-logo" src="assets/img/dream-hospitality-logo.svg" alt="Dream Hospitality circular logo, Registration No. 202601013644" width="600" height="600" fetchpriority="high">
          <p>Practical. Affordable. Locally supported.</p>
        </div>
      </div>
      <div class="wrap hero-bottom"><span>Built around your property. Designed for your guests.</span><span>Software development &amp; IT consultancy</span></div>
    </section>
    <section class="section suite-section">
      <div class="wrap">
        <div class="section-head section-head-split"><div><span class="label">The product suite</span><h2>A smoother journey.<br>From booking to check-out.</h2></div><div><p>Four hospitality software modules in development, focused on simpler operations and a better guest experience.</p><span class="tag">First modules planned for 2027</span></div></div>
        <div class="suite-list">
          <a href="products.html#booking" class="suite-row">{icon('booking')}<h3>AI-powered booking</h3><p>Direct bookings, availability and guest messaging.</p><span class="row-action">Explore</span></a>
          <a href="products.html#check-in" class="suite-row">{icon('checkin')}<h3>Contactless check-in</h3><p>Less time at the desk. A simpler arrival.</p><span class="row-action">Explore</span></a>
          <a href="products.html#guest-app" class="suite-row">{icon('guest')}<h3>Guest experience app</h3><p>Requests, services and feedback in one place.</p><span class="row-action">Explore</span></a>
          <a href="products.html#pms" class="suite-row">{icon('pms')}<h3>Cloud property management</h3><p>Reservations, front desk, housekeeping and reporting.</p><span class="row-action">Explore</span></a>
        </div>
      </div>
    </section>
    <section class="section consultancy-feature">
      <div class="wrap split">
        <div><span class="label">IT consultancy &amp; support</span><h2>Your hospitality expertise.<br><em>Our technology focus.</em></h2></div>
        <div><p class="lead">The right systems should make your day easier.</p><p>We help hospitality businesses assess their technology, choose suitable systems, implement them and keep them running with local support.</p><a class="btn btn-dark" href="consultancy.html">Explore consultancy services</a></div>
      </div>
    </section>
    <section class="section">
      <div class="wrap"><div class="section-head"><span class="label">Who we serve</span><h2>Independent spirit.<br>Shared ambitions.</h2><p>Starting in Malaysia, with plans to grow across Southeast Asia.</p></div>
      <div class="audience-grid"><article><span class="audience-symbol" aria-hidden="true">✦</span><h3>Hotels &amp; resorts</h3><p>Independent and boutique properties looking for more direct bookings and simpler day-to-day operations.</p></article><article><span class="audience-symbol" aria-hidden="true">◈</span><h3>Rentals &amp; serviced apartments</h3><p>Operators managing multiple units who need easier arrivals and better guest communication.</p></article><article><span class="audience-symbol" aria-hidden="true">◎</span><h3>Growing hotel groups</h3><p>Small and mid-sized groups that need consistent systems and support across their properties.</p></article></div></div>
    </section>
    <section class="section section-alt"><div class="wrap split"><div><span class="label">The Dream approach</span><h2>Technology with<br>hospitality at its heart.</h2><a class="text-link" href="about.html">Get to know Dream Hospitality</a></div><ul class="checks"><li><strong>More direct bookings.</strong> Help properties welcome guests through their own channels.</li><li><strong>Simpler operations.</strong> Reduce manual steps across the front desk and housekeeping.</li><li><strong>A better guest experience.</strong> Make arrivals and communication feel easier.</li></ul></div></section>
    """ + cta_band("Your property. Your next chapter.", "Explore hospitality technology with a Malaysian company focused on practical software and local support.", "Plan your property brief"),
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
        "Better stays begin behind the scenes.",
        "We are developing booking, check-in, guest experience and property management software for hotels, resorts and vacation rentals. The first modules are planned for launch in 2027; all capabilities below are planned.",
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
    + cta_band("Interested in what we're building?", "Visit our contact page for our office details. Direct enquiry channels will be added once confirmed."),
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
        "Make technology work for your property.",
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
    + cta_band("Need help with your hotel technology?", "Find our Kuala Lumpur office and the latest information on how to reach us."),
)

PAGES["about.html"] = dict(
    title="About | Dream Hospitality",
    description="Dream Hospitality Sdn. Bhd. is a Malaysian hospitality technology company based in Kuala Lumpur, developing software and providing IT consultancy for hotels, resorts and vacation rental operators.",
    body=page_hero(
        "About us",
        "Rooted in Malaysia. Built for hospitality.",
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
            <tr><th scope="row">Incorporated</th><td>8 April 2026, Malaysia</td></tr>
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
        "Find us in Kuala Lumpur.",
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
            <a class="btn btn-dark" href="https://www.google.com/maps/search/?api=1&amp;query=Exchange%20106%2C%20Lingkaran%20TRX%2C%20Kuala%20Lumpur" target="_blank" rel="noopener noreferrer">View building on Google Maps</a>
          </div>
          <div>
            <span class="label">Direct enquiries</span>
            <h2>Contact details are being finalised.</h2>
            <p>Our email address and telephone number will be added once confirmed. Online enquiries are not available yet.</p>
            <p>We welcome enquiries from hotels, resorts, vacation rental and serviced apartment operators, and hotel groups about our software and IT consultancy services.</p>
            <!-- PLACEHOLDER: enquiry form + PDPA consent line, once the form service and privacy notice are approved -->
          </div>
        </div>
      </div>
    </section>""",
)


from enhancements import apply
ENQUIRY_READY = apply(PAGES, page_hero, cta_band)

def build():
    for page, p in PAGES.items():
        html = head(page, p["title"], p["description"])
        if p.get("jsonld"):
            html += ORG_JSONLD
        html += header(p.get("nav_parent", page)) + '  <main id="main">' + p["body"] + "\n  </main>\n" + footer()
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
