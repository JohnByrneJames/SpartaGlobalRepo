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

