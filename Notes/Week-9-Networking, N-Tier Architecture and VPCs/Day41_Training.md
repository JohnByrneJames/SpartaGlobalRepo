###### Sparta Global Training Day 41
###### Running our VM on Jenkins with automated testing

___

> 9:30 AM Academy Stand up [Morning]

No real blockers in terms of learning this weekend, however I did struggle quite a bit with getting the posts to work. Unfortunately I did not get it to work and am now going to work with someone to get it up and running for this mornings task.

I have been put into a group with Ibrahim and we are going to try complete the task together this morning.

I managed to get my posts working, I already had it set up for the most part but was missing a few small parts. I had to go to my security groups and add the port "**27017**" to my inbound rules, with the rule "**any**" this meant any inbound connections coming from this port would be allowed.

**27017** is the default port of mongodb. This worked when I went into my app instance and ran the command `npm test` which then ran the tests and actually ran the website.


### How does it work?

**CI**
* Job consists
* Triggers: push to dev branch
* Job: Installing packages running tests.


When we tell Jenkins to **Restrict build** we are asking it to the run the tests on a different node. In this case the `sparta-ubuntu-node`.

There is a node that is running on Jenkins that will always be using the same versions to the development server and will run the instance there.

![Image_ofJenkins_test_server](../../Images/AMI_JENKINS_TESTSERVER.PNG)

You can test what is actually running inside a VirtualMachine by clicking on the working directory.

**CI Deployment**

After successful job on Jenkins then it should automatically run the other job which will move the code from one server to another. (**Message**)

There was a small error inside our app folder, the problem we have is that the actual tests would pass and then after that it would not know what to do afterwards. So we needed to tell it to exit after it has completed the tests.

Go to **App**>**Package.json**

Then inside you need to change this line:

```javascript
"test":"./node_modules/mocha/bin/mocha"
```

into (add the `-exit` at the end)

```javascript
"test":"./node_modules/mocha/bin/mocha --exit" 
```

> 2:00 PM Jenkins Deployment [Mid-Afternoon]

We tried to automate the process of deploying the code from our git to the EC2 instance on our AWS. This will be automated using a job which will trigger another job to do the deployment using SSH and Rsync.

The first thing we did was download some code that Filipe sent in the chat. We placed it somewhere and unpacked it, then we removed its remote and added our own so we can succesfully push and pull from the [**repo**](https://github.com/JohnByrneJames/NodeAppPipeline).

**So far we have**
* Set up a git Repo
* Ran tests locally using Vagrant and OracleVM
* Setup CI ~ (JENKINS)
    - [x] **MUST BUILD IN AGENT NODE**
    - [x] **MUST ONLY LISTEN TO DEV BRANCH**
    - [x] **MUST MERGE CODE IF SUCCESS**
    
We set the webhook and then created a develop branch using the bash CMD:

```bash
git checkout -b develop
```

Once we pushed this to the GitHub it was checked by the Jenkins Job and this automatically merged it into the master branch.

The job I made was called **Eng67-John-NodeJS-v2** for the last part.

___

**Pushing build to AWS instance**

Using:

* `SCP`
* `SSH`

**Steps for SCP** into AWS EM instance.

1. Copy app
2. Copied the environment setup files (config and sh files)
3. we run these. Possible restart required.

We created the Job, then allows port 22 to be reached on the AWS instance inside my security group.
