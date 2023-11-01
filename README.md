# Django Technical Assessment Template

Hello, 

Today we received task from the Empire. They asked to go thru the death star project and find any potential problems.

They asked to write it all down and hand them the report or even fix it ourselves if it's possible.

They also added second requirement, It is said that in the alternative universe there are a bunch of movies about this universe. They would like to be able to get some more information about it. You can receive this information from special data transfer portal at https://swapi.dev/. They want to see this data on their computers. Those computers only support one type of interface called REST API. Here is what they want to know. 

* Based on starship's id or creator (producer of a film in which starship has been seen. there can be multiple people and multiple films) they want to know what species could have seen it (we can assume that any specie that has been in a given movie could have seen it).

* How much units of given starship (id) would they need to evacuate given planet (id or name)

* They also want to be able to create new types of starships

It's up to you to decide how would you like to represent the data.

#### Instructions

- The assessment will require you to:
    1. Implement REST API endpoints in Django
    2. Identify problem areas in the existing code such as bugs, quality, memory usage, performance, etc.
    3. Implement fixes for the problem areas.
- Create one assessment branch and PR to capture all of your work.
    - Optional, create a PR for your increments of work, i.e. grouped fixes, API endpoints, etc. Then merge each into the major assessment branch for review.
- You are free to use any third-party libraries and database of your choice. Make sure you share your reasoning behind choosing each of them.
- Basic tests for endpoints and their functionality are required. Their exact scope and form is left up to you.
- Create an `EXPLANATION.md` and think out-loud. Explain what you found, did, didn't do, and why. Share your reasoning. Be specific.
- When the entire assessment is done and ready for our review, email us. See [Git Workflow Tips](#git-workflow-tips) below.

Remember, this is your opportunity to show us how you think, approach development and problem-solving, your expertise, and your communication skills.

**🎉 Our hope is that you enjoy this technical assessment. *Have fun with it!* 🎉 **

#### Git Workflow Tips

Use your normal git workflow.

- We like to push commits throughout the day to ensure we are all collaborating with the most up-to-date code.
- When first opening the PR:
    - Set the PR to `draft`
    - Prefix the title as `[WIP]`
- Write something descriptive in the PR's opening discussion box. 
    - Hint: Think of this as a user story where you're building a PR for a feature. For us to do a code review, what do you think would help us? 
- Create one assessment branch and PR to capture all of your work.
    - Optional, create a PR for your increments of work, i.e. grouped fixes, API endpoints, etc. Then merge each into the major assessment branch for review.
- When the PR is ready for review:
     - Add a label: `needs: review`
     - Tag @tabrisrp (Remy) as the reviewer
     
####      

#### FAQ

##### Can I use third-party libraries?

Yes. You are free to use to choose any third-party library. Just make sure to explain why you choose each and how you are using them.

##### Can I use any database?

Yes. You are free to use to choose any database. Just make sure to explain why you choose it.

##### Do I need to write tests?

Yes. Basic tests for endpoints and their functionality are required. Their exact scope and form is left up to you.

##### Do my git commit history matter?

Yes it does. Why? It shows us how you work.

##### Does the number of fixes I find matter?

Yes. We know how many there are in the original app. We use an objective scorecard to determine P/F for the technical assessment.

##### How is the assessment reviewed?

We use an objective scoring system to get a baseline of the assessment. This scorecard lists all known issues in the app plus the criteria to evaluate the new endpoint implementation. Each item in the scorecard has points.

We will provide you with your score and feedback.

##### Where do I ask questions?

Create an issue in your assessment repo. Let's discuss things there. Ping us. We are happy to help and collaborate.
