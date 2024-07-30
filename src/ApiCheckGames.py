"""

Helper Check id Games using CodaShop API

Author  : sandroputraa
Date    : 2024-07-30
Version : 1.0

"""
from requests_toolbelt.utils import dump
from datetime import datetime
from loguru import logger
import requests


class ApiCheckGames:

    def __init__(self, debug=False, proxy=None):
        self.debug = debug
        logger.add(
            sink="logs.log",
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan><b>{message}</b></cyan>",
            rotation="1 week",
        )
        logger.opt(colors=True)

        self.request = requests.session()

        if proxy is not None:
            logger.info("Request Using Proxy | Proxy: {}".format(proxy))

        self.request.proxies = proxy
        self.request.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        })

        self.logger = logger
        self.endpoint_api = {
            'coda_shop': 'https://order-sg.codashop.com/initPayment.action'
        }
        self.headers = {
            'coda_shop': {
                "Host": "order-sg.codashop.com",
                "Accept-Language": "id-ID",
                "Origin": "https://www.codashop.com",
                "Referer": "https://www.codashop.com/",
            }
        }

    def eight_ball_pool(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'EIGHT_BALL_POOL',
            }
        try:
            logger.info("Trying Requesting to API | Product: EIGHT_BALL_POOL | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': 272564,
                    'voucherPricePoint.price': 14000.0000,
                    'voucherPricePoint.variablePrice': 0,
                    'user.userId': userId,
                    'user.zoneId': None,
                    'voucherTypeName': 'EIGHT_BALL_POOL',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: EIGHT_BALL_POOL | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'EIGHT_BALL_POOL',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: EIGHT_BALL_POOL | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'EIGHT_BALL_POOL',
                }
            else:
                logger.error("Failed Requesting to API | Product: EIGHT_BALL_POOL | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'EIGHT_BALL_POOL',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'EIGHT_BALL_POOL',
            }

    def aether_gazer(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'AETHER_GAZER',
            }
        try:
            logger.info("Trying Requesting to API | Product: AETHER_GAZER | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '2',
                    'voucherPricePoint.price': '16650.0',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': None,
                    'voucherTypeName': '547-AETHER_GAZER',
                    'voucherTypeId': '524',
                    'gvtId': '691',
                    'lvtId': '11840',
                    'pcId': '906',
                    'shopLang': 'id_ID',
                    'dynamicSkuToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkeW5hbWljU2t1SW5mbyI6IntcInNrdUlkXCI6XCJjb20ueW9zdGFyLmFldGhlcmdhemVyLnNoaWZ0aW5nZmxvd2VyMVwiLFwiZXZlbnRQYWNrYWdlXCI6XCIwXCIsXCJkZW5vbUltYWdlVXJsXCI6XCJodHRwczovL2NkbjEuY29kYXNob3AuY29tL2ltYWdlcy81NDdfM2QyMTBiNzUtNTJkYi00YjUxLTgzMGYtZDYxMTFiNjFkNDQ5X0FFVEhFUiBHQVpFUl9pbWFnZS9Db2RhX0FHX1NLVWltYWdlcy82MC5wbmdcIixcImRlbm9tTmFtZVwiOlwiNjAgU2hpZnRpbmcgRmxvd2Vyc1wiLFwiZGVub21DYXRlZ29yeU5hbWVcIjpcIlNoaWZ0aW5nIEZsb3dlcnNcIixcInRhZ3NcIjpbXSxcImNvdW50cnkyTmFtZVwiOlwiSURcIixcImx2dElkXCI6MTE4NDAsXCJhZGRpdGlvbmFsSW5mb1wiOntcIkR5bmFtaWNTa3VQcm9tb0RldGFpbFwiOlwibnVsbFwifX0ifQ.eKiPyHwGZJUuUGGzwWiPiDuF6xC5G7_PWLn6TXVAKVs',
                    'pricePointDynamicSkuToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkeW5hbWljU2t1SW5mbyI6IntcInBjSWRcIjo5MDYsXCJwcmljZVwiOjE2NjUwLjAsXCJjdXJyZW5jeVwiOlwiSURSXCIsXCJhcGlQcmljZVwiOjE2NjUwLjAsXCJhcGlQcmljZUN1cnJlbmN5XCI6XCJJRFJcIixcImRpc2NvdW50UHJpY2VcIjoxNjY1MC4wLFwicHJpY2VCZWZvcmVUYXhcIjoxNTAwMC4wLFwidGF4QW1vdW50XCI6MTY1MC4wLFwic2t1SWRcIjpcImNvbS55b3N0YXIuYWV0aGVyZ2F6ZXIuc2hpZnRpbmdmbG93ZXIxXCIsXCJsdnRJZFwiOjExODQwfSJ9.y89THkVNztOzAXS64nr9Rtamn3wbWLIYXeRWrZ9yMBc',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: AETHER_GAZER | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'AETHER_GAZER',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: AETHER_GAZER | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'AETHER_GAZER',
                }
            else:
                logger.error("Failed Requesting to API | Product: AETHER_GAZER | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'AETHER_GAZER',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'AETHER_GAZER',
            }

    def arena_of_valor(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'ARENA_OF_VALOR',
            }
        try:
            logger.info("Trying Requesting to API | Product: ARENA_OF_VALOR | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '270294',
                    'voucherPricePoint.price': '10000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': '2748846783202461',
                    'user.zoneId': None,
                    'voucherTypeName': 'AOV',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: ARENA_OF_VALOR | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('roles')[0].get('role')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('roles')[0].get('role'),
                    'server': request_data.json().get('confirmationFields').get('roles')[0].get('server'),
                    'type_name': 'ARENA_OF_VALOR',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: ARENA_OF_VALOR | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'ARENA_OF_VALOR',
                }
            else:
                logger.error("Failed Requesting to API | Product: ARENA_OF_VALOR | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'ARENA_OF_VALOR',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'ARENA_OF_VALOR',
            }

    def auto_chess(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'AUTO_CHESS',
            }
        try:
            logger.info("Trying Requesting to API | Product: AUTO_CHESS | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '203879',
                    'voucherPricePoint.price': '150000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'voucherTypeName': 'AUTO_CHESS',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )

            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: AUTO_CHESS | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'AUTO_CHESS',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: AUTO_CHESS | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'AUTO_CHESS',
                }
            else:
                logger.error("Failed Requesting to API | Product: AUTO_CHESS | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'AUTO_CHESS',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'AUTO_CHESS',
            }

    def azur_lane(self, userId, zoneId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'AZUR_LANE',
            }
        if zoneId == '' or zoneId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Zone ID is Required',
                'type_name': 'AZUR_LANE',
            }
        if zoneId == 'Avrora':
            zoneIdCode = '1'
        elif zoneId == 'Lexington':
            zoneIdCode = '2'
        elif zoneId == 'Sandy':
            zoneIdCode = '3'
        if zoneId == 'Washington':
            zoneIdCode = '4'
        elif zoneId == 'Amagi':
            zoneIdCode = '5'
        elif zoneId == 'Little Enterprise':
            zoneIdCode = '6'
        else:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Invalid Zone ID',
            }
        try:
            logger.info("Trying Requesting to API | Product: AZUR_LANE | User ID: {} | Zone ID: {}".format(userId, zoneId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '99665',
                    'voucherPricePoint.price': '70000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': zoneIdCode,
                    'voucherTypeName': 'AZUR_LANE',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: AZUR_LANE | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'server': zoneId,
                    'type_name': 'AZUR_LANE',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: AZUR_LANE | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'AZUR_LANE',
                }
            else:
                logger.error("Failed Requesting to API | Product: AZUR_LANE | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'AZUR_LANE',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'AZUR_LANE',
            }

    def bad_landers(self, userId, zoneId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'BAD_LANDERS',
            }
        if zoneId == '' or zoneId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Zone ID is Required',
                'type_name': 'BAD_LANDERS',
            }
        if zoneId == 'Global':
            zoneIdCode = '11001'
        elif zoneId == 'JF':
            zoneIdCode = '21004'
        else:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Invalid Zone ID',
                'type_name': 'BAD_LANDERS',
            }

        try:
            logger.info("Trying Requesting to API | Product: BAD_LANDERS | User ID: {} | Zone ID: {}".format(userId, zoneId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '333121',
                    'voucherPricePoint.price': '2300.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': zoneIdCode,
                    'voucherTypeName': 'BAD_LANDERS',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: BAD_LANDERS | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'server': zoneId,
                    'type_name': 'BAD_LANDERS',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: BAD_LANDERS | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'BAD_LANDERS',
                }
            else:
                logger.error("Failed Requesting to API | Product: BAD_LANDERS | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'BAD_LANDERS',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'BAD_LANDERS',
            }

    def barbarq(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'BARBARQ',
            }

        try:
            logger.info("Trying Requesting to API | Product: BARBARQ | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '5145',
                    'voucherPricePoint.price': '120000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'voucherTypeName': 'ELECSOUL',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )

            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: BARBARQ | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('apiResult')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('apiResult'),
                    'type_name': 'BARBARQ',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: BARBARQ | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'BARBARQ',
                }
            else:
                logger.error("Failed Requesting to API | Product: BARBARQ | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'BARBARQ',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'BARBARQ',
            }

    def basketrio(self, userId, zoneId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'BASKETRIO',
            }

        if zoneId == '' or zoneId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Zone ID is Required',
                'type_name': 'BASKETRIO',
            }

        if zoneId == 'Buzzer Beater':
            zoneIdCode = '2'
        elif zoneId == '001':
            zoneIdCode = '3'
        elif zoneId == '002':
            zoneIdCode = '4'
        else:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Invalid Zone ID',
                'type_name': 'BASKETRIO',
            }

        try:
            logger.info("Trying Requesting to API | Product: BASKETRIO | User ID: {} | Zone ID: {}".format(userId, zoneId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '147203',
                    'voucherPricePoint.price': '832500.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': zoneIdCode,
                    'voucherTypeName': 'BASKETRIO',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: BASKETRIO | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'server': zoneId,
                    'type_name': 'BASKETRIO',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: BASKETRIO | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'BASKETRIO',
                }
            else:
                logger.error("Failed Requesting to API | Product: BASKETRIO | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'BASKETRIO',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'BASKETRIO',
            }

    def call_of_duty(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'CALL_OF_DUTY',
            }
        try:
            logger.info("Trying Requesting to API | Product: CALL_OF_DUTY | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '270251',
                    'voucherPricePoint.price': '20000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': None,
                    'voucherTypeName': 'CALL_OF_DUTY',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: CALL_OF_DUTY | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('roles')[0].get('role')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('roles')[0].get('role'),
                    'type_name': 'CALL_OF_DUTY',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: CALL_OF_DUTY | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'CALL_OF_DUTY',
                }
            else:
                logger.error("Failed Requesting to API | Product: CALL_OF_DUTY | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'CALL_OF_DUTY',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'CALL_OF_DUTY',
            }

    def dragon_city(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'DRAGON_CITY',
            }
        try:
            logger.info("Trying Requesting to API | Product: DRAGON_CITY | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '254206',
                    'voucherPricePoint.price': '65000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': None,
                    'voucherTypeName': 'DRAGON_CITY',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: DRAGON_CITY | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username'))),
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'DRAGON_CITY',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: DRAGON_CITY | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'DRAGON_CITY',
                }
            else:
                logger.error("Failed Requesting to API | Product: DRAGON_CITY | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'DRAGON_CITY',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'DRAGON_CITY',
            }

    def free_fire(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'FREE_FIRE',
            }
        try:
            logger.info("Trying Requesting to API | Product: FREE_FIRE | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '270288',
                    'voucherPricePoint.price': '200000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': None,
                    'voucherTypeName': 'FREEFIRE',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: FREE_FIRE | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('roles')[0].get('role')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('roles')[0].get('role'),
                    'type_name': 'FREE_FIRE',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: FREE_FIRE | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'FREE_FIRE',
                }
            else:
                logger.error("Failed Requesting to API | Product: FREE_FIRE | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'FREE_FIRE',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'FREE_FIRE',
            }

    def hago(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'HAGO',
            }
        try:
            logger.info("Trying Requesting to API | Product: HAGO | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '272113',
                    'voucherPricePoint.price': '29700.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': None,
                    'voucherTypeName': 'HAGO',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: HAGO | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'HAGO',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: HAGO | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'HAGO',
                }
            else:
                logger.error("Failed Requesting to API | Product: HAGO | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'HAGO',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'HAGO',
            }

    def mobile_legends(self, userId, zoneId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'MOBILE_LEGENDS',
            }
        if zoneId == '' or zoneId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'Zone ID is Required',
                'type_name': 'MOBILE_LEGENDS',
            }
        try:
            logger.info("Trying Requesting to API | Product: MOBILE_LEGENDS | User ID: {} | Zone ID: {}".format(userId, zoneId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '5199',
                    'voucherPricePoint.price': '68543.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': zoneId,
                    'voucherTypeName': 'MOBILE_LEGENDS',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: MOBILE_LEGENDS | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'MOBILE_LEGENDS',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: MOBILE_LEGENDS | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'MOBILE_LEGENDS',
                }
            else:
                logger.error("Failed Requesting to API | Product: MOBILE_LEGENDS | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'MOBILE_LEGENDS',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'MOBILE_LEGENDS',
            }

    def point_blank(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'POINT_BLANK',
            }
        try:
            logger.info("Trying Requesting to API | Product: POINT_BLANK | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '344845',
                    'voucherPricePoint.price': '11000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': '0',
                    'voucherTypeName': 'POINT_BLANK',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: POINT_BLANK | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'POINT_BLANK',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: POINT_BLANK | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'POINT_BLANK',
                }
            else:
                logger.error("Failed Requesting to API | Product: POINT_BLANK | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'POINT_BLANK',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'POINT_BLANK',
            }

    def valorant(self, userId):
        if userId == '' or userId is None:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': 'User ID is Required',
                'type_name': 'VALORANT',
            }
        try:
            logger.info("Trying Requesting to API | Product: VALORANT | User ID: {}".format(userId))
            request_data = self.request.post(
                url=self.endpoint_api['coda_shop'],
                data={
                    'voucherPricePoint.id': '950525',
                    'voucherPricePoint.price': '75000.0000',
                    'voucherPricePoint.variablePrice': '0',
                    'userVariablePrice': '0',
                    'user.userId': userId,
                    'user.zoneId': '0',
                    'voucherTypeName': 'VALORANT',
                    'shopLang': 'id_ID',
                },
                headers=self.headers['coda_shop']
            )
            if self.debug:
                logger.debug(dump.dump_all(request_data).decode('utf-8'))
            if request_data.status_code == 200 and request_data.json().get('errorCode') == '':
                logger.success("Success Requesting to API | Product: VALORANT | User ID: {} | Nickname: {}".format(userId, request_data.json().get('confirmationFields').get('username')))
                return {
                    'status': True,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Success Requesting to API',
                    'nickname': request_data.json().get('confirmationFields').get('username'),
                    'type_name': 'VALORANT',
                }
            elif request_data.status_code == 200 and request_data.json().get('errorCode') != '':
                logger.error("Failed Requesting to API | Product: VALORANT | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': request_data.json().get('errorMsg'),
                    'type_name': 'VALORANT',
                }
            else:
                logger.error("Failed Requesting to API | Product: VALORANT | User ID: {} | Response: {}".format(userId, request_data.json()))
                return {
                    'status': False,
                    'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'message': 'Failed Requesting to API',
                    'type_name': 'VALORANT',
                }
        except Exception as error_requests:
            return {
                'status': False,
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'message': str(error_requests),
                'type_name': 'VALORANT',
            }
