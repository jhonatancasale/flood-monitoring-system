from influxdb import InfluxDBClient

from core.univesp.db.properties import config
from core.univesp.utils.logger import get_logger


db_logger = get_logger('connection_logger')


class Connection:
    stations = [{'id': _id} for _id in range(10)]


    def __init__(self):
        self.client = InfluxDBClient(
            'localhost', 8086, 'root', 'root', config["database_name"]
        )

    @property
    def system_status(self) -> str:
        query = 'SELECT "time", "sys_status" FROM station ORDER BY time DESC LIMIT 1'
        result_set = self.client.query(query)
        if not result_set.error:
            return tuple(result_set.get_points())[0]['sys_status']


    def get_stations(self) -> dict:
        query = 'SELECT "id", "type", "battery" FROM station'
        result_set = self.client.query(query)
        if not result_set.error:
            points = result_set.get_points()
            return [
                {
                    key: point[key] for key in 'id type'.split()
                } for point in points
            ]


    def get_station(self, station_id: int) -> dict:
        query = f'SELECT * FROM station WHERE id={str(station_id)!r} ORDER BY "time" DESC LIMIT 1'
        result_set = self.client.query(query)
        if not result_set.error:
            values = tuple(result_set.get_points())[0]
            values.pop('time')
            return values


    def get_from_minutes(self, station_id: int, minutes: int) -> list:
        return [{f'{minute}': minute} for minute in range(minutes, -1, -1)]

    def get_all_stations_from_minutes(self, minutes):
        return []

    def get_from_date(self, station_id: int, from_date: str) -> list:
        return []

    def get_all_from_date(self, from_date: str):
        return []

    def get_from_to_date(self, station_id: int, from_date: str, to_date: str):
        return []

    def get_all_from_to_date(self, from_date: str, to_date: str):
        return []

