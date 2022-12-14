FROM python:3.6-alpine

# install poetry for easily managing our dependencies
RUN pip install poetry

# create the application directory
RUN mkdir -p /app

# set the script to run when entrypoint
COPY . /app
WORKDIR /app

# install flask dependencies
RUN poetry install

# expose the application on port 5000
EXPOSE 5000

# make sure basic security measures are enabled
ENV FLASK_ENV="production" \
    FLASK_DEBUG=0

# run the application
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
