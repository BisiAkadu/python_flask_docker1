FROM python:alpine
ADD . /appfile
WORKDIR /appfile
COPY requirement.txt .
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
COPY . .
EXPOSE 5005
CMD ["python", "main.py"]
