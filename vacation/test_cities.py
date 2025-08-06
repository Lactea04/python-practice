from city_functions import city_country_name

def test_city_country():
    """Santiago, Chile 같은 도시와 나라의 이름에 대한 테스트"""
    name = city_country_name(
        'santiago', 'chile'
    )
    assert name == 'Santiago, Chile'

def test_city_country_population():
    """Santiago, Chile - population 5000000 같은 도시와 나라의 이름에 대한 테스트"""
    infor = city_country_name(
        'santiago', 'chile', 5000000
    )
    assert infor == 'Santiago, Chile - population 5000000'