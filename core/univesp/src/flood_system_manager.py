from datetime import datetime

from core.univesp.db.database import Connection
from core.univesp.utils.logger import get_logger

### TODO
# - [ ] Use a Station class

manager_logger = get_logger('manager_logger')

class SystemManager:
    conn = Connection()

    @property
    def status(self) -> str:
        return self.conn.get_system_status()


    def to_timestamp(self, _date):
        try:
            date = datetime.strptime(_date, '%Y%m%d%H%M%S')
        except ValueError as error:
            manager_logger.debug(error)
            return None

        timestamp = f'{date.timestamp()}'.replace('.', '')
        date_len = len(timestamp)

        return f"{timestamp}{'0' * (19 - date_len)}"


    def get_stations(self) -> dict:
        return list(self.conn.get_stations())


    def get_station(self, station_id: int) -> dict:
        return self.conn.get_station(station_id)


    def get_from_minutes(self, station_id: int, minutes: int) -> dict:
        return {'data': self.conn.get_from_minutes(station_id, minutes)}


    def get_all_stations_from_minutes(self, minutes):
        return {'data': self.conn.get_all_stations_from_minutes(minutes)}


    def get_from_date(self, station_id: int, from_date: str):
        date = self.to_timestamp(from_date)

        return self.conn.get_from_date(station_id, date)


    def get_all_from_date(self, from_date: str):
        date = self.to_timestamp(from_date)

        return self.conn.get_all_from_date(date)


    def get_from_to_date(self, station_id: int, _from_date: str, _to_date: str):
        from_date = self.to_timestamp(_from_date)
        to_date = self.to_timestamp(_to_date)

        return self.conn.get_from_to_date(station_id, from_date, to_date)


    def get_all_from_to_date(self, _from_date: str, _to_date: str):
        from_date = self.to_timestamp(_from_date)
        to_date = self.to_timestamp(_to_date)

        return self.conn.get_all_from_to_date(from_date, to_date)

