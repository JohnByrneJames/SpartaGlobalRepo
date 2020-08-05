###### Sparta Global Training Day 38
###### Continuous Integration and delivery this week (**_JENKINS_**)

___


> 9:30 AM - 10:00 AM Self-revision and Standup [Morning]

Today we are starting on Jenkins with Filipe, but first we had a stand up. I personally had no blockers yesterday apart from the fact
that my laptop is not able to run the virtual machine software using Vagrant. Therefore I have got my big computer and
am going to set that up later tonight when I have more time.

* To add to VM_Proxy Repository 

* **Add part telling user how to access the code**
* **Add Development environment Note, talk about the environment**

> 11:00 AM Hopefully starting with Virtual Machine in Jenkins and AWS [Late-Morning]

**Theory**

Think we are going to do some more theory first of all.

**SDLC** Traditionally, could take up to **1** year to complete. For example **1** year for windows to produce the Windows 95 CD.

Then it could take them **2** years developing patches and fixing bugs for that previously released windows 95. **$$$$** when product is released/ Deployed to customers.

___

**Next** Dev Cycle **2000** - **2010**

It would take **3** months to develop, **3** months of testing and then a further **1** month to deploy the product.
Here you get **$$$$** earlier 

___

_**ERA** of Agile/SCRUM_ - **2011** - **Present**

**Dev Cycle** is now only **4** weeks, but the testing still takes **3** months and the deployment still takes **1** month. **$$** is got a little earlier,
2 months earlier.

_**ERA** of Agile/SCRUM with **Devops**_ - **2011** - **Present**

**Dev Cycle** is now only **4** weeks, and the testing and deployment steps are usually now fully automated, it can take **10** minutes or even seconds
to test and deploy a product. (Obviously dependent on infrastructure). **$$** made much earlier and continuous due to constant updates
and extra services .. **$$** ... **$$**. ↔

**AWS** has everything **IAAS**, **SAAS** and **PAAS**

## AWS and Jenkins

Creating a Jenkins_Account

We went to Our Jenkins [Login](http://jenkins.spartaglobal.academy:8080/)

I created an account and we got a log in

Then we created a new directory in our folder called `web_app_starter_code` where we unzipped a file
that filipe sent us. Inside the terminal we initialised the git repository and added two lines to the `.gitignore`.

```bash
echo "app/node-modules/" >> .gitignore 
echo "*.log" >> .gitignore 
```

Then we linked up the folder with this [repository](https://github.com/JohnByrneJames/WebApp-CI) on my GitHub.

Now on Jenkins we made a job through the new tab, then we clicked `Freestyle job` and called it `eng67-john-ci-job`.

**Notes**
* **Jenkins** Has..
    * **JSDK 8**
    * **Python**
    
 Then we configured the settings of the Job with our Test server credentials and a link to the Repo where we have the project.
 Also a key that can be used to deploy.
 
**Now we are setting up the key**

This key will be used on our github to allow Jenkins to communicate with GitHub. We are going to be doing this in two different ways,
one is considered an easier way and one is a harder way. We first generated a SSH key using this [**SITE**](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

We then give the private key to **Jenkins** so it can communicate with **GitHub** when we eventually give it the public key of the **SSH** key pair.

We are now making a web hook and attaching that too - this is an inverted API call, so github makes a call to Jenkins and it carrys out an
event. Then we added the option:

`Provide Node & npm bin/ folder to PATH`#

and then added an extra build step for `Execute Shell`

```bash
cd app
npm install
npm install
```

Once everything has been set up correctly Jenkins will be listening to your master branch of GitHub and will be automatically called
to carry out that specific job every time a commit is made to that readme. The web hook tells the jenkins server that a change has taken place,
triggering the job. So every time you make a change to your github history a test will be carried out on that version.

**Task**

# Jenkins CI Lab

## Summary

Our current CI setup on Jenkins has one major flaw. The build is currently started and the tests are run on the master branch of the repository. 
This means that if the tests fail the code still exists on the master branch ( which is only supposed to contain working code ).

We need to reconfigure the job so that the code is tested on a different branch ( develop ) and automatically merged with the master branch if the tests pass.

The developers should also be informed on Github if their commit passed the tests or not and they should be notified via email too.

## Tasks

* Configure your job to checkout code from the develop branch rather than the master branch
* Have the job merge the develop branch code with the master branch and test against that
* Use the Git publisher plugin to push the master branch to Github if the tests pass.

## Tips

All of these items are simple configuration provided by plugins that are already installed and setup on our Jenkins instance. If you are writing code you are doing it wrong.

You will need to research how these plugins works:

* The Github plugin
* The Git publisher plugin

**Acceptance Criteria**

**Steps**
* 1 - Go to the the job and select `Configure`
* 2 - Go inside the Repo and replace the branch with `develop` or the name of the development branch
* 3 - 