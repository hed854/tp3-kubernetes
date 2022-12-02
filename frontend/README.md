# basic frontend

params.env only for local docker use

from root dir

```
docker build -t frontend frontend
docker run --env-file=frontend/params.env --network=host --rm -it frontend /bin/bash
```
