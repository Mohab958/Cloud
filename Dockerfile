FROM python:3.9
ADD cloud.py .
WORKDIR /cloud
COPY . /cloud
COPY paragraphs.txt /app/data/
RUN pip install --upgrade pip setuptools
RUN pip install nltk
EXPOSE 4000
CMD python ./cloud.py




