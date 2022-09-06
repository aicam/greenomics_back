#
FROM python:3.9

#
WORKDIR /code

ENV MYSQLCONNECTION="mysql+pymysql://root:1234@db:3306/greenomics"
#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./ /code

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
