Endpoints: (GET)
[prefix] = /api/v1.0

[prefix]/status # the status of the whole system
[prefix]/stations 
[prefix]/stations/<id>
[prefix]/stations/<id>/minutes/<int:minutes>
[prefix]/stations/minutes/<int:minutes>
[prefix]/stations/<id>/dates/<date:from>/
[prefix]/stations/dates/<date:from>/
[prefix]/stations/<id>/dates/<date:from>/<date:to>
[prefix]/stations/dates/<date:from>/<date:to>


(POST)
[prefix]/stations/<id> # to new station
[prefix]/stations/<id>/measure # to new measurement
