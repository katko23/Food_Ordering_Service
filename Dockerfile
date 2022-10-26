FROM python:alpine

WORKDIR /app

COPY . .

EXPOSE 27001

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python" , "FoodOrderingMain.py"]