###### Sparta Global Training Day 50
###### Continuing Terraform and looking at our new scripts to create more segments required in a VPC
___

> 9:30 AM Academy Stand up [Morning]

Today we have our Academy stand up with the whole current academy, we are going to go through what has been achieved this week with our representative Andrew.

> 10:30 AM Stand up [Mid-Morning]

We discussed about terraform and how it is a great orchestration tool. We are going to create a load balancer and scaling for our instances as this could make our application more scalable and highly available.

## Notes of Shahrukhs Video

**Docker** Containerization tool (Alternative to Oracle VMs)

**Kubernetes** Container orchestration tool
- if pod 3 goes down, it will load balance between pod 1 and 2.
- Kubernetes will automatically spin up pod 3 again with the same IP, and balance the load back onto it.

```bash
# t tag build
docker build -t <tag>

# p is port 
docker run - p <image name>

# Deploying kubernetes
kubectl run sparta <impage> --replicas=<no> --port<port>

kubectl expose deploy <tag> --port<port> --target-port=<target port> --type=<E.g. load balancer> 

# display pods running app
kubectl get pods

# expected to increase traffic
kubetcl scale deploy <tag> --replicas=<no>

# scale dependening on the usage (50%) > ECT (horizontal scaling, up and down)
kubectl autoscaling deploy <tag> --cpu-percent=<amount> --min=<no> --max=<no>

# get min and max of pods
kubectl get hpa
```

**Kubernetes Self-healing**

When a pod gets deleted or goes down, it is able to automatically spin the machine back up.

**Best practices**
1. Adopt micro-services architecture: start small with 1 or 2 services with small teams, test, learn and move on
2. Use Docker to containerise your apps for fast and consistent delivery
3. Orchestration with K8 to makes your life easy

**Why Containers over Virtual Machines**
[Good Website](https://www.docker.com/resources/what-container)

> 11:30 AM Load Balancer/ Auto-Scaling [Late-Morning]

## Why should we use auto-scaling

**Single Point of Failure**
* The single point of failure could be our database stopping, making our entire system stop. For example if a single database is supplying 5 different apps then it will crash all 5.

## Why should we use load balancer 

* A load balancer helps you maintain your instances, whether it be a front end webserver, backend database it actually distributes the load of traffic coming onto your servers between however many instances of that server you are running. For example using Kubernetes we are able to create 3 nodes running the same NGINX web app, effectively splitting the workload of each individual instance.

* A similar concept is the scaling, this describes the process of scaling servers servers resources up or down depending on the amount of traffic they are expected to cope for. There is also the concept of scaling out as well which consists of creating more duplicate instances and using a load balancer to distribute that traffic, effectively halving the work that instance has to do.

## Automating the auto-scaling and load balancing

* The task of auto-scaling and load balancing can be automated using tools orchestration tools such as Kubernetes along with containerized instances, typically done in the market leading tool docker. These containerized instances are much more compact than VMs and can run on a single OS, as a pose to each one having its own OS installed. Kubernetes is able to start up more instances of a web server when it is needed due to incoming traffic loads increasing and then spin down those instances when the traffic returns to a threshold.

## Health checks

## Monitoring with independent tools/ AWS could watch

## One to One Minutes

**One-to-One** with Shahrukh

- **We will time-box our meeting for 10 minutes**
- **Please take notes, as you will be expect to email us the summary of our conversations...**
- **How did you think this week went?**
>**"** I think this week went rather well, I have understood most of the concepts I think, but I feel like there is a lot for myself to look over in terms of the concepts as I think I would not be able to describe them in an interview to the level that was described by Shahrukh. I think the highlight of this week for myself was being able to automate provisioning with Ansible and also spin up rather complex infrastructure using code within terraform. I am looking forward to getting into docker as I am curious to see how containerization works, its something thats been bugging me from day 1 of the course, I always hear about docker so I can't wait to finally get my hands on it! 
>**"**
- From the behavioural competencies one competencies do you think you are excelling and which competencies you need to work one?
>**"** I want to carry on being motivated and Studious towards everything I do so that I can always be a life-long learner and someone who is always looking forward to learning something new and has a positive mindset whenever something new or difficult is put in front of them. This is the same as last week as I think I am keeping it up. However I need to work on my focus and priorities for sure, as I disappointed myself a lot when I really messed up in my interview practice with Filipe.
>**"**
- One thing to start doing? 
>**"** Start formulating lots of different answers that are in STAR form and repeat them, so if they come up in the quality gate I can easily retrieve it and then incorporate it into a example that will make myself look like I know what I am talking about.
>**"**
- One thing to stop doing? 
>**"** Stop getting strung up on particular tasks, let them go for the time being and be more in the moment. I was so annoyed that my VPC was not working on week 8 I neglected the fact I was in a interview and this lead to me seeming disconnected, however I have seen my error and am working to improve that.
>**"**
- One thing to continue?
> **"** Keep up the interaction I am having with the class so that I am present and always taking part with the discussion ECT.
> **"**

* **Positive feedback** <br>
>**"** 
>**"**

* **Constructive feedback** <br>
>**"**   
>**"**
