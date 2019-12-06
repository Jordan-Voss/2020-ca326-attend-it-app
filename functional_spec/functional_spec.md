
    0. Contents


    1 - Introduction       pg 2


    	1.1 - Overview  pg 2


    	1.2 - Business Context pg 2


    	1.3 Glossary pg 3


    2 - General description


    	2.1 - Project/System Functions pg 4


    	2.2 -  User Characteristics and Objectives pg 4


    	2.3 -  Operational Scenarios pg 5


    	2.4 -  Constraints pg 6


    3 - Functional Requirements


    	3.1 - Login Page pg 7


    	3.2 - Timetable Generation pg 7


    	3.3 -  Attendance Marking pg 8


    	3.4 -  Analysis pg 8


    4 - System Architecture pg 10


    5 - High Level Overview pg 12


    6 - Preliminary Schedule pg 15


    7 - Appendices pg 17



1. <span style="text-decoration:underline;">Introduction</span>

1.1 _Overview_

The system we have chosen to develop is called ‘Attend-It’. It is an online website/app that will take the attendance of students in classes, labs, or tutorials  and the target audience will be students and lecturers. This project will counter the problem we have at Dublin City University where attendance of students is taken in different forms, many of which are very unreliable. The most common way of taking attendance is by either a lecturer passing a sheet to be signed by students or by a form online. Through these methods, students can easily lie and fraudulently fill it in for themselves or friends.  Our system will tackle this issue, by identifying the Wi-Fi access points in the room and who is connected to them, marking them present for the lecture. Lecturers using our system will have a live-feed of students that are attending the class and will be able to see which students are absent. Using linear regression, the lecturer will be able to use our system to find the correlation between grades and attendance of students. It will also find trends in absenteeism and be able to predict approximate attendance level of lectures as the semester goes on. It will use cues such as time of lecture, whether the students have a big break beforehand, and exams/assignments due in that module or others.

Users will have a study timetable generated based on the difficulties of their modules decided by each individual student, dedicating more time for the ones they find difficult. Our app will be able to generate multiple timetables that have the student’s work, college, sleep and study schedule all in one.  Lectures using the app will be able to see the attendance level of each student and grades. This data will comply with GDPR as the lecturer will be the only one seeing this section of the app. The data will be anonymised so even the lecturer will not be able to see who each piece of data represents, but only the correlation between all exam marks and attendance.

1.2 _Business Context_

Although we do not have a business organisation sponsoring our project, we do hope that Dublin City University, and other institutes of education could benefit  from our project in order to make attendance tracking more efficient for staff. We also think it would be beneficial for the students through our study plan generator which would ease the pressure of exams for students by reminding them regularly of deadlines and encourage them to study from the beginning of each semester.

1.3_Glossary_

**Access Point:** A hardware device on a local area network that allows wireless capable devices and wired networks to connect through a wireless standard, including Wi-Fi or Bluetooth. Also known as a hotspot.

**Http Request:** A packet of information that one computer sends to another computer to communicate something.

**GUI:** Stands for "Graphical User Interface", it is a user interface that includes graphical elements, such as windows, icons and buttons. Essentially the screen that the user sees when using an app or website.

**GDPR:** The General Data Protection Regulation (GDPR) is a legal framework that sets guidelines for the collection and processing of personal information from individuals who live in the European Union

**JDBC:** Java Database Connectivity, a Java API. Using it as a java interface for communicating with our database and MySQL

**API:** Application Program Interface is a set of routines, protocols, and tools for building software applications. It specifies how software components should interact. For us this is specifying how Java and MySQL should interact



2. <span style="text-decoration:underline;">General Description</span>

2.1 _Product/System Functions_

When a student/lecturer  downloads our app or accesses it  through our website they will be prompted to enter their login details.

_<span style="text-decoration:underline;">Students;</span>_

Upon successfully entering their details, the will have entered the home-page with **Attend** , **Time-Table**, **Study-Timetable** , **Achievements**, and **Preferences** as navigation bars.

**Attend-**  The user will be able to log in their attendance of the lecture/lab, if one is running. If they don’t have any occurring the next one will be on display.

**Time-Table-** The user will have access to their college timetable.

**Study-Timetable-** The user will have the option to generate a timetable surrounding their college timetable. They will be able to implement a work, sleep or study schedule around it. If they have any extra-curricular activities, it can be added into this timetable.

**Preference-** The user will be able to rank their modules from easy to difficult.

**Achievements** - The student will receive achievements throughout the semester when they achieve, e.g. ‘Attending all of a single module within a week’ , ‘Attending all scheduled lectures and labs within a week’ as well as alternatives for each month and full semester.

_<span style="text-decoration:underline;">Lecturer;</span>_

When a lecturer successfully logs in to our app/website, they are introduced to the homepage with **Class**, **Time-Table** and **Analysis** as navigation bars.

**Class-** When the user clicks on to the Class title, they will have a live feed of who is attending their classroom and what time they attended the class.

**Time-Table-** The user will have access to their college timetable.

**Analysis-** The user will be able to see trends in their students attendance. Feedback will be given in terms of predicting attendance of each student and determine the correlation between attendance and results.

2.2 _User Characteristics and Objectives_

The intended users for our app will be students and lecturers. Students/Lecturers with a mobile phone or laptops will be able to access our app. Students will already have a basic knowledge of how apps work so traversing it will not be difficult.  Students, specifically those who lack organisation skills will have their timetable customised and generated to their liking. The majority, if not all lecturers have a bit of knowledge with using Loop,  so this information can be easily transferred and used to use our app.

2.3 _Operational Scenarios_

_<span style="text-decoration:underline;">Login </span>_

The student/lecturer will be prompted to enter their login details. Students need to use their university credentials to successfully log in to the app/website. If they are unsuccessful in entering their details, a message will pop up indicating they have entered the wrong details and they should try again.

_<span style="text-decoration:underline;">Class</span>_

When the lecturer successfully enters their login details and clicks on to the **Class** bar they will be able  to see and access a live feed  how many students are attending their lecture/lab. It will also highlight all the students that are absent in the live class.

_<span style="text-decoration:underline;">Analysis</span>_

When a lecturer clicks into the **Analysis** bar, it will allow them to see trends of their students attendance in the form of data visualisations. The lecturer will have a tool which will allow them to predict how many students will ideally attend the next class.  The lecturer will be able to see the correlation between attendance and results of each student and using these variables, will be able to predict a grade for the students.

_<span style="text-decoration:underline;">Attend</span>_

When a student clicks on the **Attend** navigation bar, the page will give them information on what class they should be attending right now, or what lecture/lab is coming up next based on their timetable.  On this page, the student will be able to  click “attend” to their lecture that is currently running which will mark them as attended.When they click attend, our system will be able to check their location using the Wi-Fi access points in the building  to see whether they are actually in attendance of that lecture/lab.

_<span style="text-decoration:underline;">TimeTable</span>_

Upon clicking the **Timetable,** the student will be able to make, edit or view their college timetable. Timetables will be colour coordinated to show which classes they have attended and the ones they have missed. Students will be able to choose from a range of different colours as we are keeping in mind users that suffer from colour-blindness. They will also be able to cycle back and access previous weeks that have passed.

_<span style="text-decoration:underline;">Study TimeTable</span>_

When a student clicks into the **Study Timetable** they will be able to generate their own study timetable and customise it around their college timetable. The user will be able to fit in their work schedule or extra curricular activities into this  timetable.

_<span style="text-decoration:underline;">Preferences</span>_

A student clicking into the **Preferences** tab will introduce them to the ranking modules. This is a feature that allows them to rank each module from easy to difficult (0 being the easiest and the most difficult being 5). This will allow the student to allocate more time in the modules they find very difficult.

2.4 _Constraints_

**_<span style="text-decoration:underline;">Time</span>_**

Time will be a major constraint for this project as the deadline is in the month of March. As the project grows we can only hope that it still fits in time with our task deadlines and will  be fully functional before the due date. The more constraints we face in time, the higher the potential risks as the project will end up being rushed._<span style="text-decoration:underline;">		</span>_

**_<span style="text-decoration:underline;">Experience and prior knowledge</span>_**

Given that neither of us have made an app and  have any knowledge of Wi-Fi access points , we may find it more difficult to implement our system as initially intended.

**_<span style="text-decoration:underline;">Database memory</span>_**

Given the limit on our server account and MySql, we will be unable to test the project on the scale that it would possibly grow to in time and see the potential problems that would occur later on with more people using our system.



3. <span style="text-decoration:underline;">Functional Requirements</span>

3.1 _Login Page_

**Description**

The system must be able to identify the correct user login and distinguish between a student’s account and a lecturer’s account, and redirect them to the appropriate pages. We will need to store all of the pre-existing and new users in a database in order to determine a login.

**Criticality**

The login page is critical to our system in terms of identification. Without this we will not be able to tell who has logged in to attend a class or be able to tell if they are a student or lecturer, which would enable the incorrect permissions for the user.

**Technical Issues**

Our primary issue is to ensure all logins are unique and stored correctly within our database while retaining the ability to identify the correct member of staff or the student body whose details will be stored within.

**Dependencies with other requirements**

This section will be what determines the homepage that is shown next (either a staff or student version) and will be important, especially on the student side to show correct timetables, achievements and study plans generated to the specific student as these are tailored individually and will not apply to all who use the app.

3.2 _Timetable Generation_

**Description**

The system must be able to provide multiple study timetables for the user, ensuring no overlapping between their work, extra curricular activities, college timetable, travel, and sleep. It must also take into account the ranking of each module based on difficulty and prioritise the most time of the total study hours per week to this topic.

**Criticality**

In this part of our system, the most important part is to ensure each student’s timetable is allocated only to them, as their work,study,sleep, etc. schedules will differ. It is critical that we identify the student and have the correct generated timetables stored in the database as well as offering refreshed study plans if a timetable is edited during the semester or a work schedule is changed.

**Technical Issues**

A technical issue with the timetable generation of our system is ensuring each timetable generated is completely accurate while also maintaining the most efficient for studying, e.g. suitable breaks, subject rotation. We want to provide our students with the best way to learn through our generated study timetables.

**Dependencies with other requirements**

This section will be determined by information placed into the ‘Preferences’ section of the app. It must take the information provided and stored into the database and with this information compute 3-5 of the best methods a student can study and construct multiple timetable options for them each week.

3.3 _Attendance Marking_

**Description**

Our system must be able to identify the access point that a computer is connected to, and the account that is identified with it when a student opts to sign into a lecture.

**Criticality**

This part of our system is very critical as it is the main function of our app. It must work efficiently to provide real time information to the lecture on who is present or absent.

**Technical Issues**

When connecting to access points in the college, a device automatically connects to the nearest/strongest signal it can get. Sometimes this may not be in the same room as the lecture that is taking place. Therefore we will have to incorporate a way of checking all adjacent rooms that could be the source of connection for a student’s device. We can do this my cross referencing a class list with lists of those connected to the room a lecture is taking place in, as well as all the rooms which could possibly be generating a stronger signal to a person sitting in any seat in the room and if someone is connected to an access point in LG26 for example, but the lab is taking place in LG27, we can mark them as present, however if this person is connected to XG19, we know they are not attending and they will not be counted as in attendance.

**Dependencies with other requirements**

On the student side of the app when they are clicking to attend a lecture, this will be depended on by the lecturer’s side, where they can see the real time information on those who are present.

3.4 _Analysis_

**Description**

The Analysis section on the lecturer’s side of the app will depict some data visualisation showing the correlation between attendance and overall marks in CA and exams (helpful for the next year to show that attendance does matter.) It will also find trends in absenteeism and be able to predict approximate attendance in lectures as the semester goes on. It will use cues such as time of lecture, whether the students have a big break beforehand, and exams/assignments due in that module or others.

**Criticality**

This is an important part of our system as it uses the data gained by our attendance tracking and uses it to try to find reasons as to why certain lectures may be attended more than others. This will be a useful tool to the lecturers as it will help with future timetable design as trends develop over the years to see where the best place to put a lecture would be.

**Technical issues**

An issue with this will be to ensure when we are representing the correlation between students being absent and their exam marks, that we don’t make this available to everyone. It must be available only to the relevant lecturers and must not be able to be traced back to individuals and only show the correlation between a result and attendance. We cannot have this data open for every lecturer to see so a lecturer must only be able to see the data for modules that they are teaching, but a head of school should be able to see all data for the lecturers within their school.

**Dependencies with other requirements**

Will depend on the data gathered over a semester with regards to attendance and incorporate these with the marks awarded at the end of the exam period.



4. <span style="text-decoration:underline;">System Architecture</span>
1. User

    Logs into app and makes HTTP requests

2. Web Server

    Hosts the apps various layers

*   GUI: User interface where users interact with the app via HTTP requests and responses
*   Application: Manages the application, works with the data layer to process requests from users and execute what is needed to be done.
*   Data: Handles data and provides retrieval services for the database
3. Database

    Where data is stored and can be edited or used

4. Web Services:

    Interaction with other applications (Loop etc.)






![architecture diagram](https://imgur.com/lyu0nqI)




5. <span style="text-decoration:underline;">High Level Design</span>


**User Journey Flow Diagram (Lecturer)**



![leclogin](https://imgur.com/JjYAuti)

**User Journey Flow Diagram (Student)**



![usrlogin](https://imgur.com/zNtNJAg)





![UseCase](https://imgur.com/vxVFmFx)


6. <span style="text-decoration:underline;">Preliminary Schedule</span>

The image below shows a provisional timeline for our project.We will be conducting research  using our HP laptop, MacBook Pro and the Dublin City University computers. We will be using Kivy in Python as a framework for the GUI since most of our code will be written in Python.  We will start with the GUI of the Login Screen.  Using MySql as a database management  we will also focus on the database retrieval in the same week. Since we are using MySql, we have chosen to use JDBC, which is a Java interface for working with MySql. We have given two weeks for our system to be able to pinpoint a device’s location using the access points in the building. We estimate it might take longer as we need to consider the fact that depending on where the student is in the room, determines which access point is closest to the student . This is when we will begin testing our system thoroughly as we believe this is the area id likely  to be error prone. If we manage to solve this issue sooner, it will shorten the testing of the lecturer’s live feed of present/absent students. We plan on doing the GUI of the Timetables and Preferences section.  We have given ourselves a considerable amount of time for the creation of multiple timetables as we need to be sure that our program will give accurate timetables, while also considering the most beneficial method of studying (regular breaks etc.). A lot has to be considered as well since we have to factor in their sleep  schedule, work schedule and their preferred number of hours of study per week ultimately giving them a timetable that makes sense to them. This again will include various software testing aspects and some user requirement testing. The next major step will be researching how we can use linear regression to determine the correlation between attendance and grades of a student. These areas will be thoroughly tested to ensure that solid trends are found within the data. Following this timeline will give us enough time to perfect our system for final testing so it will be the standard we set out for it. Once the final alterations are complete we will start preparations for the demonstration of our project in March.





![gantt1](https://imgur.com/VJZfJO6)


![gantt2](https://imgur.com/ati4oGW)




7. <span style="text-decoration:underline;">Appendices</span>

**Research Tools:**

[https://kivy.org/#home](https://kivy.org/#home)

[https://www.javatpoint.com/java-jdbc](https://www.javatpoint.com/java-jdbc)

[https://www.python.org/](https://www.python.org/)

[https://www.mysql.com/](https://www.mysql.com/)

[https://www.w3schools.com/](https://www.w3schools.com/)

[https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f](https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f)
