FROM python:3.7

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    libatlas-base-dev gfortran nginx supervisor && apt-get clean cache

WORKDIR /app

RUN git clone https://github.com/jhonatancasale/flood-monitoring-system.git .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    pip3 install uwsgi flask

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -rf /root/.cache

COPY nginx.conf /etc/nginx/
COPY flask-site-nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/

CMD ["/usr/bin/supervisord"]
