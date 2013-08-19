bind = 'unix:/tmp/gunicorn.sock'
# bind = '0.0.0.0:5000'

backlog = 2048
workers = 5
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
# timeout = 30
# keepalive = 2
