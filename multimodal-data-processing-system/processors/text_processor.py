def summarize_text(text):
    lines = text.split('.')
    return '. '.join(lines[:3]) + '...'
