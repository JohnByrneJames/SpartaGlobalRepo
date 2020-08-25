###### Sparta Global Training Day 52
###### Continuing with Docker and exploring deeper into its power
___

> 9:00 AM Academy Stand up [Morning]

I completed the exercise of creating my own repository on docker hub and then adding an image to it and pulling it down to my pc. No blockers particularly and I am looking forward to the rest of the day.

**Exercise**

1. We are going pull our image we have on our docker hub.
2. Then see it in the browser to see if it is working.
3. Get a colleagues image from their Repository.
4. run it and then view it in the browser.

If you want to delete an image in docker.

```bash
# Delete a docker image (-f = force)
docker rmi <image_name> -f

# Delete a docker container 
docker rm <container_name> -f

# Deleting my own image
docker rmi johnbyrnejames/john-eng67

# pulling down my image again (:latest = version)
docker pull johnbyrnejames/john-eng67:latest

# Check if the image was pulled successfully
docker images

# create a container and run the image in detached mode
# run it on port 99:80 as port 80 is already in use for me
docker run -d -p 99:80 johnbyrnejames/john-eng67:latest

# Pulling maxes image from Docker Hub
docker pull max476/max-docker-first:firstcommit

# creating this as a container and access it through port 100
docker run -d -p 100:80 max476/max-docker-first:firstcommit
```

* What is Docker? It is an open source platform for containerisation

* What is the difference between VM and Docker? Docker is Lightweight compared to VMs. Docker shares the memory of a single OS rather than creating an entire virtual environment.

* Why does Benefit us? Fast, consistent delivery of your applications.

* Who is using Docker? 50% of the industry are using it; trend setters like Facebook, Google, Apple adopt these then they become popular in the industry.