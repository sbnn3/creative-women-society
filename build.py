#!/usr/bin/env python3
"""Static site builder for Creative Women Society.

Renders Jinja2 templates in templates/pages/ to dist/, copies static/ assets,
and rewrites BASE_URL so the same source can target either a GitHub Pages
project path (e.g. /creative-women-society/) or a root domain (/).

Usage:
  python3 build.py --base-url /creative-women-society/
  python3 build.py --base-url /
"""
import argparse
import os
import shutil
import sys
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(ROOT, "templates", "pages")
DIST_DIR = os.path.join(ROOT, "dist")
STATIC_DIR = os.path.join(ROOT, "static")

sys.path.insert(0, ROOT)
import registry  # noqa: E402


def build(base_url):
    env = Environment(
        loader=FileSystemLoader([os.path.join(ROOT, "templates"), TEMPLATES_DIR]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)

    # copy static assets
    shutil.copytree(STATIC_DIR, os.path.join(DIST_DIR, "static"))

    for template_name, output_rel, context in registry.PAGES:
        tpl = env.get_template(template_name)
        html = tpl.render(base_url=base_url, **context)
        out_path = os.path.join(DIST_DIR, output_rel)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("built:", output_rel)

    print(f"\n{len(registry.PAGES)} pages built to {DIST_DIR} (base_url={base_url})")


if __name__ == "__main__":
    import pages_manifest  # noqa: F401  (registers pages via import side-effect)
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="/creative-women-society/")
    args = ap.parse_args()
    build(args.base_url)
