"""Registers all site pages with the build system (registry.PAGES)."""
from registry import register

register(
    "home.html",
    "index.html",
)

register(
    "experiences_landing.html",
    "signature-experiences/index.html",
)

register(
    "experience_category.html",
    "signature-experiences/arts-culture/index.html",
    category_name="Arts & Culture",
    tagline="Celebrating creativity through theatre, opera, museums, galleries, workshops and cultural experiences.",
    purpose="To inspire women through creativity, culture and artistic expression. Experiences are designed to deepen cultural appreciation while encouraging conversation and shared discovery.",
    hero_image="https://images.unsplash.com/photo-1564399580075-5dfe19c205f3?auto=format&fit=crop&w=1800&q=80",
    examples=[
        "Theatre Evenings", "Opera & Ballet Performances", "Museum Visits", "Art Gallery Tours",
        "Painting Workshops", "Pottery Workshops", "Floral Design Workshops", "Photography Walks",
        "Artist Talks", "Classical Music Concerts", "Heritage Experiences", "National Trust Visits",
        "Cultural Festivals",
    ],
    future_items=[
        "The Royal Opera Experience", "The National Gallery Evening", "The Hidden Museums Series",
        "Meet the Artist", "The Sculpture Garden Experience",
    ],
    featured_title="The Hidden Museums Series",
    featured_description="A forthcoming series exploring London's lesser-known collections, paired with conversation and reflection.",
)

register(
    "experience_category.html",
    "signature-experiences/literary-afternoons-book-club/index.html",
    category_name="Literary Afternoons & Book Club",
    tagline="Thought-provoking conversations inspired by books, literature and lifelong learning.",
    purpose="To celebrate literature, ideas and thoughtful conversations in an elegant and inspiring atmosphere. Reading becomes a shared experience that encourages curiosity, dialogue and lifelong learning.",
    hero_image="https://images.unsplash.com/photo-1722182877533-7378b60bf1e8?auto=format&fit=crop&w=1800&q=80",
    examples=[
        "Monthly Book Club", "Afternoon Tea & Books", "Literary Conversations", "Author Talks",
        "Poetry Evenings", "Reading Circles", "British Literature Series", "Women's Literature Series",
        "Leadership Book Club", "Biography Discussions", "Creative Writing Workshops",
    ],
    future_items=[
        "The Literary Afternoon", "Books & Brunch", "The Oxford Literary Experience",
        "The Shakespeare Evening", "Coffee & Conversations",
    ],
    featured_title="The Literary Afternoon",
    featured_description="A recurring gathering for thoughtful conversation over books, tea and shared perspective.",
)

register(
    "experience_category.html",
    "signature-experiences/society-gatherings/index.html",
    category_name="Society Gatherings",
    tagline="Elegant social experiences designed to connect women through meaningful conversations, wellbeing and shared moments.",
    purpose="To create elegant social occasions where women connect through shared experiences, wellbeing and inspiring conversations. These gatherings celebrate friendship, beauty, hospitality and the joy of spending meaningful time together.",
    hero_image="https://images.unsplash.com/photo-1785119774026-b6066d7835f5?auto=format&fit=crop&w=1800&q=80",
    examples=[
        "Afternoon Tea Experiences", "Fine Dining Evenings", "Seasonal Gatherings", "Garden Parties",
        "Christmas Gala", "Etiquette Workshops", "British Etiquette Series", "Beauty Workshops",
        "Wellbeing Workshops", "Spa Retreats", "Wine Tastings", "Chocolate Tastings",
        "Hat Styling Workshops", "Personal Branding Sessions", "Fashion & Style Workshops",
        "Perfume Masterclasses", "Floral Workshops",
    ],
    future_items=[
        "The Ritz Society Experience", "The Wellness Escape", "The Garden Party",
        "The Elegant Table", "The Parisian Afternoon", "The Ladies' Autumn Retreat",
    ],
    featured_title="The Ritz Society Experience",
    featured_description="Our signature afternoon of elegance, conversation and connection — see the full experience page.",
)

register(
    "experience_category.html",
    "signature-experiences/signature-journeys/index.html",
    category_name="Signature Journeys",
    tagline="Extraordinary journeys carefully designed to combine travel, culture and unforgettable experiences.",
    purpose="To create unforgettable journeys that combine travel, culture and discovery. Every journey is designed to become a memorable chapter in the life of the Society.",
    hero_image="https://images.unsplash.com/photo-1759732029561-10c0d0198281?auto=format&fit=crop&w=1800&q=80",
    examples=[
        "Oxford Experience", "Cambridge Experience", "Stonehenge", "The Cotswolds", "Bath",
        "Edinburgh", "Scottish Highlands", "Hidden Britain", "Paris", "Venice", "Tuscany",
        "Norwegian Fjords",
    ],
    future_items=[
        "London from Above", "The Royal Castles Journey", "Hidden Gardens of England",
        "The Venice Experience", "The Scandinavian Escape", "Christmas in Europe",
    ],
    featured_title="The Oxford Experience",
    featured_description="A day of heritage, architecture and shared discovery through one of England's most storied cities.",
)

register(
    "experience_ritz.html",
    "signature-experiences/the-ritz-society-experience/index.html",
)

# ---------------------------------------------------------------------------
# The Society / Legacy / Membership
# ---------------------------------------------------------------------------

register("the_society.html", "the-society/index.html")
register("legacy.html", "legacy/index.html")
register("membership.html", "membership/index.html")

# ---------------------------------------------------------------------------
# The Journal
# ---------------------------------------------------------------------------

register("journal_landing.html", "journal/index.html")

register(
    "journal_article.html",
    "journal/an-editors-letter/index.html",
    title="An Editor's Letter",
    category="Conversations",
    date="August 2026",
    reading_time="3 min",
    summary="A short note from our founder — what's ahead, what has inspired her, and a thought for the community.",
    hero_image="https://images.unsplash.com/photo-1607423730403-b7fc1eb83ce0?auto=format&fit=crop&w=1800&q=80",
    body_html="""
<p>Dear Society,</p>
<p>There is a particular kind of pleasure in beginning something new while carrying forward everything that came before it. Creative Women Society did not begin on a blank page &mdash; it began in a classroom, in the friendships and conversations that outlasted any single lesson, and in the quiet realisation that a community, once formed, does not want to stop growing.</p>
<p>This letter is the first of what I hope will become a small monthly tradition: a short note, at the start of each month, about what is ahead for the Society, what has inspired me recently, and a thought I would like to leave with you. Not a long article &mdash; simply a conversation, the way I might begin one over tea.</p>
<p>What is ahead: the Society's Signature Experiences are beginning to take shape across all four categories &mdash; Arts &amp; Culture, Literary Afternoons &amp; Book Club, Society Gatherings and Signature Journeys. Each one has been designed with the same question in mind: will this bring women closer together, and will it leave them with something worth carrying home?</p>
<p>What has inspired me: the idea, borrowed from nowhere in particular except good manners and better company, that elegance is not about extravagance at all. It is about attention &mdash; to a table properly set, to a conversation properly listened to, to a friendship properly tended. That is the standard I would like every experience we create to be held to.</p>
<p>And a thought for the community: belonging is rarely announced. It tends to arrive quietly, somewhere between a shared laugh and a shared silence. I hope that is exactly how it feels to be part of this Society.</p>
<p>With warmth,<br>The Founder</p>
""",
)

register(
    "journal_article.html",
    "journal/the-quiet-power-of-lifelong-learning/index.html",
    title="The Quiet Power of Lifelong Learning",
    category="Leadership",
    date="August 2026",
    reading_time="4 min",
    summary="Why curiosity, not certainty, is the most enduring form of confidence.",
    hero_image="https://images.unsplash.com/photo-1620130674275-d709994ed7c8?auto=format&fit=crop&w=1800&q=80",
    body_html="""
<p>It is tempting, in professional life, to treat confidence as a destination — a state you arrive at once you have learned enough, achieved enough, or been told enough times that you are right. But the women we admire most rarely describe their confidence this way. They describe it as a habit of staying curious.</p>
<p>Lifelong learning is often framed as a professional obligation: a course to complete, a certification to renew. Within Creative Women Society, we think of it differently — as a form of self-respect. To keep asking questions, long after you are expected to know the answers, is one of the quieter forms of courage.</p>
<h2>Learning as Connection, Not Competition</h2>
<p>One of the reasons the Society's Leadership &amp; Professional Growth gatherings avoid the language of networking is that learning, done well, is not a transaction. It is closer to hospitality: you offer what you know, and you receive what someone else has taken years to understand, and both of you leave a little richer than you arrived.</p>
<p>This is why a Leadership Conversation at the Society rarely looks like a lecture. It looks like a circle of women, some decades into their careers and some only beginning, discussing a single idea from every angle they can find.</p>
<h2>The Discipline of Staying a Beginner</h2>
<p>There is a particular grace in a woman who has every reason to consider herself an expert, and who still asks the beginner's question anyway. It is not a lack of confidence. It is, we would argue, the most durable kind there is — the kind that does not need to be defended, only practised.</p>
<p>So the invitation, this month, is a simple one: pick up the book you have been meaning to read, ask the question you have been holding back, and treat your own curiosity as seriously as you treat your achievements. It has, after all, gotten you further than certainty ever could.</p>
""",
)

register(
    "journal_article.html",
    "journal/the-art-of-the-afternoon/index.html",
    title="The Art of the Afternoon",
    category="Elegant Living",
    date="August 2026",
    reading_time="3 min",
    summary="On the quiet ritual of afternoon tea, and why slowing down is a form of elegance.",
    hero_image="https://images.unsplash.com/photo-1769637565381-f21f88e7b4d6?auto=format&fit=crop&w=1800&q=80",
    body_html="""
<p>There is a specific hour — somewhere after lunch has settled and before the day begins to hurry towards evening — that the English have quietly perfected the art of doing very little, very beautifully. Afternoon tea did not become a tradition because anyone needed the calories. It became a tradition because someone, a very long time ago, understood that a day needs a pause built into it on purpose.</p>
<p>At Creative Women Society, The Ritz Society Experience exists for exactly this reason. It is not really about the sandwiches, though they help. It is about the deliberate, slightly old-fashioned decision to set aside an entire afternoon for nothing more productive than good company and good conversation.</p>
<h2>Elegance Is a Decision, Not a Budget</h2>
<p>It is easy to mistake elegance for expense. But the truest version of it — the version this Society tries to embody in every experience it curates — is really a decision about attention. A properly laid table. A conversation without a phone nearby. A afternoon with nowhere else to be.</p>
<p>You do not need The Ritz to practise this. A pot of tea, a good cup, and forty-five minutes without an agenda will do the job perfectly well at your own kitchen table.</p>
<h2>A Small Invitation</h2>
<p>This week, we would gently suggest reclaiming one afternoon — even briefly — for the sake of nothing but itself. Put the kettle on. Call a friend, or don't. Either way, let the hour be entirely, unapologetically unhurried. It is, in its own quiet way, one of the more elegant things you can do all week.</p>
""",
)

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

register("contact.html", "contact/index.html")

# ---------------------------------------------------------------------------
# Legal
# ---------------------------------------------------------------------------

register(
    "legal.html",
    "privacy-policy/index.html",
    title="Privacy Policy",
    body_html="""
<h2>1. Who We Are</h2>
<p>Creative Women Society ("the Society", "we", "us", "our") is a community for women based in London, United Kingdom. This Privacy Policy explains how we collect, use and protect personal data when you visit this website, subscribe to our newsletter, apply for membership, or otherwise get in touch with us.</p>
<h2>2. What Personal Data We Collect</h2>
<p>Depending on how you interact with us, we may collect: your name, email address and telephone number (contact and membership forms); the content of messages you send us; your email address if you subscribe to our newsletter; and standard technical data (such as browser type and pages visited) collected automatically when you use the website.</p>
<h2>3. How We Use Your Data</h2>
<p>We use personal data to respond to enquiries, process membership applications, send newsletters and event communications to those who have opted in, and improve the website. We do not sell personal data to third parties.</p>
<h2>4. Legal Basis for Processing (UK GDPR)</h2>
<p>We process personal data on the basis of consent (for newsletter subscriptions and marketing communications), the performance of a contract (for membership), and our legitimate interests in operating and improving the Society and this website.</p>
<h2>5. Data Retention</h2>
<p>We retain personal data only for as long as necessary for the purposes described above, or as required by law.</p>
<h2>6. Your Rights</h2>
<p>Under UK data protection law, you have the right to access, correct, delete, or restrict the use of your personal data, and to withdraw consent at any time (for example, by unsubscribing from our newsletter). To exercise these rights, please contact us at the email address below.</p>
<h2>7. Cookies</h2>
<p>This website uses cookies as described in our <a href="../cookie-policy/">Cookie Policy</a>.</p>
<h2>8. Contact</h2>
<p>For any questions about this Privacy Policy or how your data is handled, please contact us at <a href="mailto:hello@creativewomensociety.com">hello@creativewomensociety.com</a>.</p>
""",
)

register(
    "legal.html",
    "terms-conditions/index.html",
    title="Terms & Conditions",
    body_html="""
<h2>1. Introduction</h2>
<p>These Terms &amp; Conditions govern your use of this website and, where applicable, your membership of Creative Women Society. By using this website or applying for membership, you agree to these terms.</p>
<h2>2. Use of This Website</h2>
<p>This website is provided for informational purposes and to facilitate membership applications, enquiries and newsletter subscriptions. You agree to use the website only for lawful purposes.</p>
<h2>3. Membership</h2>
<p>Membership of Creative Women Society is subject to acceptance by the Society. Membership benefits, options and pricing are described on the Membership page and may be updated from time to time. Full membership terms will be provided upon application.</p>
<h2>4. Signature Experiences</h2>
<p>Places at Signature Experiences are offered subject to availability. Specific booking terms, cancellation policies and dress codes will be communicated ahead of each experience.</p>
<h2>5. Intellectual Property</h2>
<p>All content on this website, including text, images and the Creative Women Society name and identity, is the property of Creative Women Society or its licensors and may not be reproduced without permission.</p>
<h2>6. Limitation of Liability</h2>
<p>While we take care to keep this website accurate and up to date, Creative Women Society accepts no liability for any loss arising from reliance on information provided on this website.</p>
<h2>7. Changes to These Terms</h2>
<p>We may update these Terms &amp; Conditions from time to time. Continued use of the website after changes are published constitutes acceptance of the revised terms.</p>
<h2>8. Contact</h2>
<p>Questions about these Terms &amp; Conditions can be sent to <a href="mailto:hello@creativewomensociety.com">hello@creativewomensociety.com</a>.</p>
""",
)

register(
    "legal.html",
    "cookie-policy/index.html",
    title="Cookie Policy",
    body_html="""
<h2>1. What Are Cookies</h2>
<p>Cookies are small text files placed on your device when you visit a website. They help websites function properly and can provide information about how the site is used.</p>
<h2>2. How We Use Cookies</h2>
<p>This website may use essential cookies necessary for the site to function, and analytics cookies that help us understand how visitors use the site so we can improve it. Where analytics or non-essential cookies are used, we will ask for your consent via a cookie banner.</p>
<h2>3. Managing Cookies</h2>
<p>You can control or delete cookies through your browser settings at any time. Please note that disabling certain cookies may affect the functionality of this website.</p>
<h2>4. Third-Party Cookies</h2>
<p>Where the website embeds third-party content (such as fonts or, in future, booking or payment tools), those third parties may set their own cookies in accordance with their own policies.</p>
<h2>5. Contact</h2>
<p>Questions about this Cookie Policy can be sent to <a href="mailto:hello@creativewomensociety.com">hello@creativewomensociety.com</a>.</p>
""",
)
