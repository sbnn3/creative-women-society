# Creative Women Society — Official Website

**A Society of Elegant Minds.**

This repository contains the source code for the Creative Women Society website — built from the Society's brand & website brief (Chapters 1–11: brand identity, site architecture, page-by-page content, features, and visual identity).

## Live preview

The site auto-builds and deploys on every push to `main` via GitHub Actions → GitHub Pages:

**https://sbnn3.github.io/creative-women-society/**

This is the working preview link — it always reflects the latest commit, so you can watch the site evolve in real time.

The Society's own domain, **creativewomensociety.com**, currently shows a "coming soon" page (see the [`creativewomensociety-comingsoon`](https://github.com/sbnn3/creativewomensociety-comingsoon) repository) and will be pointed at this site once it is ready to launch.

## How this site is built

Plain HTML/CSS/JS, generated from [Jinja2](https://jinja.palletsprojects.com/) templates — no framework, no build tooling beyond Python, fast-loading and simple to maintain.

```
site/
├── templates/
│   ├── base.html            # shared <head>, header/nav include, footer include
│   ├── partials/
│   │   ├── nav.html
│   │   └── footer.html
│   └── pages/                # one template per page
├── static/
│   ├── css/style.css         # design system (colours, type, components)
│   ├── js/main.js            # header scroll state, mobile nav, reveal animation, FAQ accordion
│   └── img/
├── registry.py                # page registry used by build.py
├── pages_manifest.py           # registers every page + its route + metadata
├── build.py                   # renders templates/pages/*.html → dist/
└── requirements.txt
```

### Building locally

```bash
pip install -r requirements.txt
python build.py --base-url /creative-women-society/   # for the GitHub Pages preview
# or
python build.py --base-url /                          # for the creativewomensociety.com root domain
```

Output is written to `dist/`.

## Content status

Text taken directly from the Society's brand brief is used verbatim. Sections the brief did not provide finished copy for (Founder biography & photo, Member Spotlight, Journal article bodies, legal pages) currently use clearly-placeholder content in the Society's voice, ready to be replaced with real material. All photography is temporary, curated stock (see `image_bank.md` in the project notes) standing in for real Society photography, per Chapter 11.6–11.7.

## Roadmap

See the open items tracked in the project — Signature Experiences category pages, The Society, Legacy, Membership, The Journal, Contact, legal pages, and eventually the CMS / member-portal features described in Chapter 10 of the brief.
