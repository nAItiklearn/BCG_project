"""
BCG GenAI Consulting Project - Task 2 (Enhanced)
Advanced NLP-Powered Financial Chatbot
Analyst: Naitik | Team Lead: Aisha
Client: Global Finance Corp (GFC)

This enhanced version uses Natural Language Processing to understand
query variations, handle typos, and extract entities intelligently.
"""

import spacy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

# Load spaCy NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    print("⚠️  spaCy model not found. Run: python -m spacy download en_core_web_sm")
    exit()

class NLPFinancialChatbot:
    """
    Enhanced chatbot with Natural Language Processing capabilities
    """
    
    def __init__(self):
        # Financial data from Task 1
        self.financial_data = {
            'Microsoft': {
                '2024': {'revenue': 245122, 'net_income': 88136, 'profit_margin': 36.0, 
                        'cash_flow': 118000, 'roe': 52.8, 'assets': 512163},
                '2023': {'revenue': 211915, 'net_income': 72361, 'profit_margin': 34.2,
                        'cash_flow': 87582, 'roe': 45.2, 'assets': 411976},
                '2022': {'revenue': 198270, 'net_income': 72738, 'profit_margin': 36.7,
                        'cash_flow': 89035, 'roe': 43.6, 'assets': 364840}
            },
            'Tesla': {
                '2024': {'revenue': 97690, 'net_income': 7091, 'profit_margin': 7.3,
                        'cash_flow': 14900, 'roe': 9.6, 'assets': 122070},
                '2023': {'revenue': 96773, 'net_income': 14997, 'profit_margin': 15.5,
                        'cash_flow': 13256, 'roe': 23.6, 'assets': 106618},
                '2022': {'revenue': 81462, 'net_income': 12556, 'profit_margin': 15.4,
                        'cash_flow': 14724, 'roe': 27.4, 'assets': 82338}
            },
            'Apple': {
                '2024': {'revenue': 391035, 'net_income': 93736, 'profit_margin': 24.0,
                        'cash_flow': 118254, 'roe': 164.6, 'assets': 364980},
                '2023': {'revenue': 383285, 'net_income': 96995, 'profit_margin': 25.3,
                        'cash_flow': 110543, 'roe': 171.7, 'assets': 352583},
                '2022': {'revenue': 394328, 'net_income': 99803, 'profit_margin': 25.3,
                        'cash_flow': 122151, 'roe': 196.1, 'assets': 352755}
            }
        }
        
        # Company name mappings (includes abbreviations and variations)
        self.company_mappings = {
            'microsoft': 'Microsoft',
            'msft': 'Microsoft',
            'ms': 'Microsoft',
            'tesla': 'Tesla',
            'tsla': 'Tesla',
            'apple': 'Apple',
            'aapl': 'Apple'
        }
        
        # Metric synonyms
        self.metric_synonyms = {
            'revenue': ['revenue', 'sales', 'income', 'earnings', 'turnover'],
            'net_income': ['net income', 'profit', 'earnings', 'bottom line', 'net profit'],
            'profit_margin': ['profit margin', 'margin', 'profitability', 'profit %'],
            'cash_flow': ['cash flow', 'operating cash', 'cash', 'ocf'],
            'roe': ['roe', 'return on equity', 'equity return'],
            'assets': ['assets', 'total assets']
        }
        
        # Intent patterns
        self.intent_patterns = {
            'get_metric': ['what', 'show', 'tell', 'get', 'how much', "what's", 'give me'],
            'compare': ['compare', 'comparison', 'vs', 'versus', 'difference between'],
            'trend': ['trend', 'change', 'growth', 'over time', 'historical'],
            'ranking': ['best', 'highest', 'lowest', 'top', 'worst', 'which', 'who']
        }
    
    def extract_company(self, query):
        """Extract company name using NLP and fuzzy matching"""
        query_lower = query.lower()
        
        # First try direct mapping
        for abbr, full_name in self.company_mappings.items():
            if abbr in query_lower:
                return full_name
        
        # Use spaCy for entity recognition
        doc = nlp(query)
        for ent in doc.ents:
            if ent.label_ == "ORG":
                company_match = process.extractOne(ent.text.lower(), 
                                                   self.company_mappings.keys())
                if company_match and company_match[1] > 70:
                    return self.company_mappings[company_match[0]]
        
        # Fuzzy match against company names
        for company in ['Microsoft', 'Tesla', 'Apple']:
            if fuzz.partial_ratio(company.lower(), query_lower) > 80:
                return company
        
        return None
    
    def extract_year(self, query):
        """Extract year from query"""
        # Look for 4-digit years
        years = re.findall(r'20(22|23|24)', query)
        if years:
            return '20' + years[0]
        
        # Keywords for latest year
        if any(word in query.lower() for word in ['latest', 'current', 'recent', 'now', 'today']):
            return '2024'
        
        return '2024'  # Default to latest
    
    def extract_metric(self, query):
        """Extract financial metric using synonym matching"""
        query_lower = query.lower()
        
        for metric, synonyms in self.metric_synonyms.items():
            for synonym in synonyms:
                if synonym in query_lower:
                    return metric
        
        return None
    
    def detect_intent(self, query):
        """Detect user intent using keyword matching"""
        query_lower = query.lower()
        
        for intent, keywords in self.intent_patterns.items():
            for keyword in keywords:
                if keyword in query_lower:
                    return intent
        
        return 'get_metric'  # Default intent
    
    def format_currency(self, amount):
        """Format currency values"""
        return f"${amount:,.0f}M"
    
    def format_percentage(self, value):
        """Format percentage values"""
        return f"{value:.1f}%"
    
    def get_metric_value(self, company, year, metric):
        """Get specific metric value"""
        try:
            return self.financial_data[company][year][metric]
        except KeyError:
            return None
    
    def handle_get_metric(self, company, year, metric):
        """Handle queries asking for specific metric"""
        value = self.get_metric_value(company, year, metric)
        
        if value is None:
            return f"Sorry, I don't have {metric} data for {company} in {year}."
        
        # Format based on metric type
        if metric in ['revenue', 'net_income', 'cash_flow', 'assets']:
            formatted_value = self.format_currency(value)
        else:
            formatted_value = self.format_percentage(value)
        
        response = f"📊 **{company}'s {metric.replace('_', ' ').title()} in {year}:**\n"
        response += f"   {formatted_value}\n\n"
        
        # Add context
        if metric == 'revenue':
            response += "💡 This represents the total revenue generated during the fiscal year."
        elif metric == 'net_income':
            response += "💡 This is the company's bottom-line profit after all expenses."
        elif metric == 'profit_margin':
            response += f"💡 {company} keeps {formatted_value} of every dollar as profit."
        elif metric == 'cash_flow':
            response += "💡 This shows cash generated from core business operations."
        elif metric == 'roe':
            response += "💡 ROE measures how efficiently the company generates profits from equity."
        
        return response
    
    def handle_compare(self, metric, year='2024'):
        """Handle comparison queries"""
        if not metric:
            return "Please specify which metric you'd like to compare (e.g., revenue, profit margin)."
        
        response = f"📊 **{metric.replace('_', ' ').title()} Comparison ({year}):**\n\n"
        
        companies_data = []
        for company in ['Microsoft', 'Tesla', 'Apple']:
            value = self.get_metric_value(company, year, metric)
            if value:
                companies_data.append((company, value))
        
        # Sort by value
        companies_data.sort(key=lambda x: x[1], reverse=True)
        
        # Display with medals
        medals = ['🥇', '🥈', '🥉']
        for i, (company, value) in enumerate(companies_data):
            medal = medals[i] if i < 3 else '  '
            if metric in ['revenue', 'net_income', 'cash_flow', 'assets']:
                formatted = self.format_currency(value)
            else:
                formatted = self.format_percentage(value)
            response += f"{medal} **{company}**: {formatted}\n"
        
        winner = companies_data[0][0]
        response += f"\n💡 **{winner}** leads in {metric.replace('_', ' ')} for {year}."
        
        return response
    
    def handle_trend(self, company, metric):
        """Handle trend analysis queries"""
        if not company or not metric:
            return "Please specify both a company and metric for trend analysis."
        
        response = f"📈 **{company}'s {metric.replace('_', ' ').title()} Trend (2022-2024):**\n\n"
        
        for year in ['2022', '2023', '2024']:
            value = self.get_metric_value(company, year, metric)
            if value:
                if metric in ['revenue', 'net_income', 'cash_flow', 'assets']:
                    formatted = self.format_currency(value)
                else:
                    formatted = self.format_percentage(value)
                response += f"- **{year}**: {formatted}\n"
        
        # Calculate change
        start_val = self.get_metric_value(company, '2022', metric)
        end_val = self.get_metric_value(company, '2024', metric)
        
        if start_val and end_val:
            change_pct = ((end_val - start_val) / start_val) * 100
            if change_pct > 0:
                response += f"\n📈 **Growth**: {change_pct:.1f}% increase from 2022 to 2024"
            else:
                response += f"\n📉 **Decline**: {abs(change_pct):.1f}% decrease from 2022 to 2024"
        
        return response
    
    def handle_ranking(self, metric, year='2024'):
        """Handle ranking queries (best/worst)"""
        return self.handle_compare(metric, year)
    
    def process_query(self, query):
        """Main query processing with NLP"""
        
        # Detect intent
        intent = self.detect_intent(query)
        
        # Extract entities
        company = self.extract_company(query)
        year = self.extract_year(query)
        metric = self.extract_metric(query)
        
        # Route to appropriate handler
        if intent == 'compare' or intent == 'ranking':
            return self.handle_compare(metric, year)
        elif intent == 'trend':
            return self.handle_trend(company, metric)
        elif intent == 'get_metric':
            if company and metric:
                return self.handle_get_metric(company, year, metric)
        
        # If we couldn't understand
        return self.provide_help()
    
    def provide_help(self):
        """Provide help message"""
        return """
💡 **I can help you with financial insights! Try questions like:**

**Specific Queries:**
- "What was Microsoft's revenue in 2024?"
- "Show me Apple's profit margin"
- "Tesla cash flow"

**Comparisons:**
- "Compare profit margins"
- "Which company has the best revenue?"

**Trends:**
- "Show Apple's revenue trend"
- "Tesla net income over time"

**Flexible Queries:**
- Works with company abbreviations (MSFT, AAPL, TSLA)
- Case-insensitive
- Handles typos and variations

Ask me anything about Microsoft, Tesla, or Apple! 💼
        """

def main():
    """Main chatbot interface"""
    
    print("=" * 80)
    print("🤖 GFC FINANCIAL CHATBOT - NLP-Powered Version")
    print("=" * 80)
    print("\n✨ Enhanced with Natural Language Processing!")
    print("\nI understand natural language queries about Microsoft, Tesla, and Apple.")
    print("Try asking in your own words - I can handle variations!")
    print("\nDeveloped by: Naitik | BCG GenAI Consulting Team")
    print("Client: Global Finance Corp (GFC)")
    print("\n" + "-" * 80)
    print("\n💡 EXAMPLE QUERIES:")
    print("- 'What was Microsoft's revenue in 2024?'")
    print("- 'MSFT profit margin'")
    print("- 'Compare cash flow'")
    print("- 'Show me Apple revenue trend'")
    print("- 'Which company has best ROE?'")
    print("\nType 'help' for more examples or 'exit' to quit")
    print("-" * 80)
    
    # Initialize NLP chatbot
    chatbot = NLPFinancialChatbot()
    
    # Main loop
    while True:
        print("\n💬 Your Query: ", end="")
        user_input = input()
        
        # Exit condition
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\n" + "=" * 80)
            print("Thank you for using GFC Financial Chatbot!")
            print("NLP-powered analysis by BCG GenAI Consulting Team")
            print("=" * 80)
            break
        
        # Help condition
        if user_input.lower() in ['help', '?']:
            response = chatbot.provide_help()
        else:
            # Process query with NLP
            response = chatbot.process_query(user_input)
        
        # Display response
        print("\n🤖 Chatbot Response:")
        print(response)
        print("-" * 80)

if __name__ == "__main__":
    main()