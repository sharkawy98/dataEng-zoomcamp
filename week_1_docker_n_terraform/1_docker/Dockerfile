# base image
FROM python:3.9

# download and install dependencies
RUN pip install pandas

# tell the image what to do when it starts as a container
WORKDIR /app
COPY pipeline.py pipeline.py

# cmd
ENTRYPOINT [ "python", "pipeline.py" ] 
