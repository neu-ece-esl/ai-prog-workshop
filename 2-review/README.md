# 🔍 Level 2: AI as a Code Review and Improvement Tool

### 🎯 Objective:
Learn how to use AI (e.g., ChatGPT) as a coach to review, debug, and improve existing code. This activity demonstrates how AI can support student learning through hint-driven feedback, error identification, and code optimization — without directly giving away the answer.

---

## 🧠 Concept: AI for Code Review and Improvement

In this activity, we explore how AI — such as ChatGPT — can be used to review existing code, identify bugs, and suggest improvements. Instead of using AI to *write* code from scratch, we focus on using it as a **coach** that helps students **understand**, **debug**, and **refactor** code they are already working with.

---

## 🎓 Pedagogical Framing

The goal is not to let AI do the thinking for students, but rather to use it to **scaffold their problem-solving process**. When students encounter faulty code:

- They're first encouraged to **analyze it themselves**.
- Then, AI can be used to provide **targeted hints** or **explanations**.
- Students are expected to **reflect on** and **critically evaluate** AI's suggestions.

This approach promotes:
- Deeper understanding of algorithms and logic
- Collaborative learning through discussion of AI output
- A mindset of *debugging as discovery*, not just fixing

## 🟨 Step 3: Faulty Merge Sort Code (Code cell)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid]) 

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) or j < len(right):
        
        if i < len(left) and (j >= len(right) or left[i] < right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    return sorted_list
```

---

## 🤖 Suggested AI Prompt

Once you've attempted to understand the code and identify possible bugs yourself, you may use the following prompt to ask an AI assistant (like ChatGPT) for help:

> **Prompt:**
>
> "Can you review the following merge sort implementation and highlight any possible errors or inefficiencies? Please explain what is wrong, suggest corrections, and explain how the code can be made more efficient and robust."

Copy the full code above and paste it along with this prompt into ChatGPT or your AI tool of choice.

---

## 🤖 Sample AI Response (Summary)

Here's an example of how an AI assistant like ChatGPT might respond to your prompt:

---

### 🔍 Identified Issues

1. **Incorrect Slice in Recursive Call**
   - `right = merge_sort(arr[mid])` should be `arr[mid:]`.

2. **Unsafe Loop Condition**
   - `while i < len(left) or j < len(right)` should be `and` to avoid `IndexError`.

3. **Missing Appending of Remaining Elements**
   - Any unprocessed elements in `left` or `right` should be appended after the loop using:
     ```python
     sorted_list.extend(left[i:])
     sorted_list.extend(right[j:])
     ```

---

### ✅ Corrected Version (Brief)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
```

---

## 💬 Reflection

After you receive the AI's response, ask yourself:
- Did the AI catch all the subtle bugs?
- Do you understand *why* those bugs matter?
- Can you think of edge cases that would cause the code to fail?
- Would your students benefit from this kind of hint-driven support in your own teaching?
- Do you agree with the AI reasoning?
- what do you learn from this debugging task?

---

## 🧑‍🏫 Instructor Activity: Designing an AI-Supported Code Review Task

Now that you've explored how AI tools like ChatGPT can assist in identifying and improving faulty code, it's your turn to step into the role of a learning designer.

### 🎓 Your Task:
Design a **classroom activity** where students use an AI assistant (e.g., ChatGPT) as a **code reviewer** to enhance their debugging, reasoning, and reflection skills.

---

### 💡 Design Considerations:

#### 🔍 What kind of faulty code will you use?
- An algorithm with subtle logic bugs?
- An object-oriented implementation with structural issues?
- A larger codebase with redundant or inefficient logic?

#### 🤖 How will students interact with the AI?
- To request **hints** or **partial feedback**?
- To **compare their own debugging** with AI-generated suggestions?
- To **evaluate the quality** and accuracy of AI's corrections?

#### 🧠 How will you structure the learning process?
- Will students try to fix the code manually before prompting the AI?
- Will you design it as a **collaborative discussion** or peer review?
- Will they use the AI's responses as a base to **refactor, optimize, or document** the code?

#### 🧩 What use cases or skills will this support?
- Debugging and tracing subtle errors
- Reverse engineering unfamiliar code
- Navigating and understanding **large or poorly documented codebases**

---

### 📝 Suggested Output:

Briefly outline your proposed classroom activity:

- 📍 **Topic or Concept**: What course topic does this support?  
- 💥 **Faulty Code Example**: What kind of bugs or issues will students investigate?  
- 🤝 **AI Interaction**: How will students engage with the AI to support their thinking?  
- 🎯 **Learning Outcomes**: What should students demonstrate or reflect on by the end?

> This activity is a great opportunity to build something you can adapt for your course, especially if you teach algorithms, software design, or debugging strategy.

---
