FROM python:3.10-slim as builder
# RUN apt-get update
# RUN apt-get install libxml2 libreoffice libxml2-dev libxslt-dev libmagic1 unoconv -y
# RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
# RUN apt-get update;apt-get install -y --no-install-recommends fontconfig ttf-mscorefonts-installer
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

# #RUN pip install --install-option="--prefix=/ins" -r requirements.txt
# # FROM python:3.6-alpine
# # COPY --from=builder /app/env /app/env
# # ENV PATH="/app/env/bin:$PATH"

# ADD . /tmp/
# WORKDIR /tmp
# #server
ENV ENV  development
ENV HOST_NAME   0.0.0.0
ENV PORT_NAME   5000
ENV NUMBER_WORKER 4

EXPOSE 5000
CMD python run.py
# # CMD gunicorn --bind ${HOST_NAME}:${PORT_NAME} wsgi:app -w ${NUMBER_WORKER}
