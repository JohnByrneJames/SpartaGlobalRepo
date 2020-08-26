###### Sparta Global Training Day 51
###### Starting working with containers in Docker and seeing how they are so amazingly beneficial
___

> 9:30 AM Academy Stand up [Morning]

No real problem with any of the exercises in Terraform, but I could not test my work as the credentials for AWS had expired when I tried to plan it. I am not 100% sure that it works but when we get some new keys I will then test and develop it further.

This week is for Quality gates, either on thursday or friday and am looking forward to it but a little nervous for the quality gates. We have a task on the Trello board that has a presentation task.

> 10:00 AM Presentation [Morning]

**We need to create a presentation** with the following topics:

1. **DNS**
2. **Types of Records**
3. **A Records**
4. **CNAMEs**
5. **Alias'**
6. **MX Records**
7. **TTLs**
8. **Propagation**

* _Find the Powerpoint [Here](../../Documents/Route53_and_DNS_Reverse_Group_3.pptx)_

* Other group powerpoints [Here] and [Here]

_**Group with ~ Max, Mehdi and Andrew**_

## Using Docker

**1.** To check if docker is installed enter the following command

```bash
# prints out list of command
docker
```

**2.** Create a container 

```bash
# Create a container
docker run hello-world
```

**3.** This gets an image for the container

```bash
docker run ahskhan/nginx-test-rp-app
```

Now we did, pull nginx image from docker hub

```bash
docker pull nginx
```

**4.** To view the images or anything we download we can view it by typing

```bash
docker images
```

**5.** We ran a web app using NGINX using shahrukhs image on Docker hub, it created a container from an image

```bash
docker run -p 80:80 ahskhan/nginx-test-rp-app:v2
```

**6.** To check if the image is working.

```bash
docker ps
```

**7.** To force delete the container use

```bash
docker rm adc97af51da3 -f
```

**8.** You can create containers very fast with any images that you have previously used.

```bash
# view images
docker images

# run it in the browser with port 80:80
docker run -p 80:80 nginx
```

**9.** port mapping allows us to have it also on port 90 like so

```bash
docker run -p 99:80 nginx
```

Then we can search `localhost:99` in the browser and see NGINX running.

**10.** Run the container in detached mode. Running this as detached allows you to edit/ configure the container whilst it is still running.

```bash
docker run -d -p 80:80 nginx

alias docker="winpty docker"

docker ps -a

docker exec -it <id of container> sh

docker exec -it <name of container> sh
```