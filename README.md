<div>

<span class="c8 c21"></span>

</div>

<span class="c3"></span>

<span class="c22"> </span><span class="c38">--</span><span class="c36 c38">--</span><span class="c38 c39">-</span>

<span class="c32">[</span><span class="c32 c36">Parking</span><span class="c0">]</span>

<span class="c22">Simulation</span>

<span class="c3">             </span>

<span class="c3"></span>

<span class="c3"></span>

<span class="c3"></span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6">         </span>

<span class="c6"></span>

<span class="c18">By</span> <span class="c18">Enter The [</span><span class="c18 c35">Matrix</span><span class="c18">]</span><span class="c18"> </span>

* * *

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 820.00px; height: 358.75px;">![](images/image2.png)</span>

# <span class="c31"> Introduction</span><span class="c9 c7 c33">.</span>

<span class="c1">Over the last few years, the number of students at the University of Washington Bothell has been continuously growing. According to Fast Facts 2017-2018 (uwb.edu),  there are 5,995 FTE students currently going to UWB; 57% of students live in King County and another 27% of students live in Snohomish County. The increasing number of commuters are putting pressure on the UWB administration as they are trying to build more parking spaces to accommodate current and future students. UW Bothell shares its campus with Cascadia College which makes this problem more apparent for both colleges. In 2017, Cascadia College had 3,425 full-time and part-time students (collegetuitioncompare.com). This sums up to a total of about 9,500-10,000 students on the campus. Aside from the number of enrollments, we have to take in the considerations of staff and faculty from UW Bothell and Cascadia College that are commuting to campus every day.</span>

<span class="c1">We are modeling how the parking lots at UW Bothell function under various traffic conditions. We will simulate how commuters will occupy the parking spaces at UW Bothell. Currently, there are five main parking lots/garages (South Garage, South Surface Lots, Discovery Hall Lots, North Garage Lots and Chase House Lot) that we will use to simulate the parking spaces. Additionally, there are also a number street parking placed alongside the three main roads (Campus Way NE, NE 180th St, 110th Ave NE). The three main roads will link all the parking lots together. Depending on different simulation parameters, we will get a different expected result every hour.</span>

<span class="c1">Additionally, the parking spots have different types that we have to take into account. Most students will be using the regular parking spots on campus, but our simulation will take into account the disability, motorcycle, and carpool parking spots. Thus, we will calculate how the expected parking congestion based on the average number of students and faculty that visit campus during the day, and the type of the parking spot that they typically use.</span>

<span class="c1">One of the phenomena that we are testing for is how a proposed new Time Schedule for classes will affect parking lot usage across the Campus. This proposed new schedule sought out to introduce a Free Block midday, which translates to slightly earlier times, and a more efficient usage of Friday for the classes (UW Bothell Time Schedule Work Group). The better usage of Friday would decrease the number of students on Campus from Mondays through Thursdays, whereas the Free Block would allow for those arriving and leaving the campus to not be limited to the typical 15-minute gap between their classes. However, by utilizing the Free Blocks, we would free up the classrooms to host meetings and events, which could increase the amount of people on campus, leading to increased usage of the parking lots.  </span>

# <span> </span><span>Model Description</span><span class="c9 c27">.</span>

<span class="c1">We will be using an Agent model to help visualize this project. This will allow use to better simulate those who use the parking structures and having the ability to add variance within the agents by simulating when they use the parking structures. Our model will test which times of the day the parking lots will get more congested, and increase the time it takes to both leave the parking lots and how long it will take for people who are arriving to park.</span>

<span class="c1">The assumptions that we are making for our model are that not all UW Bothell students drive, that not all cars that will contain just a single passenger, cars arriving in to the parking structure, students and staff have differing schedules throughout the week, and staff will use parking spots longer than students.</span>

<span class="c1">As that public transportation in King Country is vast, we are able to assume that a percentage of Students and Staff do not use the parking lots. That being said, there is a possibility that those students and staff only use them once a day, having carpooled to or from UW Bothell. Furthermore, in those cases the number of passengers in a percentage of those cars will have increased, separate of those who have are specific Carpool Parking Pass. We will have to consider each student will have a different schedule, therefore they will go to the campus on different days. The number of faculties and staffs will affect the number of parking spaces as they will be staying on the campus for longer than an average student. Cascadia students will also be included in the model as they made up of a large proportion of data in the model.</span>

<span class="c1">The constraints that we will have in our model are that our model is only account for times in which the Campus is open, that the number of total people will not exceed 110% of those enrolled and employed at UW Bothell and Cascadia College. This extra 10% accounts for visitors the the campus when there is an event occuring at the campus.</span>

<span class="c1">Our model could be used for testing parking patterns within the parking lots are UWB. In the cases where one of the parking lots is inaccessible, our model can be used to simulate what affects it will have on the rest of the parking lots. This is also the case when adding parking lots, showing the effects having additional parking lots have on alleviating the congestion of the parking lots</span>

<span class="c23">Our model can potentially be used to assist students and staff when arriving so that they can account for the congestion of the parking lots into their arrival and departure times.</span>

* * *

<span class="c8 c7"></span>

# <span> </span><span>Analysis</span><span class="c9 c27">.</span>

<span class="c1">The metrics that we are going to be testing for are the length of time it will take to leave and enter the parking lots based on location, and the usage of the parking lots by number of cars. We came up with several questions that will guide our analysis throughout the modeling process.</span>

## <span class="c9 c7">What is the current parking problem at UW Bothell?</span>

<span class="c1">First, we will calculate the length of time a student will take to find and leave a parking space. This will show the existing congestion problem at UW Bothell. At peak hour, we expected the problem to be apparent.</span>

## <span class="c9 c7">What is the expected wait time for students to park at peak hours?</span>

<span class="c1">As we gather more data through running multiple trials of the simulation. We can figure out the average wait time to find a parking space at each hour. Therefore, we can get a sense of parking time for UWB students.</span>

## <span class="c9 c7">With the new Free Block included, will there be a difference in terms of congesting and parking availability on the campus?</span>

<span class="c1">We will switch the student schedules around to accommodate with the new time schedule. The rate of cars entering in and exiting out of the campus will be different. We will see if there are any noticeable differences between the existing time block and the new Free Block.</span>

## <span class="c9 c7">With the construction of the new 5-level parking garage (600 parking spaces), will that bring significant changes to the current parking problem at UW Bothell?</span>

<span class="c1">By adding another garage module to the system, we can see differences in terms of wait time and travel time for students. We can make conclusions if the new garage will bring changes to the existing system.</span>

## <span class="c9 c7">How will you validate/verify your model?</span>

<span class="c1">We will verify our model by the doubling checking each other once he have pushed a new update to the GitHub. Having a new set of eyes review the code makes sure that the code is readable, and properly commented.</span>

<span class="c23">We will validate our model by checking our model against real life data collected by the members of our group, collecting the data whenever we use the parking lots.</span>

# <span> </span><span>Testing</span><span class="c9 c27">.</span>

<span class="c1">We will be testing the proper creations of all of our objects. We should be able to create 3 different types of agents, the student, the faculty member, and the staff member (a visitor agent will be a subset of this agent). We will also test that we are only able to park a single vehicle in a single position within a list, which is how we represent a single spot in a parking lot.  </span>

<span class="c1">We will make the implementation and debugging process more efficient by using unit testing. Unit tests allow us to test every section of our code step by step as we proceed in the development process. Standard unit tests are also very easy to read and implement compared to customized testing code.</span>

<span class="c23">Every class, and function will be tested using the python’s standard unit testing library. The expected input, and output specified by the code documentation is translated into modular test cases which we’ll use to ensure the proper functionality of every section of our simulation. The code is expected to behave properly in case of invalid inputs / parameters. Thus, our unit tests will also test the code with invalid / unexpected inputs and our code should behave the sway that is specified in the code documentation.</span>

<span class="c7 c8"></span>

# <span> </span><span>Personnel</span><span class="c9 c27">.</span>

## <span class="c9 c7">Adam Deehring</span>

*   <span class="c7">Areas of Expertise:</span><span class="c7"> </span><span class="c1">Conceptual Design</span>
*   <span class="c7">Tasks throughout Project:</span> <span class="c1">Creation of Agents (Student + Staff + Faculty)</span>

## <span class="c9 c7">Dewey Nguyen</span>

*   <span class="c7">Areas of Expertise:</span> <span class="c1">Coding Implementation</span>
*   <span class="c7">Tasks throughout Project:</span> <span class="c1">Creation of Environments (Garage + Roads)</span>

## <span class="c9 c7">Ardalan Ahanchi</span>

*   <span class="c7">Areas of Expertise:</span> <span class="c1">Implementation, Unit Testing, Optimization</span>
*   <span class="c7">Tasks throughout Project:</span> <span class="c1">Creation of the simulation logic</span>

## <span class="c9 c7">Xavier Cheng</span>

*   <span class="c7">Areas of Expertise:</span> <span class="c1">Verification and Validation</span>
*   <span class="c7">Tasks throughout Project:</span> <span class="c23">Help Create Environments / Analysis</span>

    * * *

# <span> </span><span>Technologies</span><span class="c9 c27">.</span>

<span class="c1">In our project, we will be using Google Drive, GitHub, and Discord.</span>

<span class="c1">We will be using Google Drive for creating, editing, and storing reports or results for our simulations. These data will be used to analyse our tests.</span>

<span class="c1">We will be using GitHub for storage and version control of our code. The manager will create a repository and invite all team members to be the collaborators. All team members will post changes to the Github repository.</span>

<span class="c1">We will be using Discord as our main communication method. We’ve created a discord server designated for this project. Text chat and voice chat functions will be constantly used throughout the quarter</span>

<span class="c1">Unit testing will be accomplished by using the standard python unit testing library. By utilizing unit testing, our tests will become more comprehensive, readable, and reliable.</span>

# <span> </span><span>Benchmarks</span><span class="c9 c27">.</span>

## <span>May 25th 2019 -</span> <span class="c7">Structure and Visualization</span>

*   <span class="c1">By this date, we will have all of structure of the simulation built, as well as the base methodology for our simulation’s visualization should be finished.</span>

## <span>May 30th 2019 -</span> <span class="c9 c7">Completion of the Control</span>

*   <span class="c1">By this date, we will have a working base case for our simulation. Once this is done, we will be able to start altering behaviors across the simulation</span>

## <span>June 4th 2019 -</span> <span class="c9 c7">Final Presentation Wrap Up</span>

*   <span class="c1">By this date, we will have the final presentation of the project completed. It should be ready for presentation on the 5th. Ideally, we need to have a working demo as well to demonstrate in the presentation.</span>

## <span>June 5th 2019 -</span> <span class="c9 c7">Final Software Product Wrap Up</span>

*   <span class="c1">By this date, we will have the Software Project completed to turn in, and to be turned in before 11:59 pm.</span>

# <span> </span><span>Design Draft</span><span class="c9 c27">.</span>

<span class="c8 c21">The following figure demonstrates our draft design hierarchy. The required objects along with their predicted functions and attributes are displayed in the UML class diagram format.</span>

<span class="c8 c21"></span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 351.00px; height: 680.00px;">![](images/image1.png)</span>

<span class="c8 c21"></span>

<span class="c25">Figure 1\.</span> <span class="c8 c21">Draft design of the simulated objects.</span>

<div>

<span class="c26"> Page</span><span class="c26 c34"> </span><span class="c33 c37"> </span><span class="c36 c33 c23 c41">.</span>

</div>
