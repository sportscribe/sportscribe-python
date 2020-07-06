import requests, json

# Class to manage the result
class SportScribeResult:

  status = False
  data = None

  def __init__(self,res):
    if res.status_code == 200:
      self.status = True
      self.data = res.json()
    else:
      self.status = False
      self.data = { 'status_code' : res.status_code }

  def __bool__(self):
    return self.status

  def __str__(self):
    return json.dumps(self.data,indent=2)


# Class to manage the API interface
class SportScribe:

  apikey : str = None
  endpoint : str = None
  language : str = 'en'

  def __init__(self,apikey):
    if apikey == None or apikey == '':
      raise Exception('No ApiKey')
    else:
      self.apikey = apikey

  def setEndpoint(self,endpoint : str):
    self.endpoint = endpoint

  def setLanguage(self,language : str):
    self.language = language

  def __get(self,endpoint : str):
    if not endpoint[0] == '/':

      raise Exception('invalid endpoint');
    elif not self.endpoint:
      raise Exception('endpoint not set');

    headers = { 'x-api-key' : self.apikey }
    api_url = self.endpoint + endpoint + '?lang=' + self.language




    res = requests.get(api_url, headers=headers)
    return SportScribeResult(res)

  def getLeagues(self):
    return(self.__get('/leagues'))

  def getMatchPreviewByTeam(self,teamid : int) :
    return(self.__get('/matchPreview/' + str(teamid)))

  def getMatchPreviewByDate(self,date : str) :
    return(self.__get('/matchPreview/date/' + date))

  def getTeams(self,leagueid : int):
    return(self.__get('/teams/' + str(leagueid)))
