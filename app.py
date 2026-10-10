import streamlit as st
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

st.set_page_config(page_title="PySpark Practice", page_icon="⚡", layout="wide")

# -------------------------
# App state
# -------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# -------------------------
# Questions
# -------------------------
questions = [
    {
        "type": "mcq",
        "question": "Which PySpark transformation keeps only rows that match a condition?",
        "options": ["filter", "select", "groupBy", "collect"],
        "answer": "filter",
        "explanation": "The filter transformation keeps rows that satisfy a condition."
    },
    {
        "type": "mcq",
        "question": "What does the select() method do in PySpark?",
        "options": [
            "It removes rows",
            "It chooses specific columns",
            "It writes data to disk",
            "It sorts rows"
        ],
        "answer": "It chooses specific columns",
        "explanation": "select() is used to project one or more columns from a DataFrame."
    },
    {
        "type": "code",
        "question": "Write PySpark code that creates a DataFrame with 3 rows: (Alice, 28), (Bob, 35), (Charlie, 42). Then filter for age >= 30.",
        "starter_code": "from pyspark.sql import Row\n\ndata = [\n    Row(name='Alice', age=28),\n    Row(name='Bob', age=35),\n    Row(name='Charlie', age=42)\n]\n\ndf = spark.createDataFrame(data)\nresult = df.filter(df.age >= 30)\nresult.show()",
        "answer_checker": "age>=30",
        "explanation": "Use spark.createDataFrame() with Row objects, then call filter(df.age >= 30)."
    },
    {
        "type": "mcq",
        "question": "Which function would you use to count rows in a DataFrame?",
        "options": ["count()", "size()", "len()", "shape"],
        "answer": "count()",
        "explanation": "count() returns the number of rows in a DataFrame."
    }
]

# -------------------------
# Spark session
# -------------------------
@st.cache_resource
def get_spark():
    return SparkSession.builder.appName("PySpark Practice").master("local[*]").getOrCreate()

spark = get_spark()

# -------------------------
# Utility
# -------------------------
def next_question():
    if st.session_state.current_index < len(questions) - 1:
        st.session_state.current_index += 1
    else:
        st.session_state.current_index = 0

def reset_quiz():
    st.session_state.score = 0
    st.session_state.current_index = 0
    st.session_state.answers = {}

# -------------------------
# Main UI
# -------------------------
st.title("⚡ PySpark Practice")
st.caption("Practice fundamentals, transformations, and DataFrame logic.")

if len(st.session_state.answers) == 0:
    st.write("Start with a question below and track your score.")

question = questions[st.session_state.current_index]

st.subheader(f"Question {st.session_state.current_index + 1}/{len(questions)}")

if question["type"] == "mcq":
    st.markdown(f"**{question['question']}**")

    selected = st.radio("Choose an answer", question["options"], key=f"mcq_{st.session_state.current_index}")

    if st.button("Submit Answer", key=f"submit_mcq_{st.session_state.current_index}"):
        st.session_state.answers[st.session_state.current_index] = selected
        if selected == question["answer"]:
            st.session_state.score += 1
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong. Correct answer: {question['answer']}")
        st.info(question["explanation"])
        next_question()

elif question["type"] == "code":
    st.markdown(f"**{question['question']}**")
    code = st.text_area(
        "Write your PySpark code",
        value=question["starter_code"],
        height=220,
        key=f"code_{st.session_state.current_index}"
    )

    if st.button("Run Code", key=f"run_code_{st.session_state.current_index}"):
        try:
            namespace = {"spark": spark, "F": F}
            exec(code, namespace)
            result = namespace.get("result")
            if result is not None:
                st.write("Result:")
                result.show(truncate=False)
                rows = result.collect()
                expected_rows = [
                    {"name": "Bob", "age": 35},
                    {"name": "Charlie", "age": 42},
                ]

                # simple validation
                got = [row.asDict() for row in rows]
                if len(got) == 2 and all(r in got for r in expected_rows):
                    st.session_state.score += 1
                    st.success("Correct solution! ✅")
                    st.info(question["explanation"])
                else:
                    st.error("Your output is not matching the expected result yet.")
                    st.info(question["explanation"])
            else:
                st.warning("Your code did not define a `result` DataFrame.")
                st.info(question["explanation"])
        except Exception as e:
            st.exception("There was a Spark execution error.")
            st.info(question["explanation"])

        st.session_state.answers[st.session_state.current_index] = "attempted"
        next_question()

# -------------------------
# Score summary
# -------------------------
st.markdown("---")
st.subheader("Current Score")
st.metric("Score", f"{st.session_state.score} / {len(questions)}")

if st.button("Reset Quiz"):
    reset_quiz()
