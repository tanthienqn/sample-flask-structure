FROM python:3.10-slim as builder

WORKDIR /tmp
ADD Pipfile /tmp/
ADD Pipfile.lock /tmp/
RUN python -m venv /app/env
ENV PATH="/app/env/bin:$PATH"
RUN pip install --upgrade pip && \
     pip install pipenv && \
     pipenv install --dev --system --deploy --ignore-pipfile
ADD requirements.txt /tmp/
RUN pip install -r requirements.txt

########################################################################################################################
# Re build image
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app/env ./env
ADD . .
ENV PATH="/app/env/bin:$PATH"

ENV ENV  development
ENV HOST_NAME   0.0.0.0
ENV PORT_NAME   5000
ENV NUMBER_WORKER 4

EXPOSE 5000

CMD gunicorn -c gunicorn.conf.py run:gunicorn_app
