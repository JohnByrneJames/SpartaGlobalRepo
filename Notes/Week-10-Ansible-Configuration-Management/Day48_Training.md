###### Sparta Global Training Day 48
###### Continuous with Ansible trying to perfect playbooks
___

> 9:00 AM Stand up [Morning]

Although I tried to finish my Ansible playbook and configuration the night before I could not and today is the day that I fix it!. No real blockers but I am going to consult with google and find out. Starting with bash shell scripts and then one by one changing them to more appropriate and robust yaml scripting expressions.

Useful command! 

```bash
# Get history of your bash
history >> history.txt
```

Today we worked a lot on the Ansible playbooks and how to automate the process
of provisioning our DB and APP.

## AWS

Next task is to automate the creation of our EC2 Instances on AWS using a AMI. I will document the steps later on in my [Ansible](https://github.com/JohnByrneJames/Ansible) Repository. 

* aws.playbook.yml
* var: AMI-id
* access_key
* secret_key
* MUST NOT
* Compromise the public API

**What is Ansible:**
What is Ansible
Simple - Agentless - IT Automation Tool
Ansible is a universal language, unravelling the mystery of how work gets done. Turn tough tasks into repeatable playbooks. Roll out enterprise-wide protocols with the push of a button.

**How does it work:**
Simplicity - Ansible functions by connecting via SSH to the clients

Agent-Less – There is no need to install a server and an agent that will pull the changes from it.

**Automation**
Since it uses SSH, it can very easily connect to clients using SSH-Keys, simplifying through the whole process. Client details, like host-names or IP addresses and SSH ports, are stored in files called inventory files. Its actions/tasks are defined in YAML files called Playbooks

**Why Ansible?**
It is Vital to know why should we use Ansible:
With its simplicity, ease-of-use, broad compatibility with most major cloud, database, network, storage, and identity providers amongst other categories. Ansible has been a popular choice of Engineering teams for configuration-management since 2012. Ansible can be used as a source control tool.

Best thing about Ansible is that you do not need to have advance scripting knowledge.

How does it fit into DevOps culture and practices:

The growing predominance of multi-cloud and hybrid cloud architectures
Ansible provides a common platform for enabling mature DevOps and infrastructure as code practices.
Ansible is easily integrated with higher-level orchestration systems, such as AWS Code-Build, Jenkins, or Red Hat.