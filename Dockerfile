#Specify the python docker image/container type you will like to use 
FROM python:3.8-slim

#Copy your project to a dir called app
COPY . /app 
#Change our working dir to the dir we copied our projects to
WORKDIR /app
#It is conventional to put your env or additional installations into an opt folder and your venv is one of them
RUN python3 -m venv /opt/env 

#Run your requirements install by locating the where the pip is in your env---> /opt/env
RUN /opt/env/bin/pip install -r requirements.txt 

#Locates your venv,, activates it so you can run django related commands
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]

 
