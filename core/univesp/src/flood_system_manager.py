from core.univesp.src.database import Connection

### TODO
# - [ ] Use a Station class

class SystemManager:
    conn = Connection()

    @property
    def status(self) -> str:
        return self.conn.system_status

    def valid_from_date(self, from_date):
        return False

    def valid_to_date(self, to_date):
        return False

    def to_timestamp(date):
        return ''

    def valid_range_date(self, _from_date, _to_date):
        from_date = to_timestamp(_from_date)
        to_date = to_timestamp(_to_date)

        return (
            self.valid_from_date(from_date) and \
            self.valid_to_date(to_date) and \
            from_date < to_date
        )

    def get_stations(self) -> dict:
        return self.conn.get_stations()

    def get_station(self, station_id: int) -> dict:
        return self.conn.get_station(station_id)

    def get_from_minutes(self, station_id: int, minutes: int) -> dict:
        return {
            'get_from_minutes': \
            self.conn.get_from_minutes(station_id, minutes)
        }

    def get_all_stations_from_minutes(self, minutes):
        return {
            'get_all_stations_from_minutes': \
            self.conn.get_all_stations_from_minutes(minutes)
        }

    def get_from_date(self, station_id: int, from_date: str):
        return {'get_from_date': \
            self.conn.get_from_date(station_id, from_date)
        }

    def get_all_from_date(self, from_date: str):
        return {'get_all_from_date': self.conn.get_all_from_date(from_date)}

    def get_from_to_date(self, station_id: int, from_date: str, to_date: str):
        return {
            'get_from_to_date': self.conn.get_from_to_date(
            station_id, from_date, to_date
        )}

    def get_all_from_to_date(self, from_date: str, to_date: str):
        return {
            'get_all_from_to_date': self.conn.get_all_from_to_date(
                from_date, to_date
        )}

