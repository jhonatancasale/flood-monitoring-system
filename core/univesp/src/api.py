from flask import request, Response
from flask_api import FlaskAPI

from core.univesp.src.flood_system_manager import SystemManager

app = FlaskAPI(__name__)
system = SystemManager()


@app.route('/api/v1.0/', methods='GET'.split())
def get_readme():
    with open('README.md') as readme:
        return jsonify({'readme': readme.readlines()})


@app.route('/api/v1.0/status', methods='GET'.split())
def get_status():
    return {'status': system.status}


@app.route('/api/v1.0/stations', methods='GET'.split())
def get_stations():
    return {'stations': system.get_stations()}


@app.route('/api/v1.0/stations/<int:station_id>', methods='GET'.split())
def get_station(station_id: int):
    return {'station': system.get_station(station_id)}


@app.route('/api/v1.0/stations/<int:station_id>/minutes/<int:minutes>', methods='GET'.split())
def get_from_minutes(station_id: int, minutes: int):
    return {f'data': system.get_from_minutes(station_id, minutes)}


@app.route('/api/v1.0/stations/minutes/<int:minutes>', methods='GET'.split())
def get_all_stations_from_minutes(minutes):
    return {'data:': system.get_all_stations_from_minutes(minutes)}


@app.route('/api/v1.0/stations/<int:station_id>/date/<string:from_date>', methods='GET'.split())
def get_from_date(station_id: int, from_date: str):
    return {f'data:': system.get_from_date(station_id, from_date)}


@app.route('/api/v1.0/stations/date/<string:from_date>', methods='GET'.split())
def get_all_from_date(from_date: str):
    return {'data:': system.get_all_from_date(from_date)}


@app.route('/api/v1.0/stations/<int:station_id>/dates/<string:from_date>/<string:to_date>', methods='GET'.split())
def get_from_to_date(station_id: int, from_date: str, to_date: str):
    return {'data': system.get_from_to_date(station_id, from_date, to_date)}


@app.route('/api/v1.0/stations/dates/<string:from_date>/<string:to_date>', methods='GET'.split())
def get_all_from_to_date(from_date: str, to_date: str):
    return {'data': system.get_all_from_to_date(from_date, to_date)}


@app.route('/api/v1.0/stations/<int:station_id>/measure', methods='POST'.split())
def insert_new_measurement_from(station_id: int):
    data = dict(request.form)

    if system.post_new_measurement(data):
        return Response('success', status=201)
    else:
        return Response('failure', status=400)



if __name__ == '__main__':
    app.run(debug=True)
