import common

r = common.Artist('cher', '8ed0103c4c47b623fb344b83c3c2c222')

array = [r.get_events(), r.get_info, r.get_passed_events]

for method in array:
    print method
