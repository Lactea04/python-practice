def city_country_name(city, country, population=''):
    """City, Country - population xxx 형태의 문자열 반환"""
    if population:
        name = f"{city}, {country}"
        additional_infor = f" - population {population}"
        return name.title() + additional_infor
    else:
        name = f"{city}, {country}"
        return name.title()