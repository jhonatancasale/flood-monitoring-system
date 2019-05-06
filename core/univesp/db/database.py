from influxdb import InfluxDBClient

from core.univesp.db.properties import config
from core.univesp.utils.logger import get_logger
from requests.exceptions import ConnectionError
from influxdb.exceptions import InfluxDBClientError


db_logger = get_logger('connection_logger')


class Connection:
    def __init__(self):
        self.client = InfluxDBClient(
            'localhost', 8086, 'root', 'root', config["database_name"]
        )


    def execute_query(self, query):
        try:
            _result_set = self.client.query(query)
            if not _result_set.error:
                result_set = tuple(_result_set.get_points())
                return  result_set[0] if len(result_set) == 1 else result_set
        except ConnectionError as error:
            db_logger.error(error)


    def get_system_status(self) -> str:
        query = 'SELECT "time", "sys_status" FROM station \
                ORDER BY time DESC \
                LIMIT 1'

        result_set = self.execute_query(query)
        return result_set['sys_status'] if result_set else None


    def get_stations(self) -> dict:
        query = 'SELECT "id", "type", "battery" FROM station'

        result_set = self.execute_query(query)
        return (
            {key: point[key] for key in 'id type'.split()} for point in result_set
        ) if result_set else []


    def get_station(self, station_id: int) -> dict:
        query = f'\
                SELECT * FROM station \
                WHERE id={str(station_id)!r} \
                ORDER BY "time" DESC \
                LIMIT 1'

        result_set = self.execute_query(query)
        return {
            key: result_set[key] for key in result_set if key not in 'time'.split()
        } if result_set else {}


    def simple_select_query(self, query):
        result_set = self.execute_query(query)

        return result_set if result_set else []


    def get_from_minutes(self, station_id: int, minutes: int) -> list:
        query = f'SELECT * FROM station \
                WHERE "time" > now() - {minutes}m \
                AND "id" = {str(station_id)!r}'

        return self.simple_select_query(query)


    def get_all_stations_from_minutes(self, minutes):
        query = f'SELECT * FROM station WHERE "time" > now() - {minutes}m'

        return self.simple_select_query(query)


    def get_from_date(self, station_id: int, from_date: str) -> list:
        query = f'SELECT * FROM station \
                WHERE "time" > {from_date} \
                AND "id" = {str(station_id)!r}'

        return self.simple_select_query(query)


    def get_all_from_date(self, from_date: str):
        query = f'SELECT * FROM station WHERE "time" > {from_date}'

        return self.simple_select_query(query)


    def get_from_to_date(self, station_id: int, from_date: str, to_date: str):
        query = f'SELECT * FROM station \
                WHERE "time" > {from_date} \
                AND "time" < {to_date} \
                AND "id" = {str(station_id)!r}'

        return self.simple_select_query(query)


    def get_all_from_to_date(self, from_date: str, to_date: str):
        query = f'SELECT * FROM station \
                WHERE "time" > {from_date} \
                AND "time" < {to_date}'

        return self.simple_select_query(query)

    def post_new_measurement(self, data) -> bool:
        points = [
            {
                'measurement': 'station',
                'tags': {
                    'id': int(data['id']),
                    'type': data['type'],
                },
                'fields': {
                    'value': float(data['value']),
                    'sys_status': data['sys_status'],
                    'battery': float(data['battery']),
                },
            }
        ]

        try:
            return self.client.write_points(points)
        except InfluxDBClientError as error:
            db_logger.error(error)
            return None

