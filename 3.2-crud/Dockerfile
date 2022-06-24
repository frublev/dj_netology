FROM python:3.10
ENV PYTHONUNBUFFERED 1
COPY ./stocks_products /stocks_products
WORKDIR /stocks_products
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]