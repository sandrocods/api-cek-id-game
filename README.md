
# Python Library for Checking a Game Nickname Based on an Account ID
<img src="https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/banner.png">

A Python library designed to make it easier for game developers, data analysts, and other users to check and validate usernames (nicknames) in a game based on account IDs. The library provides a simple and easy-to-use interface for accessing username data from a game database.



## Feature

| Name | Status     |
| :-------- | :------- |
| Proxy Support | ✔ |
| Logger Request | ✔ |
| 15 Games Type | ✔ |




## Usage

To use this library

```python3
from src.ApiCheckGames import ApiCheckGames

api = ApiCheckGames(debug=True, proxy=None)

print(
    api.eight_ball_pool(
        userId="<userId>"
    )
)
```
Available parameters

| Name | Desc     | Example |
| :-------- | :------- | :------- |
| `debug` | To active debug mode for request inspection | `True` or `False`|
| `proxy` | To avoid banned requests | `{'https': 'http://user:password@host:port'}`|
| `userId` | userId Account | |
| `zoneId` | zoneId Account | |


Example Response Success ✔
```json
{
    "status": true,
    "server_time": "2024-07-30 16:31:29",
    "message": "Success Requesting to API",
    "nickname": "Martinus Krisandro Perdana Putra",
    "type_name": "HAGO"
}
```

Example Response Failed ❌
```json
{
    "status": false,
    "server_time": "2024-07-30 16:32:24",
    "message": "userIDNotEligibleError",
    "type_name": "HAGO"
}
```

```json
{
    "status": false,
    "server_time": "2024-07-30 16:32:37",
    "message": "Invalid Request Parameter(s) [userAccount.userId must not be blank]",
    "type_name": "HAGO"
}
```
## List of Games

|Image | Name             | Method                         |
| ----------------- | ----------------- | ---------------- |
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/8bp.webp)| eight_ball_pool | [eight_ball_pool](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L50)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/aether_gazer.webp)| aether_gazer | [aether_gazer](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L101)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/arena_of_valor.webp)| arena_of_valor | [arena_of_valor](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L158)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/auto_chess.webp)| auto_chess | [auto_chess](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L210)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/azur_lane.webp)| azur_lane | [azur_lane](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L261)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/bad_landers.webp)| bad_landers | [bad_landers](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L331)
<img src="https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/barbarq.jpg" width="60">| barbarq | [barbarq](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L396)
<img src="https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/basketrio.jpg" width="60">| basketrio | [basketrio](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L447)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/call_of_duty.webp)| call_of_duty | [call_of_duty](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L513)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/dragon_city.webp)| dragon_city | [dragon_city](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L564)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/free_fire.webp)| free_fire | [free_fire](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L615)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/hago.webp)| hago | [hago](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L666)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/mobile_legends.webp)| mobile_legends | [mobile_legends](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L717)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/point_blank.webp)| point_blank | [point_blank](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L768)
![App Screenshot](https://raw.githubusercontent.com/sandrocods/api-cek-id-game/master/assets/valorant.webp)| valorant | [valorant](https://github.com/sandrocods/api-cek-id-game/blob/master/src/ApiCheckGames.py#L819)

## Support

For support or another request api, email krisandromartinus@gmail.com or send message in [telegram](https://t.me/sandroputraaa).

