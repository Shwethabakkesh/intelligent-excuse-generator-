from deep_translator import GoogleTranslator

def translate_text(text, lang='hi'):
    try:
        return GoogleTranslator(source='auto', target=lang).translate(text)
    except Exception as e:
        return f"Translation Error: {e}"
