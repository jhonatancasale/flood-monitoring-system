## Endpoints

### GET
```
/api/v1.0/status # the status of the whole system
/api/v1.0/stations 
/api/v1.0/stations/<id>
/api/v1.0/stations/<id>/minutes/<int:minutes>
/api/v1.0/stations/minutes/<int:minutes>
/api/v1.0/stations/<id>/dates/<date:from>/
/api/v1.0/stations/dates/<date:from>/
/api/v1.0/stations/<id>/dates/<date:from>/<date:to>
/api/v1.0/stations/dates/<date:from>/<date:to>
```


### POST
```
/api/v1.0/stations/<id> # to new station
/api/v1.0/stations/<id>/measure # to new measurement
```
