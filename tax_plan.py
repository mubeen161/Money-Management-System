import streamlit as st
import openai
def main():
    st.title("Tax Planner")

    # Collect user information
    filing_status = st.selectbox("Select Filing Status", ["Single", "Married", "Head of Household"])
    dependents = st.number_input("Number of Dependents", min_value=0, value=0)

    # Collect income information
    st.header("Income Sources")
    salary = st.number_input("Salary(per year)", value=0)
    business_income = st.number_input("Business Income(per month)", value=0)
    investment_income = st.number_input("Investment Income(per month)", value=0)
    rental_income = st.number_input("Rental Income(per month))", value=0)
    other = st.number_input("other Income(per year))", value=0)

    # Collect education expenses
    st.header("Education Expenses")
    tuition_fees = st.number_input("Tuition and Fees", value=0)
    books_supplies = st.number_input("Books and Supplies", value=0)
    # Add more education-related inputs as needed

    # Collect healthcare expenses
    st.header("Healthcare Expenses")
    hsa_contributions = st.number_input("HSA Contributions", value=0)
    # Add more healthcare-related inputs as needed

    # Collect charitable contributions
    st.header("Charitable Contributions")
    cash_donations = st.number_input("Cash Donations", value=0)
    non_cash_donations = st.number_input("Non-Cash Donations", value=0)
    # Add more charitable contribution-related inputs as needed

    # Collect business expenses (if applicable)
    st.header("Business Expenses")
    business_expenses = st.number_input("Business Expenses", value=0)
    # Add more business-related inputs as needed

    # Collect tax planning strategy preferences
    st.header("Tax Planning Strategies")
    income_shifting = st.checkbox("Interest in Income Shifting Strategies")
    tax_efficient_investments = st.checkbox("Interest in Tax-Efficient Investments")
    # Add more tax planning strategy-related inputs as needed

    # Collect deduction preferences
    st.header("Deductions")
    mortgage_interest = st.checkbox("Mortgage Interest")
    medical_expenses = st.checkbox("Medical Expenses")
    # Add more deduction-related inputs as needed

    # Collect investment information
    st.header("Investment Strategies")
    investment_types = st.multiselect("Select Investment Types", ["Stocks", "Bonds", "Real Estate"])
    investment_duration = st.number_input("Investment Duration (in years)", min_value=0, value=0)
    # Add more investment-related inputs as needed

    # Collect retirement contribution information
    st.header("Retirement Contributions")
    retirement_contributions = st.number_input("Retirement Contributions", value=0)
    if st.button("Tax Computation"):
        openai.api_key = "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"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"""
            Act as a chartered accountant and I am your client. My details are:
            My filing status is {filing_status}, i have {dependents}dependents. Income Information is as follows:
            Salary Income (per year): {salary}
            Rental Income (per month): {rental_income}
            business income(per month): {business_income}
            Investment Income (per month): {investment_income}
            Other Sources of Income (per year): {other}
            Educational Expenses are tuition fees is {tuition_fees} and books supplies{books_supplies} and health contributions are {hsa_contributions} and Charitable contributions are {cash_donations} amount cash donations and {non_cash_donations} and non cash donations
            and business expenses are {business_expenses} and income shifting are {income_shifting} and tax efficient investments is {tax_efficient_investments} and investment types are {investment_types} and mortgage interest are {mortgage_interest} and investment duration and {investment_duration} and retirement contributions and {retirement_contributions}
            Deductions include:
            Medical Expenses (per year): {medical_expenses}
            
            I need to pay Tax, so now, based on the provided data, please help me in Tax planning and calculating in Indian rupees with all formulas and draw conclusions and give me output only in 175 words.
            """,
            max_tokens=400
        )

        st.subheader("Tax Computation Result:")
        st.write(response.choices[0].text)
if __name__ == "__main__":
    main()
