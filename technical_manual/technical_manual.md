**0. ****Table of Contents**

**0.1 ****Introduction**

0.1.1 Overview

0.1.2 Glossary

**0.2 ****System Architecture**

0.2.1 System Architecture Diagram

**          0.3 High Level Design**

0.3.1 Lecture Case Flow Diagram

                        0.3.2 Student Case Flow Diagram

                        0.3.3 Use Case Diagram

 **0.4 Problems and Resolution**

0.4.1DCU's Wi-Fi Access Point

               0.4.2 Raspberry Pi

0*.*4.3 *Local Area*Network

*0.*4.4 Time Constraint

**   0.5** **Future Development**

**   0.6 Installation Guide**

**1. ****Introduction**

**1.1 ****Overview**

Attend-It is an online app that is designed to take attendance in classes labs or tutorials. We came up with this idea after noting that DCU takes attendance in different forms. The most common form of taking attendance is by a lecturer passing a sign-in sheet or an online form, which can be easily filled in fraudulently. We proposed this system so that it will be able to combat this problem and make attendance taking more reliable and concise. By using Wi-Fi access points, Attend-It will be able to see who is present and absent. Users can have a study timetable generated based on their rankings of modules, dedicating more time to the ones they find more difficult. Linear regression will allow the Lecturer to see the correlation between grades and absenteeism and will be plotted on a graph.

**1.2 ****Glossary**

1        ISS - Information Systems Services located in DCU Glasnevin campus.

2. MAC address - A media access control address is a unique identifier assigned to a network interface controller for use as a network address in communications within a network segment.

3. DHCP - The Dynamic Host Configuration Protocol is a network management protocol used on Internet Protocol networks.

4. DHCP server - dynamically assigns an IP address and other network configuration parameters to each device on a network.          

5. wpa_supplicant - cross-platform supplicant that implements key negotiation with a WPA authenticator, and it controls the roaming and IEEE 802.11 authentication/association of the wireless driver.

6. OS - Operating System is a software which acts as an interface between the end user and computer hardware.

7. Raspberry Pi - a series of small single-board computers.

8. Apache webserver - open-source and free web server software.

9. URL - The Uniform Resource Locator is an address that sends users to a specific resource online.

10. Access Point -- A hardware device on a local area network that allows wireless capable devices and wired networks to connect through a wireless standard, including Wi-Fi or Bluetooth. Also known as a hotspot.

11. **Http GET Request **- retrieves information from a server.

12. PHP- Hypertext Preprocessor is a script language and interpreter used primarily in Linux webservers

13. index.php - PHP file that is the entry point of any website and application. It is a file used for templates that contain a mixture of codes that will be delivered as a PHP code

14. IP address - Internet Protocol address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.

15. NIC - Network interface card is an electronic device that connects a computer to a computer network

**2\. System Architecture**

**2.1 System Architecture Diagram**

Using draw.io we made the *System Architecture* diagram. This diagram shows the structure and behaviour of our system.

**![Screenshot of System Architecture Diagram
](https://imgur.com/NfhtUR5)**

**3\.  High Level Design**

We used draw.io to make the Lecture/Student Case Flow diagram.

**3.1 Lecture Case Flow Diagram**

Showing the navigation between different pages

**![Screenshot of Lecture flow Diagram

Description automatically generated](https://imgur.com/QfeCaqg)**

 **3.2 Student Case Flow Diagram**

Showing the navigation between different pages

**![Screenshot of Student Flow Diagram

Description automatically generated](https://imgur.com/L37XT5R)**

**3.3 Use Case Diagram**

Representation of a user's interaction with the system that shows the relationship between the user and the different use cases in which the user is involved. 

**![A close up of a whiteboard

Description automatically generated](https://imgur.com/tDoFDHW)**

** 4. Problems and Resolution**

**4.1 ***DCU's Wi-Fi Access Point*

As soon as we started researching how to get access to the routers in DCU and get information of all the devices connected to it, we ran into a major problem. DCU's network supplies all devices with temporary IP addresses so if were to implement our program we would need to contact ISS and receive a static IP address. However, that ended up being a dead-end. To get over this issue we decided to buy two Raspberry Pi's from Amazon and turn them into access points as proof of concept.

**4.2 ***Raspberry Pi*

As soon as we configured the Raspberry Pi's as access points, the Wi-Fi interface switched off. We then looked online to try to share an internet connection (bridge) with the Raspberry Pi's but that was unsuccessful. This meant that we had to go back and download everything we needed before configuring it into an access point. This caused a lot of time wasting, back and forth installations and downloading and rebooting, reinstalling the Raspbian OS. We also needed a static IP address for the Raspberry Pi's, so we had to invest in a router that would be able to supply them IP addresses.  After editing and changing around the wpa_supplicant and DHCP files we realised that it did not work because Raspberry Pi's come with only one NIC.

**4.3 ***LocalAreaNetwork*

One of the main issues we found in this project was transferring data around without the use of internet.  Since the Raspberry Pi's were connected to a router that did not supply internet we had to find a way to get all the device's MAC address' that were connected to the Pi's and find a way to send it back to the Attend-It app. We talked to Michael Scriney since this was a network problem. He suggested that we set up a DHCP server. This would allow us to get the MAC addresses and the IP addresses of any device connected to the Raspberry Pi. However, no matter how many times we installed the isc-dhcp-server it would not run. After a few days of trying, we left that idea as we were wasting too much time and not exactly getting anywhere closer to the solution.

We realised we had to take a step back and re-analyse the situation. We randomly pitched our problem to Stephen Blott, one of the lecturers in DCU and within minutes he gave us a way to work around it. Since we already had an Apache web server installed in the Raspberry Pi's we could just edit the index.php and dump all the MAC addresses to the server. Then all the Lecturer has to do is HTTP-Get request to the URL of the webserver and from there we can get all the information back into the Attend-It app.

**4.4 **Time Constraint

When we pitched our 3^rd^ year idea, we were unaware of how long each feature of the project would take up. We also spent too much time on parts of the project that brought us nowhere. That is the reason why we had to remove some features of the project.  We were late in deciding if we were going to use Raspberry Pi's as we lacked knowledge with those devices. When we decided to order the Raspberry Pi's the time it took for them to be delivered (one week) set us back.  When we realised we needed a static IP for the Raspberry Pi's, it took some time to also find a cheap router.

**  5. Future Development**

If we were asked to take this project further, we would like to develop a web-app to go along with it. We would include all the features we missed out on as we would have a better understanding and more time to implement it.

**  6. Installation Guide**

Requirements -- iOS/Android device, Internet Connection.

Android device -- Install the app in Google PlayStore.

iOS device - Install the app in the App Store.

**References**

Setting up Raspberry Pi's as Access Point ~ <https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md>

Setting up an Apache webserver ~

<https://loop.dcu.ie/mod/resource/view.php?id=1194051>

Setting up a DHCP server on a Raspberry Pi ~

<http://www.noveldevices.co.uk/rp-dhcp-server>

Linear Regression ~

<http://www.ijcse.com/docs/INDJCSE17-08-03-080.pdf>

Diagrams ~

<https://www.draw.io/>
