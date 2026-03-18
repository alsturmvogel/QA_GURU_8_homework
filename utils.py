def clean_text(text: str) -> str:
    # Заменяет \\t и \\n на пробелы, лишние пробелы обрезает.
    text = text.replace('\t', ' ').replace('\n', ' ')
    return ' '.join(text.split())
