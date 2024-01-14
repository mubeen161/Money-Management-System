import streamlit as st
import openai
session_state = st.session_state
def main1():
    st.title("Tax Computation")
    st.header("Personal Information")

    # Personal Details
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, value=0)

    st.header("Income Information")

    # Income Inputs
    salary_income = st.number_input("Salary Income (per year)", value=0.0)
    rental_income = st.number_input("Rental Income (per month)", value=0.0)
    investment_income = st.number_input("Investment Income (per month)", value=0.0)
    other_income = st.number_input("Other Sources of Income (per year)", value=0.0)
    
    st.header("Deductions")

    # Deduction Inputs
    rent_deduction = st.number_input("Rent Deduction (per month)", value=0.0)
    medical_expenses = st.number_input("Medical Expenses (per year)", value=0.0)
    charitable_contributions = st.number_input("Charitable Contributions (per year)", value=0.0)
    job_related_expenses = st.number_input("Job-related Expenses (per month)", value=0.0)
    other_deductions = st.number_input("Other Deductions (per year)", value=0.0)
    
    st.header("Exemptions and Credits")

    # Exemptions and Credits Inputs
    dependents = st.number_input("Number of Dependents", value=0)
    eitc = st.number_input("Earned Income Tax Credit (EITC) (per year)", value=0.0)
    child_tax_credit = st.number_input("Child Tax Credit (per year)", value=0.0)
    education_credits = st.number_input("Education Credits (per year)", value=0.0)

    st.header("Retirement Contributions")

    # Retirement Contribution Input
    ira_contributions = st.number_input("Contributions to Individual Retirement Accounts (IRAs)(per year)", value=0.0)

    if st.button("Tax Computation"):
        openai.api_key = "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"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"""
            Act as a chartered accountant and I am your client. My details are:
            I am {name}, I am an individual. My age is {age}, and my gender is {gender}. My 
            Income Information is as follows:
            Salary Income (per year): {salary_income}
            Rental Income (per month): {rental_income}
            Investment Income (per month): {investment_income}
            Other Sources of Income (per year): {other_income}

            Deductions include:
            Rent Expenses (per month): {rent_deduction}
            Medical Expenses (per year): {medical_expenses}
            Charitable Contributions (per year): {charitable_contributions}
            Job-related Expenses (per month): {job_related_expenses}
            Other Deductions (per year): {other_deductions}

            Exemptions and Credits:
            Number of Dependents: {dependents}
            Earned Income Tax Credit (EITC) (per year): {eitc}
            Child Tax Credit (per year): {child_tax_credit}
            Education Credits (per year): {education_credits}

            Retirement Contributions:
            Contributions to IRAs (per year): {ira_contributions}.
            I need to pay Tax, so now, based on the provided data, please help me in Tax Computation in Indian rupees with all formulas and proper calculates and draw conclusions and give me output only in 175 words.
            """,
            max_tokens=400
        )

        st.subheader("Tax Computation Result:")
        st.write(response.choices[0].text)
        session_state.result = response.choices[0].text  # Store the result in session state

    # Laws and Tips Button
    if st.button("Laws and Tips on Tax Computation"):
        if 'result' in session_state:
            response2 = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=f"apply laws and tips to save tax on my provided tax computation{session_state.result}, give output in points with proper laws and facts and max words are 250",
                max_tokens=250
            )
            st.write(response2.choices[0].text)

if __name__ == "__main__":
    main1()
