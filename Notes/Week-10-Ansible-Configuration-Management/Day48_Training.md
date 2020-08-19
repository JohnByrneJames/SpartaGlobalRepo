###### Sparta Global Training Day 47
###### Continuous with Ansible trying to perfect playbooks
___

> 9:00 AM Academy Stand up [Morning]

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