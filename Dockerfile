FROM python:3.12.5

RUN apt-get update
RUN apt-get install -y git
RUN pip install --upgrade pip

RUN git clone https://github.com/bukhantcev/BeautyServant.git
WORKDIR /site1
ENV BOT_TOKEN = '5641597027:AAGuUaoQpMPmsxqZwXz1KNwJF6I1P1Pvih0'
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN echo "git pull && python3.12 manage.py runserver 78:111.88.18:8000" > start.sh
CMD [ "bash", "start.sh" ]
CMD ["gunicorn","-b","0.0.0.0:8000","site1.wsgi:application"]












ENV BOT_TOKEN = '5641597027:AAGuUaoQpMPmsxqZwXz1KNwJF6I1P1Pvih0'