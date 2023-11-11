FROM python:3.7
EXPOSE 5000
WORKDIR /app
RUN git clone
COPY . .
RUN python -m pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]