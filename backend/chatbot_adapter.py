import sys
import os

# Add parent directory to path to import nlp_chatbot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nlp_chatbot import NLPFinancialChatbot

class ChatbotJSONAdapter(NLPFinancialChatbot):
    """
    Adapter to return JSON responses for the UI instead of string printouts.
    """
    def __init__(self):
        super().__init__()

    def process_query_json(self, query):
        """
        Process query and return JSON structure
        """
        # Detect intent and entities
        intent = self.detect_intent(query)
        company = self.extract_company(query)
        year = self.extract_year(query)
        metric = self.extract_metric(query)

        response_data = {
            "text": "",
            "visualization": None
        }

        # Logic similar to process_query but returning data
        if intent == 'compare' or intent == 'ranking':
            response_data = self._handle_compare_json(metric, year)
        elif intent == 'trend':
            response_data = self._handle_trend_json(company, metric)
        elif intent == 'get_metric':
            if company and metric:
                response_data = self._handle_get_metric_json(company, year, metric)
            else:
                 response_data["text"] = "I couldn't understand the company or metric. Please try again."
        else:
            response_data["text"] = self.provide_help()

        if not response_data["text"] and not response_data["visualization"]:
             response_data["text"] = "I'm not sure I understood. Could you rephrase?"

        return response_data

    def _handle_get_metric_json(self, company, year, metric):
        value = self.get_metric_value(company, year, metric)
        if value is None:
             return {"text": f"Sorry, I don't have {metric} data for {company} in {year}.", "visualization": None}

        formatted_value = self.format_currency(value) if metric in ['revenue', 'net_income', 'cash_flow', 'assets'] else self.format_percentage(value)
        
        text = f"{company}'s {metric.replace('_', ' ').title()} in {year} was {formatted_value}."
        
        # Single bar for visualization might be too simple, but let's provide it
        viz = {
            "type": "bar",
            "title": f"{company} {metric.replace('_', ' ').title()} ({year})",
            "data": [
                {"name": company, "value": value}
            ]
        }
        
        return {"text": text, "visualization": viz}

    def _handle_compare_json(self, metric, year):
        if not metric:
             return {"text": "Please specify a metric to compare.", "visualization": None}

        data = []
        for company in ['Microsoft', 'Tesla', 'Apple']:
            val = self.get_metric_value(company, year, metric)
            if val is not None:
                data.append({"name": company, "value": val})
        
        # Sort for better viz
        data.sort(key=lambda x: x['value'], reverse=True)
        
        text = f"Comparing {metric.replace('_', ' ')} for {year}: " + ", ".join([f"{d['name']}: {d['value']}" for d in data])
        
        viz = {
            "type": "bar",
            "title": f"{metric.replace('_', ' ').title()} Comparison ({year})",
            "data": data,
            "yLabel": metric.replace('_', ' ').title()
        }
        return {"text": text, "visualization": viz}

    def _handle_trend_json(self, company, metric):
        if not company or not metric:
             return {"text": "For trends, I need both a company and a metric.", "visualization": None}

        data = []
        years = ['2022', '2023', '2024']
        for y in years:
            val = self.get_metric_value(company, y, metric)
            if val is not None:
                data.append({"name": y, "value": val})
        
        start_val = self.get_metric_value(company, '2022', metric)
        end_val = self.get_metric_value(company, '2024', metric)
        change_text = ""
        if start_val and end_val:
            change_pct = ((end_val - start_val) / start_val) * 100
            direction = "growth" if change_pct > 0 else "decline"
            change_text = f" That's a {abs(change_pct):.1f}% {direction} since 2022."

        text = f"Here is the trend for {company}'s {metric.replace('_', ' ')}.{change_text}"
        
        viz = {
            "type": "line",
            "title": f"{company} {metric.replace('_', ' ').title()} Trend",
            "data": data,
            "yLabel": metric.replace('_', ' ').title()
        }
        return {"text": text, "visualization": viz}
