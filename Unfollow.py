import requests
import json

cookie = '' -- ur cookie duh
robloxId = 27628965 -- ur roblox id

session = requests.Session()
session.cookies['.ROBLOSECURITY'] = cookie
session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/unfollow').headers['x-csrf-token']
followingCount = requests.get(f'https://friends.roblox.com/v1/users/{robloxId}/followings/count')
following = requests.get(f'https://friends.roblox.com/v1/users/{robloxId}/followings?sortOrder=Asc&limit=100')

while followingCount.json()['count'] != 0:
    for i in following.json()['data']:
        id = i['id']
        userName = requests.get(f'https://friends.roblox.com/v1/metadata?targetUserId={id}').json()['userName']
        print(f'unfollowed: {userName}')
        session.post(f'https://friends.roblox.com/v1/users/{id}/unfollow')
    nextPageCursor = following.json()['nextPageCursor']
    following = requests.get(f'https://friends.roblox.com/v1/users/{robloxId}/followings?sortOrder=Asc&limit=100&cursor={nextPageCursor}')
    followingCount = requests.get(f'https://friends.roblox.com/v1/users/{robloxId}/followings/count')
