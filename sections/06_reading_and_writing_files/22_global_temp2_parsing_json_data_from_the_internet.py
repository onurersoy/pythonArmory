import json
import urllib.request

# json_data_source = 'temperature_anomaly.json'
json_data_source = ('https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe'
                    '/land_ocean/1/10/1880-2022.json')

with urllib.request.urlopen(json_data_source) as json_stream:
    # The 'urlopen' function can be used in a 'with' statement, so our internet connection will be automatically
    # closed for us.
    data = json_stream.read().decode('utf-8')  # The urllib library is quite old, and doesn't automatically decode
    # for us. So we have to explicitly decode the data from UTF-8^^.
    anomalies = json.loads(data)

print(anomalies['description'])
print('*' * 80)

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
