FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /stocks_products
COPY ./stocks_products /stocks_products
WORKDIR /stocks_products
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]