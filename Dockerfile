# slim- light weight version of python image
# this gives our container a python runtime 
FROM python:3.14-slim

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# Document the port used by FastApi to run 
EXPOSE 8000

# command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
