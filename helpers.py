def celsius_para_kelvin(temperatura_celsius):
    """
    Função para converter temperatura de celsius para kelvin
    :param temperatura_celsius:
    :return: temperatura em kelvin
    Formula: C + 273.15
    """
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin

def celsius_para_fahrenheit(temperatura_celsius):
    """
    Função pra converter temperatura de celsius para fahrenheit
    :param temperatura_celsius:
    :return: celsius para fahrenheit
    Formula  (C *  9/5) + 32
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit
