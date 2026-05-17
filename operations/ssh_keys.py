import time
from pyinfra import logger, host

from pyinfra.operations import server

start = time.time()
public_keys = host.data.public_keys

server.user_authorized_keys(
    name="keys for user", user="masum", public_keys=public_keys, _sudo=True
)

duration = time.time() - start
logger.info(f"Installation took {time.time() - start:.2f}s")
