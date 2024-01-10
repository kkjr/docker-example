FROM python:3.10-slim

# RUN apt update \
#     && apt install -y <pkgs> \
#     && apt clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE <port>
# ENV <name> <value>

# argument, that can be overwritten by docker run
# CMD [ "arg" ]

ENTRYPOINT [ "uvicorn", "continuous:app", "--host", "0.0.0.0", "--port", "80" ]
