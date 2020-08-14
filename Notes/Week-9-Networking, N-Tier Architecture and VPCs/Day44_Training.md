###### Sparta Global Training Day 44
###### Looking at the Node App on our VPC public subnet instance and 
___

> 9:00 AM Academy Stand up [Morning]

I have no blockers, I have the app working on my VPC App instance. It works as expected with a weird host error but still runs the node app and I am able to connect to it. I will keep the error in mind and try resolve it later on once I have my current set up fully documented so that if I need to I can easily refer back to it.

**Today** we may have **Interviews**. These are only mocks but they are still quite important and may involve a lot of important information that will be asked in the real ones.

**We Have been tasked to create a DEMO VIDEO**:

It can be seen on this [**card**](https://trello.com/c/M0to4ePp/207-making-small-demo-videos) on the trello. This can be recorded and shown to the client later.

**Difference between**

**Private and Public Subnet**: Private has no internet and public has access to the internet.

The Gate surrounding the Subnet is the **NACL** and the Security Group is the gate that is surrounding the **Instances** for example the App EC2.

The App is quite unsecure, so you don't want to put your data there really. Then the Bastion is also quite tight on security but is just another server therefore it makes more sense to put the database on a private subnet so it cannot be accessed via the internet. The Bastion is a way to access the DB securely through port 22.

| Metric        | **NACL**                                                                                                                                                    | **SG**                                                                |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **JOB**       | Filter INCOMING and OUTGOING traffic into a subnet                                                                                                          | Filter INCOMING traffic to a instance                                 |
| **Location**  | At Subnet level                                                                                                                                             | At Instance level                                                     |
| **RULES IN**  | _By Default Deny Everything_  Rules Numbered: (Should be broader than security groups)                                                                      | _By Default nothing allowed, you need to specify_                     |
| **RULES OUT** | _By Default Deny Everything_  Should you need to specify what goes out.  This means they are stateless: They do not remember what came in as to let it out. | _By Default allows everything out_  No need to worry, it is stateful. |

**Web app SG**
* Open Port 80 on 0.0.0.0/0
* Open port 22 to your IP
* Open 443 to 0.0.0.0/0
* Open ephemeral port to 0.0.0.0/0

**Interview**

* **2 PM** Tomorrow


**LIST OF USEFUL COMMANDS**
* scp -i ~/.ssh/DevOpsStudents.pem -r environment/ ubuntu@109.10.2.78:/home/ubuntu
* ssh -i DevOpsStudents.pem ubuntu@109.10.2.78

Finished Today, was a lot of revision and trying to get the DB and APP to work on our new VPC. Find more information [**HERE**](https://github.com/JohnByrneJames/Network_VPC_setup)

**My Steps**
1. Add a public SSH into the Database instance for my IP inside the Private **NACL**
2. Added my IP to the VPC DB security group, allow my IP to SSH into it.
3. Added Internet to the Route Table, private 
4. Added HTTP and HTTPS links into the Private subnets Instance and subnet to allow internet temporarily (Port **80** and **443**)
5. SCP from OS to bastion and then into private DB
6. Run DB inside db instance inside VPC, make sure it is running
7. Exit back to OS, SCP in App provision folder. SSH into App instance inside VPC public subnet and run app provision
8. Run **NPM install** and **NPM Test**