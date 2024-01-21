class CountryInfoModel:
    def __init__(self, country_info):
        self.country_info = country_info

    def get_value(self, country, info):
        if country not in self.country_info:
            return None
        return self.country_info[country][info]
