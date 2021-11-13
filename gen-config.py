import docker
from jinja2 import Template
#initialize docker api socket
api_client = docker.APIClient(base_url='unix://var/run/docker.sock')