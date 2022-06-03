import quandl

quandl.ApiConfig.api_key = ''
data = quandl.get('BCHARTS/BITFLYERUSD', start_date='20121-10-13', end_date='2021-10-13')

print(data)
