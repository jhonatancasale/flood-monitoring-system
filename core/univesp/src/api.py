from flask import Flask, jsonify
from core.univesp.src.flood_system_manager import SystemManager

app = Flask(__name__)
system = SystemManager()


@app.route('/api/v1.0/', methods='GET'.split())
def get_readme():
    with open('README.md') as readme:
        return jsonify({'readme': readme.readlines()})


@app.route('/api/v1.0/status', methods='GET'.split())
def get_status():
    return jsonify({'status': system.status})


@app.route('/api/v1.0/stations', methods='GET'.split())
def get_stations():
    return jsonify({'stations': system.get_stations()})


@app.route('/api/v1.0/stations/<int:station_id>', methods='GET'.split())
def get_station(station_id: int):
    return jsonify({'stations': system.get_station(station_id)})


@app.route('/api/v1.0/stations/<int:station_id>/minutes/<int:minutes>', methods='GET'.split())
def get_from_minutes(station_id: int, minutes: int):
    return jsonify({f'data': system.get_from_minutes(station_id, minutes)})


@app.route('/api/v1.0/stations/minutes/<int:minutes>', methods='GET'.split())
def get_all_stations_from_minutes(minutes):
    return jsonify({'data:': system.get_all_stations_from_minutes(minutes)})


@app.route('/api/v1.0/stations/<int:station_id>/date/<string:from_date>', methods='GET'.split())
def get_from_date(station_id: int, from_date: str):
    return jsonify({f'data:': system.get_from_date(station_id, from_date)})


@app.route('/api/v1.0/stations/date/<string:from_date>', methods='GET'.split())
def get_all_from_date(from_date: str):
    return jsonify({'data:': system.get_all_from_date(from_date)})


@app.route('/api/v1.0/stations/<int:station_id>/date/<string:from_date>/<string:to_date>', methods='GET'.split())
def get_from_to_date(station_id: int, from_date: str, to_date: str):
    return jsonify(
        {'data': system.get_from_to_date(station_id, from_date, to_date)}
    )


@app.route('/api/v1.0/stations/date/<string:from_date>/<string:to_date>', methods='GET'.split())
def get_all_from_to_date(from_date: str, to_date: str):
    return jsonify(
        {'data': system.get_all_from_to_date(from_date, to_date)}
    )


if __name__ == '__main__':
    app.run(debug=True)