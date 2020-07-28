###### Sparta Global Training Day 32
###### Continuation of Vagrant and Oracle VM box
___

> 9:00 AM - 9:30 AM Stand-up [Morning]

Yesterday went well, I enjoyed learning about Linux and its intricacies. It is clear to see why it is a preference for
the DevOps role due to its ability to do almost anything inside its OS and ease of use, particularly how easy it was to
download and set up the **NGINX** server. I would like to know how to host the server publicly from inside the virtual machine too
but I think I will look into that eventually.

Enjoying the completely command line based environment, it makes sense as it is directly talking with the computer
which significantly increases the speed at which the processes are carried out. It also is quite exciting to
work without a GUI as it makes you feel more technical.

> 9:30 AM Training in VM [Early-Morning]

**Moving Folders from OS to VM**

Today we will discuss how to move folders and files from our own OS to the VM we are setting up.
We have a folder with a folder called app, we want to move that into the VM. so inside out `VagrantFile` we add the following
line:

```bash
config.vm.synced_folder "app", "/home/vagrant/app"
```

As this is a new folder, we first need to initialise the VM, to do that we are using the:

```bash
vagrant up

vagrant status

vagrant ssh
```

Once we are inside the VM we then ran the command `ls` which displayed our app folder inside the VM.


**Common Questions of DevOps in industry**

Communication with the developers when they hand over a software, there are some common questions.

* Communication is key to successful projects communication between DevOps testers QA and DevOps.
* What language is used build in the app?
* What framework has been used?
* Are there any dependencies to be installed together together
* What will the app look like?

**Requirements**
* Node app requires nodejs to be installed
* Ruby to be installed to run the tests

**Now we are going to try run some tests**
From the base file, we navigate `/D/VM_SecondEnv/Environment/spec-tests`

We then had to run a the following command:

```bash
bundle
```

This did not work as it required some dependencies that we didn't have. In order to fix this we needed to install that
dependency using the following command:

```bash
gem install bundler
```

This then said that 1 gem has been installed. The gem install is a ruby module, and it installs everything needed.
After we installed the bundle, which finished with the message: `Bundle complete! 2 Gemfile dependencies, 16 gems now installed.`

Now we are going to run a test known as `rake spec`, we are expecting tons of errors. In the spec-tests file
there is a file called Rakefile that contains all the tests that are going to be run. This file ran 9 tests, 7 failed
and 2 passed which were the ones testing for `Git` installation which is true.

Now to satisfy the tests that have failed we need to install and run both **NGINX** and **NODEJS**

```bash
apt-get install nginx
systemctl status nginx
```

After that we need to install **NODEJS**

```bash
sudo apt-get install nodejs -y
```

This has then returned the tests at success, it says there are only 2 failures. So we are to correct 1 by installing `PM2`.

To do this I first had to install a package called npm with the following command:

```bash
apt install npm
```

Then after that I went on to install pm2 with this command:

```bash
npm install pm2 -g
```

This loaded a bunch of files and installation packages that made up pm2 and then when I ran the `rake spec again` I only got 1
failure which was to do with the version of node.js.

**Going through with Shahrukh**

We first added python download:

```bash
sudo apt-get install python-software-properties
```

This makes sure that the most recent software versions are installed across the board. Now we are installing a curl dependency.

```bash 
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
```

```bash
sudo apt-get install -y nodejs
```

The last two commands help to get the software versions up to the latest, then again we run the command:

```bash
sudo npm install pm2 -g
```

This will run the pm2 installer again and with the latest software properties and setup that we set up it should
install the correct version to satisfy the last test failure. Which is the "pm2" is expected to be installed
by "npm".

Then we used the command:

```bash
sudo apt-get upgrade
```

After that we have now satisfied all of the examples, and receive the message `9 examples, 0 failures`

**Now we are going to try run the app**

The app we were given is stored inside the app file. This app file has a node app and to run it we need to install
any dependencies that may be required. The first thing we need to do is navigate into the app folder.

```bash
cd app
```

First we are going to install the `npm` package manager using the following command:

```bash
npm install
```

**Side Note** to check the version of the node use the command `node --version`

### Running the App with NodeJS

To run the app, whilst inside the /app directory use the following command:

```bash
node app.js
```

This returns `Your app is ready and listening on port 3000` which is a successful run.
This app is then accessible on the URL: **`http://development.local:3000/`**

![ImageOfConnection](../../Images/DevOps_RunningOnPort3000.PNG)

> 9:30 AM Finishing installing and going through Process [Afternoon]

The README.md inside the app directory contains some instructions on how to access different parts of the website and use it.
When the app is running use the `Ctrl+C` to exit.

Inside the `app.js` file we can see how the website is used. It talks about the instance being created, as well as the other parts of
the website that is included. The port which is 3000 as well as its message.

Inside the `package.json` there is a list of dependencies that are required in order to actually run the program, what
frameworks are being used, the main file it is running on ECT..

To access any of these files we use the `nano` text editor inside the VM. We do not need to understand the files and
functionality 100% but we need to be able to have a good idea of **WHAT** and **HOW** the app is working.

**Next** we go back to the root directory with `cd ..` and use the command:

```bash
touch nginx_installation_script.sh
```

Now we need to change this file into a executable file. This means we need to change the permissions of the file.

```bash
chmod +x nginx_installation_script.sh
```

This is now an executable and will come up as a green file when you use the `ls` command in the terminal. To run this file you use the
command:

```bash
./nginx_installation_script.sh
```

This won't run at the moment as there is nothing inside the file at the moment. We are going to try automate processes now inside this file.
This means it is going to automate a process that would usually take someone 2 to 3 hours.

Inside this file we entered the following:

> do apt-get update
> do apt-get install nginx
> do apt-get upgrade

Now to test this we are going to remove **NGINX** and then run the file we just made so it can automate the process of installing the
**NGINX** package.

```bash
sudo apt-get remove nginx
```

then we do our new automated installation bash file to install all the **NGINX** dependencies along with the updates using:

```bash
./nginx_installation_script.sh
```

This successfully installed the **NGINX**. As you can see this a very powerful way of making the installation process a lot easier.
For example if you were instructing a client or colleague to install the software, you could simply give them the `.sh` and ask them to run it
which would automatically install all and any dependencies that they may need. Effectively automating the process entirely. 