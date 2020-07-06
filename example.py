from sportscribe import SportScribe



ss = SportScribe('YOUR-API-HERE')
ss.setEndpoint('https://api.sportscribe.co/v1_0/')

# Set language if desired
# ss.setLanguage('es')
result = ss.getMatchPreviewByDate('YYYY-MM-DD')
if result:
  print(result.data)



