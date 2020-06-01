from sportscribe import SportScribe



ss = SportScribe('YOUR-API-HERE')
result = ss.getMatchPreviewByDate('YYYY-MM-DD')
if result:
  print(result.data)



