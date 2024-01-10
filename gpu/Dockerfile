FROM nvidia/cuda:12.3.1-runtime-ubuntu22.04

RUN apt update && apt install python3 python3-pip -y

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE <port>
# ENV <name> <value>

# argument, that can be overwritten by docker run
# CMD [ "arg" ]

ENTRYPOINT [ "python3", "-u", "gpu_onetime.py" ]