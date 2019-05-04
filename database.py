class Connection:
    stations = [{'id': _id} for _id in range(10)]

    @property
    def system_status(self) -> str:
        return 'critical'

    def get_stations(self) -> dict:
        return self.stations

    def get_station(self, station_id: int) -> dict:
        return {
            _id: {'id': 1, 'lat': 100 + station_id} for _id in range(10)
        }.get(station_id)

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

