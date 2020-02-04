FROM python:3.6
RUN  mkdir app && cd app && git clone https://github.com/claytonrv/users_api.git
WORKDIR /app
RUN ls
RUN pip install -r /app/users_api/requirements.txt
CMD python /app/users_api/user_api.py