import streamlit as st

st.title("🎓 Student Success Prediction - Pro Version")
st.write("Enter student details to get Grade, Risk, Placement chance & Study Plan")

# Input fields
hours = st.number_input("Study Hours per Day", min_value=0.0, max_value=12.0, value=3.0)
attendance = st.number_input("Attendance %", min_value=0, max_value=100, value=75)
prev_marks = st.number_input("Previous Marks %", min_value=0, max_value=100, value=70)

# Grade calculation
def get_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else: return "F"

# Placement Probability
def get_placement_prob(att, marks, hours):
    score = (att * 0.4) + (marks * 0.4) + (hours * 10 * 0.2)
    return min(100, int(score))

# Dropout Risk
def get_dropout_risk(att, marks):
    if att < 60 or marks < 50:
        return "🔴 High Risk"
    elif att < 75 or marks < 65:
        return "🟡 Medium Risk"
    else:
        return "🟢 Low Risk"

if st.button("🔮 Predict Performance"):
    score = (hours * 10) + attendance + prev_marks
    
    # 1. Grade
    grade = get_grade(prev_marks)
    st.subheader(f"📊 Predicted Grade: {grade}")
    
    # 2. Pass/Fail
    if score >= 150:
        st.success("✅ Pass - Good Performance")
        st.write("Continue your good work!")
    else:
        st.error("❌ At Risk")
        
        # 3. Dropout Risk
        st.warning(f"**Dropout Risk:** {get_dropout_risk(attendance, prev_marks)}")
        
        # 4. Placement Probability
        placement = get_placement_prob(attendance, prev_marks, hours)
        st.info(f"**Placement Probability:** {placement}%")
        
        st.write("---")
        st.subheader("**Analysis & Growth Plan**")
        
        if hours < 3:
            st.write("**Problem 1:** Study hours are very low.")
            st.write("**Solution:** Study at least 3-4 hours daily with short breaks.")
        if attendance < 75:
            st.write("**Problem 2:** Attendance is below 75%.")
            st.write("**Solution:** Attend classes regularly to understand concepts.")
        if prev_marks < 60:
            st.write("**Problem 3:** Previous marks are below 60.")
            st.write("**Solution:** Practice more questions and revise daily.")
    
    # 5. Recommended Skills
    st.write("---")
    st.subheader("**💡 Recommended Skills**")
    st.write("- Communication Skills")
    st.write("- Python Programming")
    st.write("- Time Management")
    
    # 6. Study Plan
    st.subheader("**📅 30-Day Study Plan**")
    st.write("Week 1: Basics revision + 2 hrs daily")
    st.write("Week 2: Practice problems + 3 hrs daily") 
    st.write("Week 3: Mock tests + 4 hrs daily")
    st.write("Week 4: Revision + Interview prep")

st.write("---")
st.caption("Pro Version with Grade, Placement & Dropout Analysis")