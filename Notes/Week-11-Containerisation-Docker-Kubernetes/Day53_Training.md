###### Sparta Global Training Day 53
###### Continuing with Docker and exploring deeper into its power
___

> 9:00 AM Academy Stand up [Morning]

We have been given a little more time to complete the docker exercise as it is not 100% working perfectly.

Try apt-get update/ apt-get upgrade.

Micro-services are great as they do not rely on anything if it needs refactoring or updating then it is easy to do so; as these containers are loosely coupled. If one is taken down then it will not break the entire application like monolithic may do.

This morning I was able to get it running with the posts loading, the issue was in that it is a production environment and I was trying to update the config file which made it a little confused. I am going to work on this in my own time to make it work a little more smoothly without the manual step of stopping, commenting out the seeding command then running again.

## Docker multi-stage production ready build

**Dockerfile** is the development environment

**Production environment** exists in container

We first created a Dockerfile that we ran using Node.

```dockerfile
    # Use the base image
    FROM node AS app
    
    # Define the working DIR inside the container
    WORKDIR /usr/src/app
    
    # Copy dependencies - If you don't know go to the documentation
    COPY package*.json ./
    
    # Install npm
    RUN npm install
    
    # Copy everything from OS to container
    COPY . .
    thspec 'README.md' did not match any files


    # Open up the port (3000) - Default port of Node.JS 
    EXPOSE 3000
    
    # RUN THE APP WTIH CMD
    CMD ["node","app.js"]
```

This was built on Git into a docker image, however when it built into an image: it was `1GB` in size.

```bash
docker build -t johnjamesbyrne/node-app-dev:v1 .
```

So to fix this we went with a magic line that only takes the essential parts of your image, this will be the parts that make your app work. 

```dockerfile
# Use the base image
FROM node AS app

# Define the working DIR inside the container
WORKDIR /usr/src/app

# Copy dependencies - If you don't know go to the documentation
COPY package*.json ./

# Install npm
RUN npm install

# Copy everything from OS to container
COPY . .

# Second stage of our build for production ~
# multi stage Docker build
FROM node:alpine

# Copy only essential things to this layer
# This line compresses the size whilst still providing full functionality
COPY --from=app /usr/src/app /usr/src/app

# Define work directory in second stage
WORKDIR /usr/src/app

# Open up the port (3000) - Default port of Node.JS 
EXPOSE 3000

# RUN THE APP WTIH CMD
CMD ["node","app.js"]
```

```bash
docker build -t johnjamesbyrne/node-app-prod:v1 .
```

This reduced the size by roughly `85%` to `144MB`. Below is the second layer we added into our Docker file that made these changes.

Then I pushed my new prod and dev images up to my DockerHub so they could be shared in the team chat.

___

Now we have been set the task of completing an end to end production pipeline using `On Prem` ➜ `GitHub` ➜ `Jenkins` ➜ `DockerHub` ➜ `Gmail webhook`