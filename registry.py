PAGES = []

def register(template, output, **context):
    PAGES.append((template, output, context))
