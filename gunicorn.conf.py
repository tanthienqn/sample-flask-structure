from os import environ


bind = "0.0.0.0:" + environ.get("PORT_NAME", "5000")
worker_connections = int(environ.get("MAX_CONNECTION_WORKER", "1000"))
worker_class = environ.get("WORKER_CLASS", "gthread")
workers = int(environ.get("NUMBER_WORKER", "2"))
threads = int(environ.get("NUMBER_THREAD", "200"))
timeout = int(environ.get("SERVICE_TIMEOUT", "60"))
# max_requests = int(environ.get("MAX_REQUESTS", "1000"))
# max_requests_jitter = 1
preload_app = True
errorlog = "-"
loglevel = "info"
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'
