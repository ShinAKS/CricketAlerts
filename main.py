import requests
import json

def alert():
    uri = "https://hs-consumer-api.espncricinfo.com/v1/pages/match/details?lang=en&seriesId=1244186&matchId=1244274&latest=true"
    response = requests.get(uri)
    json_data = json.loads(response.text)

    print(json_data['recentBallCommentary']['ballComments'][0])

if __name__=="__main__":
    alert()
