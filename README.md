# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a Streamlit number guessing app with Easy, Normal, and Hard difficulty modes. The player tries to guess a secret number before the attempt limit expires, and the app gives higher/lower feedback for each guess.

I found several bugs: Easy mode still used the 1-100 range, Normal and Hard were swapped, the attempt counter started at 1 so players only got 7 guesses instead of 8 in Normal mode, and the hint comparison logic was broken by inconsistent secret-type handling. I also found that the shared game logic needed to be moved into `logic_utils.py` so it could be tested cleanly.

To fix it, I refactored `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py`, imported those functions into `app.py`, corrected the initial attempt state to 0, fixed new game secret generation to use the current difficulty range, and simplified `check_guess` to compare numbers directly.

## 📸 Demo Walkthrough

1. Open the app and select a difficulty level from the sidebar.
2. Enter a guess in the text input and click "Submit Guess 🚀".
3. The game responds with "Go LOWER" or "Go HIGHER" depending on whether the guess is above or below the secret.
4. The sidebar updates attempts remaining and the score updates after each guess.
5. When the correct number is guessed, the game shows a win message and the final score.

## 🧪 Test Results

➜  ai110-module1show-gameglitchinvestigator-starter git:(main) python3 -m pytest tests/test_game_logic.py

============================================================== test session starts ==============================================================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: /home/cesarcalderonn/codePath/ai/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 13 items                                                                                                                              

tests/test_game_logic.py .............                                                                                                    [100%]

============================================================== 13 passed in 0.07s ===============================================================


## 🚀 Stretch Features: Challenge 4 - Enhanced Game UI

✅ **Completed**: Added structured, user-friendly UI enhancements to improve player experience:

1. **Hot/Cold Feedback System**
   - Added `get_hot_cold_feedback()` function in `app.py` that calculates proximity to the secret number based on distance and displays emoji-based temperature feedback.
   - Feedback ranges from "🔥🔥🔥 BOILING" (exact) to "❄️❄️ Very Cold" (far away).
   - Displayed after each guess alongside the higher/lower hint.

2. **Visual Progress Indicator**
   - Added a Streamlit progress bar showing attempts remaining vs. the attempt limit.
   - Updates dynamically as the player makes guesses.
   - Located at the top of the game area for quick reference.

3. **Session History Table**
   - Displays a sortable dataframe summarizing all guesses made in the current game.
   - Columns: Attempt #, Guess, Feedback (Higher/Lower/Correct), Distance from Secret, Temperature (Hot/Cold emoji).
   - Helps players track their strategy and see how close they've been getting.
   - Rendered with `st.dataframe()` for interactivity.

4. **Color-Coded Feedback**
   - Hint messages use Streamlit's `st.warning()` for higher/lower feedback (yellow background).
   - Success messages for wins use `st.success()` (green background).
   - Error messages for invalid input use `st.error()` (red background).

**Modified functions:**
- `get_hot_cold_feedback(guess, secret, low, high)` — New helper that calculates proximity and returns emoji + description.
- Feedback display in the submit section now includes hot/cold data alongside the main hint.
- Session history table built dynamically from `st.session_state.history` with calculated distance and temperature values.
