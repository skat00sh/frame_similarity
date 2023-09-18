FROM python:3.10

WORKDIR /code

COPY . /code/
# Docker has issues with libgl, hence this quick hack to make opencv works
# RUN pip install opencv-python-headless 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code
CMD ["python", "src/main.py"]
