from pprint import pprint
from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')

pprint(cli.containers())

