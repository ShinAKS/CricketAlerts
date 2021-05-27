import requests
import json

#
def alert(comments,score):
    score = score.split()[0]
    comment = comments['ballComments'][0]
    over = comment['oversActual']
    action = comment['title']
    isOut = comment['isWicket']
    runs = comment['totalRuns']
    print(', '.join([str(over),str(score),action,'OUT' if isOut else  "{} runs".format(runs)]))

def getData():
    uri = "https://hs-consumer-api.espncricinfo.com/v1/pages/match/details?lang=en&seriesId=1244186&matchId=1244274&latest=true"
    response = requests.get(uri)
    json_data = json.loads(response.text)

    # print(json_data['recentBallCommentary'],json_data['liveSummary']['fowText'])
    alert(json_data['recentBallCommentary'],json_data['liveSummary']['fowText'])
if __name__=="__main__":
    getData()
