from sys import exit

from core.univesp.db.properties import config
from core.univesp.utils.logger import get_logger

from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError


db_logger = get_logger('db_logger')


def database_exists(client: InfluxDBClient) -> bool:
    return False

def create_database(database_name: str, client: InfluxDBClient) -> bool:
    client.query(f'CREATE DATABASE {database_name}')

    return True



def main():
    db_logger.info(f'Setting up database {config["database_name"]!r}:[Start]')

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
    try:
        client.query('show databases')
    except ConnectionError as error:
        db_logger.error(error)
        exit(1)

    ### TODO
    if not database_exists(client):
        if create_database(config['database_name'], client):
            db_logger.info(f'Done!')
            db_logger.info(f'Setting up database {config["database_name"]!r}:[End]')
        else:
            db_logger.error(f"Fail to create the database!")
    else:
        db_logger.info(f'The database {config["database_name"]!r} already exists!')


if __name__ == '__main__':
    main()
