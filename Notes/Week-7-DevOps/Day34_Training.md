###### Sparta Global Training Day 34
###### Continuation of Vagrant and Oracle VM box

---

> 9:00 AM - 10:00 AM Self-revision and Standup [Morning]

This morning we have actually went ahead and completed the **NGINX** reverse proxy task which was quite interesting
and rather straight forward. Now we have been set the task of going into our directory and automating the process of
automatically creating this reverse proxy task. We are now fully automating the process of setting up the two virtual
machines. One with the database and another with the development server.

Today was spent mostly debugging my Virtual machine as it kept coming up with the same error:

>Stderr: VBoxManage.exe: error: The virtual machine 'VM_SecondEnv_default_1596123246559_92823' has terminated unexpectedly during startup with exit code 1 (0x1).  More details may be available in 'C:\Users\jonjo\VirtualBox VMs\VM_SecondEnv_default_1596123246559_92823\Logs\VBoxHardening.log'
>VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component MachineWrap, interface IMachine

Unfortunately as a result the DOD for today has not been achieved and there was little help around, my colleagues were unsure as was
Richard so I am going to use tomorrow to do further research into the problem.

**BY Default NGINX listens on port 80** However the Sparta global website is actually on port 3000.

**First**

go to the default file through the route `/etc/nginx/sites-available/default`

**Second**

go inside the sites-available folder and use the command:

```bash
sudo rm -r default
```

**Third**

create the file using the command:

```bash
touch default

nano default
```

**Finally**

Inside the default file write the following:

server {
    listen 80;
    server_name _;
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

Now you can connect to the sparta global node.js app without the port