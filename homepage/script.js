$(document).ready(function(){
    $(window).scroll(function(){
        // sticky navbar on scroll script
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
        
        // scroll-up button show/hide script
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });

    // slide-up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
        // removing smooth scroll on slide-up button click
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function(){
        // applying again smooth scroll on menu items click
        $('html').css("scrollBehavior", "smooth");
    });

    // toggle menu/navbar script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

    // typing text animation script
    var typed = new Typed(".typing", {
        strings: ["FINANCE", "CASH", "FUNDS", "TO TAX", "BUDGETING", "MONEY MANAGEMENT"],
        typeSpeed: 35,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing-2", {
        strings: ["FINANCE", "CASH", "FUNDS", "TAX", "MONEY"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    // owl carousel script
    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeOut: 2000,
        autoplayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },
            600:{
                items: 2,
                nav: false
            },
            1000:{
                items: 3,
                nav: false
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const chatIcon = document.getElementById("chat-icon");
    const chatPopup = document.getElementById("chat-popup");
    const chatClose = document.getElementById("chat-close");
    const userInput = document.getElementById("user-input");
    const chatContent = document.getElementById("chat-content");
    const sendBtn = document.getElementById("send-btn");

    chatIcon.addEventListener("click", function () {
        chatPopup.style.display = "block";
        userInput.focus();
    });

    chatClose.addEventListener("click", function () {
        chatPopup.style.display = "none";
    });

    sendBtn.addEventListener("click", sendMessage);

    userInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const userMessage = userInput.value.trim();
        if (userMessage !== "") {
            addUserMessage("You: " + userMessage);
            const botMessage = findAnswer(userMessage);
            setTimeout(function () {
                addBotMessage("Bot: " + botMessage);
            }, 500); // Simulate bot response delay
            userInput.value = "";
            userInput.focus();
        }
    }

    function addUserMessage(message) {
        const userMessageDiv = document.createElement("div");
        userMessageDiv.className = "chat-message";
        userMessageDiv.textContent = message;
        chatContent.appendChild(userMessageDiv);
        chatContent.scrollTop = chatContent.scrollHeight;
    }

    function addBotMessage(message) {
        const botMessageDiv = document.createElement("div");
        botMessageDiv.className = "chat-message bot-message";
        botMessageDiv.textContent = message;
        chatContent.appendChild(botMessageDiv);
        chatContent.scrollTop = chatContent.scrollHeight;
    }

    function findAnswer(userInput) {
        const faq = {
            "financial wellness": "Financial wellness is the state of one's overall financial health. It involves effectively managing expenses, saving, investing, and planning for the future. Achieving financial wellness contributes to reduced stress and increased stability.",
            "stress management": "Managing stress in the financial context is crucial. Utilize budgeting tools, set financial goals, and explore investment options. Seeking professional advice can provide clarity and ease financial stress.",
            "mental health": "Financial well-being is interconnected with mental health. Stress over money matters can impact mental well-being. Establishing a healthy financial plan contributes to overall mental wellness.",
            "emotional well-being": "Emotional well-being is closely tied to financial stability. Addressing financial concerns through budgeting, savings, and investment strategies positively impacts emotional health.",
            "fiscal fitness": "Fiscal fitness involves maintaining a robust financial profile. Regularly assess and optimize your budget, savings, and investments to ensure long-term fiscal health.",
            "budgeting for health": "Budgeting for health encompasses allocating funds for medical expenses, insurance, and wellness activities. Prioritize health-related spending to maintain a balanced budget.",
            "anxiety relief": "Financial anxiety is common but can be managed. Establish a clear budget, create an emergency fund, and explore investment opportunities. Seeking financial advice can provide relief.",
            "depression prevention": "Preventing financial-related depression involves proactive planning. Develop a sustainable budget, save consistently, and explore investment options to secure your financial future.",
            "financial resilience": "Financial resilience is the ability to navigate challenges and recover from setbacks. Build resilience by diversifying investments, maintaining an emergency fund, and adapting to changing financial landscapes.",
            "obesity prevention": "Financial decisions impact lifestyle, including health. Prioritize budgeting for nutritious food and wellness activities to prevent health issues like obesity.",
            "healthy finances": "Maintaining healthy finances involves strategic planning. Budget effectively, save for goals, and invest wisely to ensure a secure financial future.",
            "stress-free budgeting": "Achieve stress-free budgeting through clear financial goals, efficient expense management, and regular financial assessments. Seek guidance to optimize your budget for peace of mind.", "financial literacy": "Financial literacy is the understanding of various financial aspects, including budgeting, investing, and managing debt. Enhance financial literacy through educational resources and expert guidance.",
            "investment strategies": "Explore diverse investment strategies based on risk tolerance and financial goals. Diversification, asset allocation, and staying informed contribute to effective investment decisions.",
            "retirement planning": "Secure your future with thorough retirement planning. Understand pension plans, 401(k)s, and other retirement vehicles to ensure financial stability during your retirement years.",
            "tax planning": "Optimize your tax liabilities through strategic tax planning. Leverage deductions, credits, and exemptions to legally minimize your tax burden and maximize savings.",
            "entrepreneurial finance": "For aspiring entrepreneurs, understand the financial aspects of starting and running a business. Develop a business plan, manage cash flow, and explore funding options for entrepreneurial success.",
            "credit score improvement": "Maintain a healthy credit score by managing debts responsibly. Timely payments, debt reduction strategies, and credit report monitoring contribute to score improvement.",
            "real estate investment": "Dive into real estate investment by understanding property markets, financing options, and potential returns. Real estate can be a valuable component of an investment portfolio.",
            "student loan management": "Effectively manage student loans by exploring repayment options, loan consolidation, and forgiveness programs. Develop a plan to navigate student loan debt responsibly.",
            "financial goal setting": "Achieve financial success by setting clear and achievable goals. Define short-term and long-term objectives to guide your financial decisions and actions.",
            "inheritance planning": "Plan for the future by considering inheritance matters. Understand estate planning, wills, and trusts to ensure a smooth transition of assets to the next generation.",
            "divorce and finance": "Navigate the financial implications of divorce by understanding asset division, alimony, and child support. Seek professional advice to secure your financial well-being during this transition.",
            "identity theft protection": "Protect yourself from identity theft by implementing security measures. Regularly monitor financial accounts, use strong passwords, and be cautious about sharing personal information.",
            "emergency preparedness": "Build financial resilience through emergency preparedness. Establish an emergency fund, review insurance coverage, and create a financial contingency plan for unexpected events.",
            "investment risks": "Evaluate and understand investment risks associated with different asset classes. Make informed decisions by considering risk factors and potential returns in your investment portfolio.",
            "sustainable finance": "Explore sustainable and ethical financial practices. Consider investments that align with environmental, social, and governance (ESG) criteria for a positive impact.",
            "financial empowerment": "Empower yourself with financial knowledge and skills. Take charge of your financial future by staying informed, making informed decisions, and seeking continuous improvement.",
            "cybersecurity in finance": "Safeguard your financial information online by practicing cybersecurity measures. Use secure networks, update software regularly, and be vigilant against online threats.",
            "socially responsible investing": "Incorporate social responsibility into your investment strategy. Choose investments that align with your values and contribute to positive social and environmental outcomes.",
            "wealth preservation": "Preserve and grow your wealth over time. Implement strategies such as estate planning, tax optimization, and diversification to ensure long-term financial prosperity.",
            "financial decision-making": "Enhance your financial decision-making skills. Evaluate options, weigh pros and cons, and consider the long-term impact of decisions on your overall financial well-being.",
        
        };
        
    
        const greetings = ["hi", "hello", "hey", "greetings"];

        const user_input_lower = userInput.toLowerCase();

        if (greetings.some(greeting => user_input_lower.includes(greeting))) {
            return "Hello! How can I assist you today?";
        }

        for (const question in faq) {
            const regex = new RegExp(`\\b${question}\\b`, 'i');
            if (regex.test(userInput)) {
                return faq[question];
            }
        }

        return "I'm here to help with financial questions. Feel free to ask.";
    }
});

