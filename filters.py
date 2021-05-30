from datetime import datetime

def date(value, date_format, date_string_format='%Y-%m-%d'):
    if date_format == 'iso':
        value = value[:-1] if value[-1].lower() == 'z' else value
        return datetime.fromisoformat(value).strftime(date_string_format)