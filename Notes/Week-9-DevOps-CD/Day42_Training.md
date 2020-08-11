###### Sparta Global Training Day 42
###### We have now completed Continuous Integration and Deployment using Jenkins

___

> 9:30 AM Academy Stand up [Morning]

No Real blockers, I have finally gotten my Jenkins to take in the GitHub Code and integrate that into a build which will then be automatically merged to my GitHub Repository. Then That will trigger my Deployment job on jenkins which will SSH into the EM2 Instance and copy over the app and environment folder.

To confirm this was a success I can connect to my EM2 Instances IP address which is being hosted on the NGINX web server, this should show any updated HTML like text and images.

![CICD_WebApp_Working](../../Images/CICD_WebApp_Updated_After_Push.PNG)