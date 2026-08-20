"""Registers all site pages with the build system (registry.PAGES)."""
from registry import register

register(
    "home.html",
    "index.html",
)
