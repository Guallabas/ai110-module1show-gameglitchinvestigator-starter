# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

First bug. When I played within the normal section I played through and the number never came correct I got to 99 it said higher then I put 100 and it said lower.

Second bug. When I play on easy mode it should be between 1 to 20 but it still counts to 1 to 100

Third bug. On the left section it say I have 8 attemtps to play but when I play and try to guess it only gives me 7 tries.

Fourth bug. When clicking section normal it says 1 to 100 and when I click hard it says 1 to 50. I guess it should be backwards. 

Fifth bug. When I put hard mode. The secret was 18 and when I put 50 it said to go higher instead of saying go lower.




- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 100 in Normal mode | The game should say the guess is too high and provide a lower hint | The game gave a wrong hint and the secret did not resolve correctly | No error |
| Select Easy mode | The range should show 1 to 20 and only allow easy mode guesses | The range still showed 1 to 100 in easy mode | No error |
| Start Normal mode and count attempts | The sidebar should show 8 attempts and the game should allow 8 guesses | The game ended after 7 guesses despite showing 8 attempts | No error |
| Choose Hard mode and guess above secret | The game should say "Go LOWER" when the guess is above the secret | The game said "Go HIGHER" for a guess above the secret | No error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
The Auto section of the chat in VSCode

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Suggested to change the code where the normal and hard mode where inverted. I ended up doing a Copy and launching it to see if it changed and worked and it did. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). 
Suggested to replace the whole code and make it simpler. Ended up testing it as well but it erased a lot of the things and looked empty and nothing like the project.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? By running the game after each code change and checking that the behavior matched the expected difficulty range and hint direction.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I tested the app manually by choosing Hard mode, then guessing a number above the secret and confirming the game said "Go LOWER." I also tried Easy mode and verified the sidebar range was 1 to 20 and the game accepted guesses in that smaller range.
- Did AI help you design or understand any tests? How? AI helped point to the code paths that looked wrong, so I knew to test the difficulty mapping and hint comparison logic directly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Streamlit reruns the whole script every time a widget changes, so the app is rebuilt from top to bottom on each click. Session state is how the app remembers values like the secret number, current score, and attempt count across those reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? I want to reuse the habit of reproducing a bug manually and then checking the fix right away instead of changing code and hoping it works.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? I would keep AI suggestions smaller and review the suggested changes carefully before applying them.
- In one or two sentences, describe how this project changed the way you think about AI generated code. This project showed me that AI-generated code can help identify bugs quickly, but I still need to test and understand the logic myself because the suggestions are not always fully correct.
