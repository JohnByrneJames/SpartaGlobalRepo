###### Sparta Global Training Day 2
###### Communication
___

> 9:00 AM - Daily Stand Up **[Morning meetup]**

Discussing what we liked about yesterday and waht the highs and
blocks were of that day. 

- I enjoyed the fact that we learn about active listening and how
important it is to truely **LISTEN** and understand someones point.
This raises the point that it is positive to listen twice as much as
you talk. 

- I also enjoyed the **perato principle**, which is also known as the **80/20
principle** which says that everything is not as it seems or as it comes across.
For example in Italy; 80% of the population occupy only 20% of
the country. 

- I found that properly listening and using the concept of **active-listening** is
an essential part of being a good listener and can actively improve
every part of your business.

___
> 9:10 AM - Install Git and PyCharm and create a GitHub Account **[Morning]**

- What is **git** - it is a version control software that allows large projects to be
structurally saved throughout development and also help people work on different
parts of a project. 

- **GitHub** is stored on the cloud and is available to be cloned to any machine at any time
in any place. 

* **Initializing the Repo**
    * First of all create the repo in the **GitHub** Repositories tab on **www.Github.com**,
    you **must** create a repository with the exact name as the folder you are using on your 
    local machine.
    * Create the Repository in **GitHub** and copy either the `HTTPS` or `SSH` git links for the 
    next step in create a remote repository. 
    
___
> 12:30 PM - Afternoon Meeting with Richard **[Afternoon]**

- **Richard** is a Technical Delivery manager in Sparta Global and told a little about himself as well as 
answering some of our questions. I found out that he prefers **Command-Line** based Git rather than that
on a **GUI**.

___
> 12:45 PM - Continue Git and PyCharm Set-Up **[Afternoon]**

In the **PyCharm** `Terminal` we are to enter some commands to initialise our Repo on the **local machine** and then
establish a **remote connection** with the Repository we just made.
* **Terminal :**
    * `init git` initialises the Repo on your local machine
    * `git add .` stages your files that are in the project
    * `git status` get the status of the files, whats stages and also view the changes that have been made.
    * `git commit -m "Your message"` commits the changes to the local machines **Repo**
    * `git remote add origin git@github.com:JohnByrneJames/com_3.git` The last part is the address of your **Repository**
    * `git push -u origin master` This will finalise the changes and push it to your remote copy on **GitHub** which will
    be saved to the **cloud** and can be accessed from anywhere!
    
 ___
> 12:45 PM - Create SSH Key for easy and secure connection **[Mid-Afternoon]**

This allows access from the **local** repository to the **remote** one easier as it can be done automatically by exchanging
a public key that allows your **GitHub** to identify your computer. This is done by comparing your **public** to the stored 
**private** key on you computer.
* **Git Bash:**
    * Go to `Git bash`
    * `$ ssh-keygen -t rsa -b 4096 -C "Your Email"` This generates a SSH Key pair for your computer
    * `Passphrase Enter : (Twice)` Optional passphrase
    * `eval $(ssh-agent -s)` Start the SSH Key Agent using this will produce the pid of your key
    * `ss-add ~/.ssh/id_rsa` This wil add your SSH key to the SSH agent, `is_rsa` is to be replaced with your 
    chosen key name _(This is chosen as the start)_
    
* Add **SSH Key** to your **GitHub**
    * `clip < ~/.ssh/id_rsa.pub` this will copy the keys public ID to your clipboard **(ctrl+v)**
    * `GitHub.com > Profile > Settings > SSH and GPH Keys > New Key` Navigate the the **GitHub** SSH
    Key settings tab
    * `Title > Paste in Public Key` Add this key and it should be possible to add your SSH connection string when 
    committing changes in your **CMD** (May require Git **Email** and **Password** on initial use)  

___
> 15:35 PM - Communication 2 (Continuation from previous Day) **[Mid-Afternoon]**

* **Objectives**
    * Understanding situations
    * reacting appropriately
    

Different opinions within the workplace is inevitable, but knowing how to react
in the right way can avoid conflict.
- Miscommunication
- Different goals or priorities
- Stress
- Resource Limitations
- Personality Clash
- Styles of Thinking or working

* **Nullifiers**
    * Value harmony, positive relationships, don't want to hurt feelings, stabilise
    team dynamics
    
* **Seekers**
    * Eager to engage in disagreement, directness, honestly, lose patient when
    others aren't as direct, doesn't mind destabilising teams.
    > **"** Not every situation requires a reaction - Some can be rhetorical and are to
    inform you of potential happenings rather than prompt a reply. **"**
                                                                                                                                                                                                                                                          
Using these **Scenarios** we can identify acceptable behaviour in the workplace
* **Scenario 1**
    * Working within the same department, yourself and other colleagues have
recently noticed a team member is reluctant to take on new ideas and is
unwilling to accept criticism. What should you do?
    1. Ask the colleague who is the closest to them to talk on a one-to-one basis
    2. Inform the manager to take this further
    3. Hold a group meeting to share your concerns with this individual together
    
Question **i** could escalate the situation which is counteractive to what you want,
therefore **iii** could be the best course as it allows a constructive discussion among peers
and colleagues can voice concerns - if it does not resolve it then it can be escalated to **ii**.

* **Scenario 2**
    * You're leading a small team. 2 members seem to have different working Styles
which is causing tension across the team. How would you resolve this?
    1. Don't intervene and let the 2 employees resolve it between themselves
    2. Call the 2 employees for an informal conversation
    3. Arrange a formal meeting o take this further
    
Try calm the situation down and choose the option that will satisfy both parties, as well as keep
the situation calm and collected. **Listen** to what is being said and find the **facts** in
order to make a sensible decision. option **ii** allows it to be remain private, and perhaps
come to a conclusion that suits everyone, however if it does not then **iii** could be more suitable.

* **Tips**
    * Stay Calm
        * Understand their perspective
        * Don't assume
    * Treat them with respect
    * Don't push blame
    * Take responsibility
        * You may be wrong
    * Adjust tone of voice/ body language to best suit the situation

___
> 16:10 PM - Communication 2 Continued... **[Late-Afternoon]**

* **5 Minutes Group Work**

Discuss in a group what NLP stands for and what types of it exist as well as 
the benefits it can have.

**Neuro-Linguistic programming**

* **Defenition** : **Neuro-linguistic programming** (NLP) is a psychological approach that involves
**analysing strategies** used by **successful individuals** and applying them to
reach a personal goal. It relates thoughts, language, and patterns of
behaviour learned through experience to specific outcomes.

* **Neuro**-Linguistic-Programming
    * First Access - (Mental map of the world)
        * How we view and relate to the world
        * No two people have the same experience
    * Created from internal images, sounds, tastes and smells we encounter
    
* Neuro-**Linguistic**-Programming
    * We add personal meaning to the information received at 'first access'.
    * Assigning language to those smells, images, feelings

* Neuro-Linguistic-**Programming**
    * Our Behaviour Response
    * Communicated content is manipulated by the brain
        * Changed due to previous experiences
        * Connected to other memories
        
>**"** It is like learning the language of your own mind - is the practice of
understanding how people organise their thinking, feeling, language and
behaviour to produce the results the do. NLP provides people with a
methodology to model outstanding performances achieved by geniuses and leaders
in their field. NLP is also used for personal development for success in business. **"**

How people organise their feeling, thinking, language and behaviour to how someone receives that information.

* **Types** :
    * Mindset changes to positively affect the well-being of people suffering from anxiety
    * The behaviour of someone in a business environment and how they communicate with their peers in a positive and informative way.
* **Benefits**
    * It can be helpful to develop a better **mindset** for yourself, improve the behaviour and other aspects of your every day life,
    whether it be in the workplace or at home.
    * A bit more of a positive outlook on life can be achieved simply by changing the way you think about things and the behaviour that is
    shown we approaching different situations
    
* **NPL** in the **Workplace**
    * NLP provides you with the ability to improve your communication and reverse
negative behaviours
    * Problems are usually internal
        * Work experiences are related to the individual rather than the workplace
    * Studying language patterns to tailor communication methods
        * Building workplace relationships
        * Influence the way others think (negotiation)
    * Managing emotions
        * Control your reactions towards negative events, and do not come across as overly negative
        * Stress and anger
        * Excitement and happiness
        
* **Extra Information** on **NPL**

    * This can help you think more clearly
    * Communicate more effectively with others
    * Manage your thoughts, moods and behaviour effectively
    * Medical benefits
        * Handle your anxiety, stress, phobias
        
___
> 16:30 PM - Communication 2 Continued... **[Late-Afternoon]**

* **Cognitive Biases**

**_What is it..?_** A **cognitive bias** is a systematic error in thinking that occurs
when people are **processing and interpreting information** in the world around
them and affects the **decisions and judgments** that they make.

**cognitive biases** are often a result of your brain's attempt to simplify
**information processing**. This is on order to help you reach a decision and
make sense of the world with relative speed.

>https://www.verywellmind.com/what-is-a-cognitive-bias-2794963/ "`Cognitive Bais - What is it?`"
>___
>https://medium.com/better-humans/cognitive-bias-cheat-sheet-55a472476b18 "`Cognitive Bais - Cheat Sheet?`"

* **Two examples of Biases**

    * **Too much information** 
        * Anchoring
        * Confirmation Bias
        * Choice-supportive Bias
        
    * **Not Enough Meaning**
        * Outcome Bias
        * Authority Bias
        * Bandwagon Effect
        
Overall There are **175** types of Biases, too much to cover!

* **Exploiting Bias** in the workplace
    * **Reactance** - tell people to say no they are more likely to say yes
    * **Reciprocity** - Be the first to give up
        * The feeling of obligation to give when you receive
        * Personalised and unexpected makes it even better
    * **Door in the face** - forcing people to refuse a large request increases the
    * likelihood of agreeing to a second, smaller request
    * **Likability** - Give compliments ad build cooperation
        * Freely give honest flattery
    * **The Bystander** people who look to others to determine their own actions.
    
* **Six Hats of Thinking**
    * **White hat** - calls for information known or needed. the facts just the facts
    * **Yellow Hat** - symbolises brightness and optimism, under this hat you explore
the positives and probe for value and benefit
    * **Black hat** - judgement, the devils advocate or why something may not work.
Spot the difficulties and dangers. most powerful and useful of the hats.
    * **Red hat** - Signifies feelings, hunches and intuition . When using this hat
you can express emotions and feelings and share fears, likes, dislikes, loves,
and hates.
    * **Green hat** - focus on creativity; possibilities, alternative, and new ideas.
Its an opportunity to express new concepts and new perceptions.
    *  **Blue hat** - manage the thinking process. Its the control mechanism that
ensures the six thinking hats guidelines are observed.

---
>**Homework** 
>> * Attach Cheat-Sheet for **GitHub** commands so it can easily be reffered to in the future
>> * Can be useful to keep a **LogBook** to allow problems and resolutions to be recorded in case the
>same problem arises again the future.
>> * Look More into Neuro-Linguistic-Programming. **_`Idea Behind it?`_**