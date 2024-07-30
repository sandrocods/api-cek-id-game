from flask import Blueprint, request, jsonify
from datetime import datetime

from src.ApiCheckGames import ApiCheckGames

apiCheckIdGame = Blueprint('apiCheckIdGame', __name__)


@apiCheckIdGame.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': True,
        'message': 'Welcome to the cek-id-game API',
        'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


@apiCheckIdGame.route('/list-games', methods=['GET'])
def list_games():
    return jsonify({
        'status': True,
        'data': [name for name, member in ApiCheckGames.__dict__.items() if callable(member) and not name.startswith('_')],
        'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


@apiCheckIdGame.route('/check-id-game', methods=['GET', 'POST'])
def check_id_game():
    try:
        if request.method == 'GET':
            type_name = request.args.get('type_name', None)
            userId = request.args.get('userId', None)
            zoneId = request.args.get('zoneId', None)
        elif request.method == 'POST':
            type_name = request.json.get('type_name', None)
            userId = request.json.get('userId', None)
            zoneId = request.json.get('zoneId', None)
        else:
            return jsonify({
                'status': False,
                'message': 'Method not allowed',
                'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        api = ApiCheckGames()
        if type_name not in ApiCheckGames.__dict__:
            return jsonify({
                'status': False,
                'message': 'Type name not found',
                'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        if type_name == 'eight_ball_pool':
            return jsonify(api.eight_ball_pool(userId))
        elif type_name == 'aether_gazer':
            return jsonify(api.aether_gazer(userId))
        elif type_name == 'arena_of_valor':
            return jsonify(api.arena_of_valor(userId))
        elif type_name == 'auto_chess':
            return jsonify(api.auto_chess(userId))
        elif type_name == 'azur_lane':
            return jsonify(api.azur_lane(userId, zoneId))
        elif type_name == 'bad_landers':
            return jsonify(api.bad_landers(userId, zoneId))
        elif type_name == 'barbarq':
            return jsonify(api.barbarq(userId))
        elif type_name == 'basketrio':
            return jsonify(api.basketrio(userId))
        elif type_name == 'call_of_duty':
            return jsonify(api.call_of_duty(userId))
        elif type_name == 'dragon_city':
            return jsonify(api.dragon_city(userId))
        elif type_name == 'free_fire':
            return jsonify(api.free_fire(userId))
        elif type_name == 'hago':
            return jsonify(api.hago(userId))
        elif type_name == 'mobile_legends':
            return jsonify(api.mobile_legends(userId, zoneId))
        elif type_name == 'point_blank':
            return jsonify(api.point_blank(userId))
        elif type_name == 'valorant':
            return jsonify(api.valorant(userId))

    except Exception as error_message:
        return jsonify({
            'status': False,
            'message': str(error_message),
            'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
