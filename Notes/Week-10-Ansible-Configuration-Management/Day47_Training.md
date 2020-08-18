###### Sparta Global Training Day 47
###### Further work into Ansible...
___

> 9:00 AM Academy Stand up [Morning]

I couldn't get the web page to come up, unfortunately I haven't actually got
 the web page to load as the playbook is having a lot of issues and the internet is running extremely slow.

**Shell** is a backup for playbook scripting and it should be not used as much, we should use templates more often.

You can add `--check` at the end of a playbook to check syntax.

* export DB_HOST="mongodb://109.10.2.78:27107/posts

* Today I have set up my APP and DB working with Ansible
* The next iteration is to automate the process of logging into AWS, and using a EC2 instance all done by Ansible.

**GitHub**

We need to actually get a SSH connection that is authorized from within our AWS machine.

**Ansible is Infrastructure as Code** and **Terraform**  orchestrates it.