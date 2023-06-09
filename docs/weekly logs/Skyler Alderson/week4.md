# Week 4

## Sunday, June 4
We got together for a team meeting to go over our final version of the Charter document as well as the draft of the Design document. We notably added new requirements (student can generate new question variant, professor can see solution, and professor can set question solution visibility) as well as split our current use cases into much smaller sizes. There were also plenty of minor edits, both to fornmatting and to contents.  
I then spent a while updataing our diagrams to relfect our new requirements and use cases. I changed the use case diagrams and the DFDs, but left the sequence diagram unchanged. While a sequence diagram should show only one use case, doing so would lead to trivial sequence diagrams (user --> system, system --> user, sequence complete). I might update our sequence diagrams later if we deem it necessary but right now I don't see a point.  
Then I updated weekly logs.  

## Wednesday, June 7
Before our team's report, we got together (as we have done and will continue to do on days with a report) so we could work as a group and discuss. I continued to read PrairieLearn documentation, particularly on the "Zygote process" describes that Python enviroments are forked whenever a fresh enviroment is required. I also made some minor edits to various design documents.  
We had our report where most of the feedback was about small changes to diagrams, as well as how we needed more sequence diagrams. Otherwise, our draft moslty looked fine.  
Then we had a meeting with our client where we talked about what we would need for an MVP (the base lifecycle for a question), whether our UI mockups looked good (they did, but schemas go above the editor and the output below), and we disussed how we would hanlde questions with several sub-components. If we have a database for a question, then the contents of the database may change depending on the commands the student runs. In the end, we didn't get to a clear conclusion: "it's something to think about".  
I then worked on diagrams. I added IDs to the use cases, changed the wording on the DFDs to more clearly show how data was being transformed (used imperative verbs), and then made five sequence diagrams to fully cover our nine (or six, depending on how you count them) requirements.  

## Thursday, June 8
Before the team meeting, I made a sequence diagram to show the basic lifecycle of a question on the default PrairieLearn system. I did this such that our presentation and design doc could better show how what we're working on expands and changes the existing system. I also fixed a few issues with other diagrams that I had noticed the day before.  
Our meeting fully reviewed both the presentation and the design doc. We made many, many small changes. Most aren't worth discussing, but one of the larger changes was to the level 1 DFD to show that the embedded interface and the question instance database existing seperately from PrairieLearn server and on the user's browser. We also practiced our presentation - first try was at 12m and 18s, perfect! Once we were satisfied, I uploaded both documents to where they needed to go.  
Then I updated weekly logs.  