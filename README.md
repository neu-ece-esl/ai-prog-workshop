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
- Shift focus from **syntax and implementation** to **design, concept and intent**
- From **individual contributor** to **project team lead** where AI is a **collaborative team member**
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

Participants are introduced to four levels of AI programming assistance, each increasing in complexity and integration:

- **🔍 Code Review and Improvement**  
  Using AI (e.g., ChatGPT) to analyze, debug, and enhance existing code. Focus is placed on explanation, feedback, and code quality improvement.

- **🧠 Copilot Integration in VS Code**  
  Demonstrating GitHub Copilot’s contextual code completion to help scaffold and extend student code with intent-driven prompts.

- **⚙️ Auxiliary Code Generation**  
  Using large language models (e.g., Claude) for one-shot generation of scripts—e.g., data loaders, visualizations, and diagnostic utilities.

- **🧩 Agent Mode for Complex Projects**  
  Exploring how agentic AI systems can assist with larger, multi-file codebases. A live demonstration of a team-based project tool (e.g., user onboarding, team formation, collaboration chat) will illustrate the possibilities.

---

### 3. Hands-on Activity

Choose an AI assistance level—preferably one that challenges you beyond your current experience. Then:

- **Explore your chosen technology level.**
- **Design a classroom activity** that meaningfully integrates AI at this level.
- **Leverage an AI assistant** to help build or test your activity design.
- **Collaborate in small groups** to refine your ideas, with support available as needed.
- **Prepare to share** your activity and insights with the larger group.

---

### 4. Show & Tell / Reflection / Discussion

Share your activity ideas with the group and reflect on your experience:

- Discuss how integrating AI could impact your students’ learning.
- Consider ways these tools might reshape your assignments and course design.
- Identify potential challenges in assessment, fairness, or over-reliance on AI.
- Explore opportunities to foster deeper student engagement and ownership.

Open the floor for questions, suggestions, and further discussion.

---

## 📁 Repository Structure

The repository contains all materials used and generated during the workshop, organized for clarity and reuse:

```
ai-prog-workshop/
│
├── AI_code_review.ipynb
│ └─ Activity notebook for code review and improvement using ChatGPT
│
├── level2_copilot.ipynb
│ └─ Activity notebook demonstrating GitHub Copilot code completion
│
├── Data/
│ ├── KMeans_Clustering.ipynb
│ ├── Mall_Customers.csv
│ └─ Example data and clustering workflows used in activities
│
├── Media/
│ ├── Cluster.jpeg
│ ├── copilot_intro.gif
│ └─ Images and GIFs for demonstration and instruction
│
├── AI for review templates/
│ ├── Template#01.ipynb
│ ├── Template#02.ipynb
│ └─ Instructor templates for adapting the AI code review activity
│
├── README.md
│ └─ You’re here — full overview of the workshop and materials
```

---

## 🧑‍💻 Contributing & Continuing the Conversation

We welcome contributions from instructors adapting these resources for their own contexts. You can:

- Fork this repository and customize the materials
- Submit issues or suggestions for improvement
- Add your own classroom AI integration examples

Let’s build a collaborative, forward-thinking community of educators who embrace AI not as a shortcut—but as a tool for thoughtful, empowering, and meaningful learning.

## 🤝 Acknowledgments

This workshop is created by Gunar Schirner, Fatema Nafa, and Muhammad Salman at Northeastern University. 
Claude and other AI tools have been used in the process of ideation and drafting the workshop.