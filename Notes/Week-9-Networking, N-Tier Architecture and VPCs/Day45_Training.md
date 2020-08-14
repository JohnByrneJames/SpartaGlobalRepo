###### Sparta Global Training Day 45
###### Fixing and getting the DB and APP to work with the VPC on AWS
___

Yesterday was quite a long day, I spent most of it trying to get my posts to load and the database loaded on the private subnet. However it never really worked, so I am going to use today to try fix that as I have to record a video of how the process is done for the weekend.

Today I have my interview to prepare for. I am at 1:45 PM with the Trainer **Filipe** it is mock Quality gate in preparation for the upcoming real one next week where the trainer will decide whether we are ready to be put into the employment pool.

1. Tell me about yourself

# EC2
- Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic. 

#AWS
- This is Amazons own web services platform for cloud computing, they offer over 175 fully features services. It offers a large range of secure architectures like the VPC which can be configured with its own VPC and network route.
    
- Amazon web service is a platform that offers flexible, reliable, scalable, easy-to-use and cost-effective cloud computing solutions. 

# Load balancer
- Load balancing refers to efficiently distributing incoming network traffic across a group of backend servers, also known as a server farm or server pool.
    
- **Benefits of Load Balancing**
   - Reduced Downtime
   - Scalable
   - Redundancy
   - Flexibility
   - Efficiency
   - Global Server Load Balancing

# AMI
- AMI stands for Amazon Machine Image. It provides information required to launch an instance. You need to specify an AMI when you launch an instance. You can launch multiple instances from the same AMI with the same configuration. 

# What makes a good devops engineer?
- Someone who is an all rounded individual who has the ability to be studious in any task they undertake, retain and practice that knowledge and be able to effectively communicate it to non and tech savvy individuals. 

- **LIST**
    - FLEXIBLE, ROBUSTNESS, EASE OF USE and AUTOMATION
     - SECURITY SKILLS
     - COLLABORATION
     - SCRIPTING SKILLS
     - DECISION MAKING
     - INFRASTRUCTURE KNOWLEDGE
     - SOFT SKILLS, TEAM WORK, GOOD COMMUNICATION AND MARKET KNOWLEDGE.
     
# Isn't Devops just agile
- No Agile is a methodology that uses tools like the SCRUM framework to accomplish an iterative environment within a software development project, but DevOps makes use of these tools as a whole to create links between Development and Operations as well as communicating these processes to stakeholders and automating processes where possible.
    
# What is SQL
- SQL also known as structured query language is a domain-specific language designed for managing data in large amounts. Its main purpose is to provide a easy and effective way to store large amounts of data with high data integrity and security.
    
# SQl joins
- SQL joins are a concept found in a relational database, it combines one or more tables in various ways to compare data within those tables either to the left or right or to itself. 


# Scrum
- SCRUM is a framework where people can address complex adaptive problems, while productively and creatively delivering products fo the highest possible standard.
    
- **Scrum artefacts**
    - Product Vision
    - Sprint Goal
    - Product Backlog
    - Sprint Backlog
    - Definition of Done
    - Burn-Down Chart
    - Increment
    - Burn-Down Chart
    
# Burndown chart
- Burndown charts are graphs that give an overview of progress over time while completing a project. As tasks are completed, the graph “burns down” to zero. It is used as a tool to guide the development team to a successful completion of a Sprint on time with a working final product.  If a team decides they have moved more objectives than possible for completion from the Product Backlog to the Sprint Backlog, the Burndown Chart can aid them is ascertaining which tasks they are not realistically able to complete so that these task can be moved back to the Product Backlog.
    
# velocity chart
- Velocity is an extremely simple, powerful method for accurately measuring the rate at which scrum development teams consistently deliver business value. It is an indication of the average amount of Product Backlog turned into an Increment of product during a Sprint by a Scrum Team, tracked by the Development Team for use within the Scrum Team. Thus, to calculate velocity of your agile team, simply add up the estimates of the features, user stories, requirements or backlog items successfully delivered in an iteration. It should the team:
    - Predicting how much scope can be delivered by a specific date.
    - Predicting a date for a fixed amount of scope to be delivered.
    - Understanding our limits while defining the amount of scope we will commit for a sprint.

# sprint review
- THis is one of the SCRUM EVENTS
- It what takes place at the end of a sprint and is a time-boxed event where the team inspects the increment and adapt the product backlog if needed. Anything not completed will be either left in the backlog or removed ECT.
    - **SPRINT EVENTS**
    - SPRINT PLANNING
    - DAILY SCRUM
    - SPRINT REVIEW
    - SPRINT RETROSPECTIVE

# customer collaboration feedback in scrum
- This usually takes place during a Daily SCRUM the customer who is one of the stakeholders will be asked for their feedback on the product or product so far and their thoughts, suggestions and criticisms will be taken into consideration when thinking about what is next needed for the project. This helps the product be more adapted to what the customer wants.
___


- REMOVE:  I THINK, IN MY OPINION and MAYBE (NON ASSERTIVE COMMUNICATION)

- NOT CONCISE
- PROGRAMMING PSEUDO CODE WITH EXPLAINING
- LOOKS LIKE I AM READING FROM NOTES
- STAR

**FINISHED**

- `npm start app.js`