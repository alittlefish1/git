from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家返回pygal使用的两个字母的国别号"""

    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到指定的国家就返回none
    return None

    ##    print(country_code,COUNTRIES[country_code])