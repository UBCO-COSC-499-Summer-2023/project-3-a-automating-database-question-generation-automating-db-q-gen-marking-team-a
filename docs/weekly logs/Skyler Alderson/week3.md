# Week 3

## Sunday, May 28
We had a team meeting to review the Scope and Charter document before submission. We went over it item by item and changing things as necessary. The meeting was ended when we submitted the document and planned what we would need to do over the next few days.  

##  Monday, May 29
I worked on creating diagrams for the Design Draft milestone for week 3. I created the Use Case diagram, with all the necessary dressing, and both the level 0 & level 1 Data Flow Diagrams. I was not satisfied with the level 1 DFD, but I wanted to get a first sketch done.  

##  Tuesday, May 30
We each have been trying to get Docker to work, and my attempt was unfruitful. After some communication over Discord, we decided to put our focus on this week's milestones over tinkering with Docker.
I also made a second draft of the level 1 DFD. This one is still better, but it reveals two gaps in our diagram: where does the data that initialises an instance database come from, and where does a lecturer's new question data go to. This second draft will be used as a template for a third draft, since its foundations are good.  

##  Wednesday, May 31
We met as a team well before our first report. We discussed what we had to have prepared for the meeting, our tasks over the next few days, and how to solve our Docker issues. For Docker, we plan on splitting the work such that one person can focus on figuring our Docker (Matthew) while the others get this week's milestones completed (everyone else).  
After discussing the level 1 DFD with the team, I created a 3rd draft. I also created two sequence diagrams (I believe we'll only need two since our first two use cases follow the exact same sequance) as well as a State diagram (which proves to be tivial since we're not adding any states to PrairieLearn).  
Then, we had our first report with Scott. Feedback: clarify scalibility with our client; merge more frequently onto master; and, good luck with Docker.  
After the report, our team continued our meeting by some discussion before moving onto T-shirt sizing for our WBS/FBS. We all landed within 200 to 245 hours of work, so hopefully within budget! That is assuming we estimated everything correctly.  
Later, I converted my diagram sketches into UML using LucidChart - wouldn't recommend using their services because their free model is not good. However, the results are good enough for now. I didn't bother creating a UML version of the State diagram since it isn't a useful diagram.  
Finally, I wrote this weeks logs (up until now).  
Busy day!  

##  Thursday, June 1
I added the UML versions of the design diagrams I had created to the Design Doc draft. I also added the text to properly dress our three use cases as well as captions to every figure I added. I also removed plaace-holder sections for diagrams that we won't be using (collaborative, activity, state, component, and architecture) but left then in the table of contents in case we change our minds.  
I also spents about twenty more minutes fiddling with Docker after two of our group managed to get it to work on their machines. It still doesn't work on mine. Those working on Docker are going to try a build the Docker stuff from scratch, and I'll try another round of setting it up when that is completed.
I also copied the Use Case diagram and dressing to the Scope & Charter document (based on the rubric for the S&C doc). Just an exact copy-paste (except for the figure caption number, which was updated).  

##  Friday, June 2
Had a team meeting before our second report. We discussed in depth our issues with Docker (which have largely been resolved!) and exapnding upon our technical requirements, plus we talked about the existing documentaion for PrairieLearn and related systems. Now, there's only one team member (Nishant) that still has impeding Docker issues.  
My primary machine, an M1 desktop computer, has issues with Docker whereas my secondary machine, an old Intel Mac laptop, manages to spin up the Docker container just fine. While I would prefer to code on my primary machine, I will use my secondary for anything requiring Docker so that our team doesn't waste another dozen hours on Docker.  
We had our report with Scott but since time was short, we hadn't the chance to discuss much beyond Docker. We did get a general thumbs-up on our status, which is good.  
Our meeting with our client was very informative. Notably, we clarified some requirement and scope issues: the live creation of questions (such that a lecturer could poll their class) is entirely outside of our scope since the other group (the B-team) is working on it. The randomization of question parameters is still a stretch goal but should be easy to implement. We also added a new stretch goal: giving partial marks on submitted answers, a difficult task given we have to get a machine to determine the intent of a string of SQL. We also learned that, despite last year's PrairieLearn comments saying otherwise, it shouldn't be hard to put the open-source RelaX editor into PrairieLearn if we use iFrames. Our client also suggested we try to run SQLite directly in the web browser which should greatly help with our scalibility issues as well as simplify our data flow. Finally, our client said that we should incorperate the previous year's group's work in so far as allowing our client to use a single repo rather than mainting two for this one PrairieLearn project.  
Later, I updated several diagrams (use cases, level 0 & 1 DFD, and a sequence diagram) to reflect our changed requirements, removing all references to live generation of questions. I also updated the charter & scope as well as the design doc to reflect this.  
Then I updated some weekly logs.  