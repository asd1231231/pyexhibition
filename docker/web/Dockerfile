FROM centos/python-36-centos7
ADD . /docker
RUN pip install -r /docker/requirements.txt
CMD ["python", "main.py"]
