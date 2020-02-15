from location_functions import *

def get_ann_location(features):
    workdays = ['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday']
    if features['weather_today'] == 'Sunny':
        if features['time_season'] == 'Summer' and features['time_weekday'] == 'Tuesday':
            return '8:00 am - 4:59 pm\nGreen Ranch\n6:00 pm - 8:59 pm\nBeach'
        elif features['time_weekday'] in workdays:
            return '8:00 am - 4:59 pm\nGreen Ranch'
        elif features['time_weekday'] == 'Thursday':
            if features['ann_location_byte'] == 0x00:
                return '9:00 am - 4:59 pm\nFisherman\'s Tent Screen'
            elif features['ann_location_byte'] == 0x01:
                return '9:00 am - 4:59 pm\nCarpenter\'s House Screen'
            elif features['ann_location_byte'] == 0x02:
                return '9:00 am - 4:59 pm\nVineyard'
            elif features['ann_location_byte'] == 0x03:
                return '10:00 am - 4:59pm\nRick\'s Tool Shop'
        elif features['time_weekday'] == 'Sunday':
            if features['ann_location_byte'] in [0x00, 0x01]:
                return '8:00 am - 4:59 pm\nGoddess Pond'
            elif features['ann_location_byte'] in [0x02, 0x03]:
                return '8:00 am - 4:59 pm\nGreen Ranch'
    elif features['weather_today'] in ['Rainy', 'Snowy']:
        if features['time_weekday'] in workdays:
            return '8:00 am - 4:59 pm\nGreen Ranch Barn'
        elif features['time_weekday'] == 'Sunday':
            return '9:00 am - 4:59 pm\nGreen Ranch Barn'

def get_elli_location(features):
    pass

def convert_character_locations(features):
    locations = {}
    locations['ann_location'] = get_ann_location(features)
    locations['elli_location'] = get_elli_location(features)
    return {**features, **locations}

