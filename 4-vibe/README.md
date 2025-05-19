# 🚀 Level 4: Agent Mode for Complex Projects

Learn how to use GitHub Copilot Agent Mode in VS Code to tackle complex, multi-file projects that would normally be challenging in a classroom context. This activity demonstrates how AI agents can help students and educators manage sophisticated projects, improving learning outcomes while reducing implementation overhead.

---
## 🧩 Vibe Coding Overview
   - Focuses on rapid prototyping and collaborative iteration (with AI assistance)
   - Prioritizes agile evolution of  user experience and system flow over low-level details.
   - Enables quick project scaffolding and fast experimentation.
   - Mainstream in Startups and Accelerators [Synergy Labs](https://www.synergylabs.co/blog/what-is-vibe-coding-your-2025-vibe-coding-guide), 
   - [Y Combinator](https://www.ycombinator.com/blog/the-rise-of-vibe-coding/) :  
      > "Vibe coding is about getting something working fast, iterating in real time, and letting the product’s feel guide development decisions rather than rigid specs."  
   - 25% of YC’s current cohort have almost entirely AI-generated codebases [TechCrunch](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/)

   
   **References:**
   - [Y Combinator: The Rise of Vibe Coding](https://www.ycombinator.com/blog/the-rise-of-vibe-coding/)
   - [How AI is Changing Software Development](https://thenewstack.io/how-ai-is-changing-software-development/)
   - [GitHub Copilot Agent Mode](https://github.blog/news-insights/product-news/github-copilot-agent-mode-activated/)
   - [Top 10 Vibe Coding Tools](https://dev.to/therealmrmumba/top-10-vibe-coding-tools-that-feel-like-magic-in-2025-1md)
   - My own reflection in [AI for Human Instructors blog](https://teams.microsoft.com/l/message/19:1e2758ec49174425841771cc691dacb6@thread.tacv2/1744383783456?tenantId=a8eec281-aaa3-4dae-ac9b-9a398b9215e7&groupId=b5f3c736-7e2d-4bef-9b54-650ae2086004&parentMessageId=1744383783456&teamName=COE%20Faculty&channelName=AI%20for%20Human%20Instructors&createdTime=1744383783456)


## 🎓 Pedagogical Framing: Agent Mode for Complex Projects

- Experiential learning is key, often involving hands-on final class projects
- Class projects very time constrained (4-6 weeks) which limits scope
- Opportunity: increase experiential impact by using Agent Mode for project development
- Benefits:
    - Students can focus on system architecture and design principles
    - Tackle more ambitious projects that demonstrate real-world scenarios
    - More experiential learning in shorter timeframe
- Challenge: 
   - Students still need to understand the entire stack of code and technologies to critically evaluate collaborator's suggestions and spot fix where needed.
   - Large volumne of generated code becomes overwhelming
- Example: Grad course [High-level Design of HW/SW Systems](https://neu-ece-7368.github.io/)
   - Accelerate AI inference with GEMM Accelerator 
   - SoC and custom hardware simulation (focus HW/SW architecture) [Overview](https://neu-ece-7368.github.io/SystemCCosimulation.html)
   - Fall 2024 free to use any AI, but none did (yet) -- too complex?

---

## 🔍 Example: Group Organization Tool

- Organizing workshop participants into groups based on their interests
- Developing a new Web application too hard to do in a short time, generate?
- My Prompt for GitHub Copilot Agent Mode:
  > Generate a web page to which session participants can login (just by name no authentication required). After logging in, each participant needs to select from one of the following interests:
      - Code Improvement and Teaching
      - Code Assistance with CoPilot
      - Script Generation
      - Agent Mode for Projects
    A coordinator (username admin) finishes the first phase (after all participants have logged in). Then participants are paired together based on interests into teams (Teams get named team-1, team-2 ...). Each team should contain 2-2 members. The participants should get their team name and team members displayed once the decision is done. Optionally, members in the tam should be able to chat with each other
- [Chat](Chat.md) with the AI agent

---

## 🧑‍🏫 Instructor Activity: Enhancing Education through Agent Mode

Now that you've explored how Agent Mode can facilitate complex project development, consider how you might use this approach in your own teaching:

1. **Identify a complex, multi-component project** in your curriculum that would normally be challenging to implement in the available time.

2. **Draft a detailed system specification** that focuses on the learning objectives rather than implementation details.

3. **Create a prompt template** for students to use with Agent Mode that guides the development process while still requiring key architectural decisions.

4. **Consider assessment criteria** that emphasize understanding of system design, integration patterns, and architectural choices rather than code syntax.

This approach allows students to engage with more sophisticated projects than would otherwise be possible, developing valuable system thinking skills while still mastering programming concepts central to your course.

---

## 📚 Resources

- [GitHub Copilot Agent Mode Documentation](https://docs.github.com/en/copilot/github-copilot-in-vscode/using-the-agent-view-in-github-copilot)
- [GitHub Copilot Agent Mode Announcement](https://github.blog/news-insights/product-news/github-copilot-agent-mode-activated/)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)
