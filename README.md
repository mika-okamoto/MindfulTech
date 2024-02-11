# MindfulAI: Mental Health in the Tech Workplace

Identifying and supporting employees at risk for anxiety and mood disorders through data-driven analysis of risk factors and a custom, patient-specific LLM chatbot enhanced with clinical knowledge.

<img width="318" alt="image" Class="center" src="https://github.com/mika-okamoto/MindfulTech/assets/43559753/ee53fe98-641c-479d-ac3b-324322f8bb8b">

# The problem:

Amidst widespread layoffs and ever-intensifying working conditions, stress in the tech sector is at an all time high, with Forbes finding almost half of employees are stressed ‘often’ or ‘very often,’ to an extent that it impairs their quality of work. Unfortunately, given the status of the labor market, the worker toolkit to combat unhealthy environments is sparse – irrespective of material truth, the perception that employees may face backlash is a substantial deterrent for speaking out about mental health concerns or seeking professional treatment.

Through comparative analysis of an employee’s survey results with a large corpus of open source data, we make predictions about whether an employee has an anxiety or mood disorder: these are distinct from general low-mood symptoms and represent that anxiety or depression is hampering an individual’s ability to live their life normally. Anxiety and mood disorders are highly treatable. We believe that our prompting may suggest to at-risk employees that their stresses are beyond normal expectations for someone in technology, validate their feelings, and inspire them to seek formal treatment.

The second feature of our project leverages generative AI to resolve employee concerns in a specific, clinically-informed manner. Anxiety and depression are confusing and online resources for help are often generic or flatly incorrect – and according to the Journal of Medical Internet Research, may even decrease help-seeking behaviors in young people. We hope to answer questions in a convenient, private manner while guiding at-risk employees to proper medical resources.

We hope that MindfulAI will raise awareness for mental health in tech workplaces and spark discussions both among colleagues and incorporating leadership. After all, keeping employees in a good psychological state will reduce burnout and improve productivity and morale, which is to the benefit of both businesses and workers.

# Our Approach and Key Challenges:

Creating a multi-level, technologically-sophisticated web-application over the course of a day and a half was daunting – we’ll survey our biggest, most-instructive hurdles and how we overcame them.

**Data:** data on mental health in technology is rare – the largest and most comprehensive dataset was from Open Sourcing Mental Illness and was highly disorganized. With arbitrary response formatting and vague questions, we had a tedious cleanup task ahead. We excluded implausible entries (including employees of ages 3 and 324), aggregated questions that were dependent on others (‘if so…’), and painstakingly interpreted text fields as rescaled and normalized numerical values.

**Predictive Modeling:** We experimented with numerous models ranging from ensemble learning to neural nets, before selecting random forests – semantically suitable due to hierarchical question structures. At first, we encountered deceptively high model accuracy and F1-score, which we identified as misleading due to bias introduced during response collection. After imputing misleading data, accuracy was lowered substantially, though some lost accuracy was recovered after fine-tuning.

**Generative AI**: A jig-saw within the larger web-dev puzzle, with an objective of personalized, context-specific, and relevant answers for users. Faced with poor documentation and limited practical experience, we endeavored to stitch numerous APIs while incorporating state-of-the-art research in retrieval augmented generation (combining real-world, user-specific knowledge into the large-language-model). Ultimately, leveraging a combination of custom memory modules of past conversations when we could not work around the pre-built, along with clever prompt-engineering to overcome token limits, we created a language model that we believe effectively addressed user needs — see for yourself!

