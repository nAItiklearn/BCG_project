"""
BCG GenAI Consulting Project - Task 2
Simple Rule-Based Financial Chatbot
Analyst: Naitik | Team Lead: Aisha
Client: Global Finance Corp (GFC)

This chatbot responds to 5 predefined financial queries using if-else logic.
Data source: Task 1 financial analysis of Microsoft, Tesla, and Apple (2022-2024)
"""

def simple_chatbot(user_query):
    """
    Rule-based chatbot that matches user queries to predefined responses.
    
    Args:
        user_query (str): The user's input query
        
    Returns:
        str: The predefined response or error message
    """
    
    # Predefined Query 1: Microsoft Revenue
    if user_query == "What was Microsoft's revenue in 2024?":
        return """
📊 Microsoft's Revenue in 2024:
   $245,122 million
   
💡 Context: This represents a 15.7% increase from 2023 ($211,915M) and a 23.6% 
   increase from 2022 ($198,270M), showing strong growth driven by Azure cloud 
   services and AI investments.
"""
    
    # Predefined Query 2: Apple Profit Margin
    elif user_query == "What is Apple's profit margin?":
        return """
📊 Apple's Profit Margin (2024):
   24.0%
   
💡 Context: This means Apple keeps $0.24 of every dollar in revenue as profit.
   While lower than Microsoft's 36%, it's still exceptionally strong compared to
   industry averages and significantly higher than Tesla's 7.3%.
"""
    
    # Predefined Query 3: Highest Cash Flow
    elif user_query == "Which company has the highest cash flow?":
        return """
📊 Operating Cash Flow Comparison (2024):
   🥇 Apple: $118,254 million
   🥇 Microsoft: $118,000 million (tied)
   🥉 Tesla: $14,900 million
   
💡 Context: Apple and Microsoft are essentially tied for the best cash flow,
   both generating nearly $118 billion from operations. This demonstrates their
   exceptional ability to convert revenue into actual cash.
"""
    
    # Predefined Query 4: Tesla Net Income Change
    elif user_query == "How did Tesla's net income change from 2023 to 2024?":
        return """
📊 Tesla's Net Income Change:
   2023: $14,997 million
   2024: $7,091 million
   Change: -52.7% (DECREASE)
   
💡 Context: Tesla's net income dropped by more than half, declining by $7,906M.
   This significant decrease reflects margin pressure from aggressive pricing
   strategies and increased competition in the EV market, despite stable revenue.
"""
    
    # Predefined Query 5: ROE Comparison
    elif user_query == "Compare the ROE of all three companies":
        return """
📊 Return on Equity (ROE) Comparison - 2024:
   🥇 Apple: 164.6%
   🥈 Microsoft: 52.8%
   🥉 Tesla: 9.6%
   
💡 Context: ROE measures how efficiently companies generate profits from 
   shareholder equity. Apple's exceptional 164.6% ROE is driven by its capital
   structure and massive share buyback programs. Microsoft's 52.8% is very strong,
   while Tesla's 9.6% reflects its profitability challenges in 2024.
"""
    
    # Unknown query
    else:
        return """
❌ Sorry, I can only answer these predefined queries:

1. "What was Microsoft's revenue in 2024?"
2. "What is Apple's profit margin?"
3. "Which company has the highest cash flow?"
4. "How did Tesla's net income change from 2023 to 2024?"
5. "Compare the ROE of all three companies"

Please type one of these queries exactly as shown (case-sensitive).
Type 'exit' to quit.
"""


def main():
    """Main function to run the chatbot interface"""
    
    print("=" * 80)
    print("🤖 GFC FINANCIAL CHATBOT - Rule-Based Prototype")
    print("=" * 80)
    print("\nWelcome! I can answer 5 predefined financial queries about")
    print("Microsoft, Tesla, and Apple based on their 10-K filings (2022-2024).")
    print("\nDeveloped by: Naitik | BCG GenAI Consulting Team")
    print("Client: Global Finance Corp (GFC)")
    print("\n" + "-" * 80)
    print("\n📋 AVAILABLE QUERIES:")
    print("1. What was Microsoft's revenue in 2024?")
    print("2. What is Apple's profit margin?")
    print("3. Which company has the highest cash flow?")
    print("4. How did Tesla's net income change from 2023 to 2024?")
    print("5. Compare the ROE of all three companies")
    print("\nType 'exit' to quit")
    print("-" * 80)
    
    # Main chatbot loop
    while True:
        print("\n💬 Your Query: ", end="")
        user_input = input()
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("\n" + "=" * 80)
            print("Thank you for using GFC Financial Chatbot!")
            print("Analysis powered by BCG GenAI Consulting Team")
            print("=" * 80)
            break
        
        # Get and display response
        response = simple_chatbot(user_input)
        print("\n🤖 Chatbot Response:")
        print(response)
        print("-" * 80)


if __name__ == "__main__":
    main()