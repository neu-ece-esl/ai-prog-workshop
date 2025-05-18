# 🧠 Navigating Programming Education in AI Age

## Overview

The *Navigating Programming Education in AI Age* is designed for instructors who teach programming-oriented courses. The workshop explores how AI can shift the focus of programming from syntax and implementation details to system design, intentional development, and collaborative project management. Through interactive demos and guided activities, participants will experience different levels of AI assistance—including code review, Copilot integration, auxiliary code generation, and agent-based tools—and learn how to translate those experiences into impactful classroom practices.

---

## 🎯 Workshop Objectives

By the end of this workshop, participants will:

- Gain understanding of the evolving role of AI in programming education
- Explore multiple levels of AI programming assistance, from code review to agent-based systems
- Gain hands-on experience with AI tools in a programming context
- Start the design of classroom activities that meaningfully integrate AI support
- Reflect on the pedagogical shift from coding mechanics to design thinking and intent-driven development

---

## 🗓️ Logistics

- **Duration:** 1 hour
- **Target Audience:** Instructors of programming-oriented university courses
- **Format:** Interactive, hands-on
- **Requirements for Participants:**
  - Basic familiarity with programming concepts
  - A laptop for participating in activities
  - (Optional) Access to:
    - GitHub Copilot in VS Code
    - Claude (for script generation)
- **Agenda:**
  - 5 minutes: Overview of AI in programming education
  - 15 minutes: Exploration of AI programming assistance levels
  - 15 minutes: Hands-on activity design
  - 15–20 minutes: Show & Tell / Reflection

---

### 1. Overview

Increasing Abstraction Levels in Programming:
 - always working toward higher levels of abstraction
 - machine code, assembly, C/C++, Python, domain-specific languages (e.g. Faust for audio processing)
 - higher abstractions allow to develop more complex systems with less code focusing on the design of the system rather than the implementation details
 - With each abstraction level, developers were concerned about performance, and loss of control over the implementation details.
 - But higher abstractions dominate as compiler/runtime systems get better 
   - E.g. assembly only for utmost performance-critical code; allows using very specific-hardware features to eek out the last bit of performance (only where human is better than compiler/runtime)
- With GenAI, natural language is a new abstraction level, allowing to specify what a program should do, rather than being restricted to the syntax of a programming language

Paradigm Shift in Programming:  
- GenAI becomes peer programmer (collaborator), not just a tool
  - Helps generating simple scripts with a few sentences
  - Reviews, analyzes and gives improvement suggestions for existing code
  - Helping hand in code completion, repeating and expanding code patterns
  - Junior developer that develops complete projects across multiple files and abstractions 
- Libraries and APIs become more accessible (AI can generate project-specific code out of example snippets)
- Single developer can span many more programming languages


Limitations of GenAI:
- GenAI is not a replacement for human programmers
  - Can generate (complex) code, but it is driven by the creativity, intuition, experience and problem-solving skills of a human.
  - Limited to what it abstracted from training data (unless self-supervised training is used)

Changing Role of a Programmer: 
- Focus schifts from **syntax and implementation mechanics** to **design, clear vision and intent**
- From **individual contributor** to **project team lead** where AI is a **collaborative team member**
- Enables larger-scale, impactful projects through AI assistance
- Still needs to understand the entire stack of code and technologies, to critically evaluate collorator's suggestions and spot fix where needed.
  - Comparison with aircraft autopilot: 
    - Autopilot helps tremendously with low level tasks, but pilot is still in control
    - Pilot needs to understand the entire aircraft and its systems to be able to spot and fix issues

AI cannot build your custom, novel, high-impact project for you. It can help to build it faster and with less effort. It can help to focus on the design of the system rather than being overwhealmed with implementation details all the time. 

Question: How to guide students in programming education to become a technology leader, while still understanding the underlying technology details?

Up Next:
- Overview: AI programming assistance examples with increasing complexity and integration 
- Hands-on: design a classroom activity that integrates AI. 
- Reflection: curriculum design, course assignment, evaluation, and student engagement

--- 

### 2. AI Programming Assistance and Pedagogy

Exploration of AI programming assistance through four examples, sorted by increasing in complexity and integration:

- **⚙️ Auxiliary Code Generation** ([Details](1-script/README.md))
  One-shot generation of scripts beyond the course focus, e.g., data loaders, visualizations, and diagnostic utilities.

- **🔍 Code Review and Improvement** ([Details](2-review/README.md))
  Analyze, debug, and enhance existing code through help of AI. Focus is on explanation, feedback, and code quality improvement.

- **🧠 Copilot Integration in VS Code** ([Details](3-assist/README.md))
  Contextual code completion using GitHub Copilot to help scaffold, expand and refactor code with intent-driven prompts.

- **🧩 Agent Mode for Complex Projects** ([Details](4-vibe/README.md))
  Exploring how agentic AI systems can assist with larger, multi-file codebases. A live demonstration of a team-based project tool (e.g., user onboarding, team formation, collaboration chat) will illustrate the possibilities.

---

### 3. Hands-on Activity

Form groups 2 based on interest in AI assistance levels:
  - Preferably select a level challenging you beyond your current experience
  - Your team will be assigned a breakout room 

Then:

- **Explore your chosen technology level.**
- **Design a classroom activity** that meaningfully integrates AI at this level. Drive your design by considering (time permitting):
  - Expected outcomes/skills
  - Expressiveness and Scalability of Assessment 
  - Minimize anticipated challenges
- **Leverage AI assistants** to build your activity.
- **Prepare to share** your activity and insights with the larger group.

- Time: 15 minutes
- Starting point: [GitHub repository](https://github.com/neu-ece-esl/ai-prog-workshop) with example notebooks and templates.

---

### 4. Show & Tell / Reflection / Discussion

- **Show & Tell**: some groups share their activity ideas, challenges and insights. 
- **Reflection**: 
  - Discuss how integrating AI could impact your students’ learning.
  - Consider ways these tools might reshape your assignments and course design.
  - Identify potential challenges in assessment, fairness, or over-reliance on AI.
  - Explore opportunities to foster deeper student engagement and ownership.
- **Open Floor Discussion**


**Opportunities for Continued Exploration**

- Too many ideas, too many changes to explore in one hour!
- Launchpad for ongoing discussion and collaboration
- Regular (e.g., bi-weekly) meetups?
  - Share observations, challenges, and new ideas
  - Community to support each other in programming education revolution
- Next step: kick-off programming community meeting 

---

## 🧑‍💻 Contributing & Continuing the Conversation

We welcome contributions from instructors adapting these resources for their own contexts. You can:

- Fork this repository and customize the materials
- Submit issues or suggestions for improvement
- Add your own classroom AI integration examples

Let’s build a collaborative, forward-thinking community of educators who embrace AI not as a shortcut—but as a tool for thoughtful, empowering, and meaningful learning.

## 🤝 Acknowledgments

This workshop is created by [Gunar Schirner](https://coe.northeastern.edu/people/schirner-gunar/), [Fatema Nafa](https://coe.northeastern.edu/people/nafa-fatema/), and Muhammad Salman at Northeastern University.
Claude and other AI tools have been used in the process of ideation and drafting the workshop.