###### Sparta Global Training Day 37
###### Continuous Integration and delivery this week (**_JENKINS_**)

___

> 9:30 AM - 10:00 AM Stand up [Morning]

We looked at our usual blockers and good moments from yesterday and then we went onto
prepare for our presentations which we are having at 10:00 AM once we have rehearsed within our
groups.

> 10:00 AM Presentations [Morning]

We did the presentation, it went well and I think we got the information across in a good time
as we were time-boxed for 10 minutes. We presented from 10:20 - 10:30.

Luckily we do not need the Virtual Machine to be working at the moment, however it is important that it does work - So I plan to restart
my computer from factory settings later on in the evening. The presentation can be found [**HERE**](../../Documents/Presentation_CI_CD_CDE.pptx)

Today we went over the Reverse proxy work that was carried out last week, unfortunately my computer has actually let me down and has lots of problems running the virtual machine so I cannot demo what I can do
until that is fixed.

**Instructions for writing the README.md** for NGINX Proxy

* On Trello use this to get the DOD done [**HERE**](https://trello.com/c/wVPY6r9j/161-nginx-reverse-proxy-lab)
* Pre-requisites (VirtualBox, ECT..)
* Git cloning (How to git clone the repository instead of download the zip)
* Why we are creating it through a Virtual Machine (keep it separate / Linux is the fastest, it is everywhere / It is used almost everywhere [Uniform environment for everyone])
* Always imaging the user has 0 knowledge of the steps and technology they are about to use, this makes for a very comprehensive set of instructions for a user at any level.
* Best practice is to get rid of the default file created by **NGINX** and inject your information into a config file.
* Either do the export `DB_HOST>..` in the `VagrantFile` or in the `Provision.sh`.
* When doing the **Unlink** it is better to remove instead. But make sure it works then add this addition.

> 16:00 PM Stand up [Late-Afternoon]

**Jenkins** and **AWS**