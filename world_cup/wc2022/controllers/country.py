from ..models import Country, GroupMembers, Group

def country_list():
    data = {"country_list": Country.objects.filter()}
    return data

def country_group(country_id):
    data = {"country_group": GroupMembers.objects.filter(country_id=country_id).get()}
    return data