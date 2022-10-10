FROM python:3.9

#update
RUN apt-get update



#install requirements
COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /tmp
RUN pip install wget
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2022.05-MacOSX-arm64.sh -O ~/anaconda.sh
RUN curl — proto '=https' — tlsv1.2 -sSf https://sh.rustup.rs -y | sh
RUN pip install transformers
RUN pip install cmake
RUN pip install pkgconfig
RUN pip install sentence-transformers
RUN pip install -r requirements.txt


#copy app
COPY . /api
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":6000", "-t", "360", "--reload", "api.wsgi:app"]
