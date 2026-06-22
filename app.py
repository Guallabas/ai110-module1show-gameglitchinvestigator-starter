import random
import streamlit as st

#Bug 4: When clicking section normal it says 1 to 100 and when I click hard it says 1 to 50. I guess it should be backwards.
#Fixed with Auto. I just switched the ranges for normal and hard in the get_range_for_difficulty function. 
# Now normal is 1 to 50 and hard is 1 to 100.

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#Fifth bug. When I put hard mode. The secret was 18 and when I put 50 it said to go higher instead of saying go lower.
#FIXED With Auto and The sentences were backwords and fixed the part of comparisons becasue sometimes the secret is a 
# string and sometimes it is an int. So I made it so that if the attempt number is even then the secret is a string
# and if it is odd then the secret is an int. This way it will be consistent with the comparisons and the messages will be correct.

def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "⬇️ Go LOWER!"
        else:
            return "Too Low", "⬆️ Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "⬇️ Go LOWER!"
        return "Too Low", "⬆️ Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def get_hot_cold_feedback(guess, secret, low, high):
    """
    Calculate how 'hot' or 'cold' a guess is based on distance to secret.
    Returns a tuple: (emoji, description)
    """
    range_size = high - low
    distance = abs(guess - secret)
    
    if distance == 0:
        return "🔥🔥🔥", "BOILING - Exact match!"
    elif distance <= range_size * 0.1:  # Within 10% of range
        return "🔥🔥", "Very Hot!"
    elif distance <= range_size * 0.25:  # Within 25% of range
        return "🔥", "Hot"
    elif distance <= range_size * 0.5:  # Within 50% of range
        return "🌡️", "Warm"
    elif distance <= range_size * 0.75:  # Within 75% of range
        return "❄️", "Cold"
    else:
        return "❄️❄️", "Very Cold"

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

# Progress bar showing attempts remaining
attempts_remaining = attempt_limit - st.session_state.attempts
progress_pct = max(0, attempts_remaining / attempt_limit)
st.progress(progress_pct, text=f"Attempts: {max(0, attempts_remaining)}/{attempt_limit}")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempts_remaining)}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        if st.session_state.attempts % 2 == 0:
            secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)
        
        # Get hot/cold feedback
        hot_cold_emoji, hot_cold_desc = get_hot_cold_feedback(guess_int, st.session_state.secret, low, high)

        if show_hint:
            st.warning(f"{message}\n{hot_cold_emoji} {hot_cold_desc}")

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# Session history table
if st.session_state.history:
    st.divider()
    st.subheader("📊 Game Session Summary")
    
    history_data = []
    for idx, guess in enumerate(st.session_state.history, 1):
        if isinstance(guess, int):
            hot_cold_emoji, hot_cold_desc = get_hot_cold_feedback(guess, st.session_state.secret, low, high)
            if guess == st.session_state.secret:
                hint = "✅ Correct!"
            elif guess > st.session_state.secret:
                hint = "⬇️ Too High"
            else:
                hint = "⬆️ Too Low"
            distance = abs(guess - st.session_state.secret)
            history_data.append({
                "Attempt": idx,
                "Guess": guess,
                "Feedback": hint,
                "Distance": distance,
                "Temperature": f"{hot_cold_emoji} {hot_cold_desc}"
            })
    
    if history_data:
        st.dataframe(history_data, use_container_width=True)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
