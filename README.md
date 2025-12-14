# 💼 BCG GenAI Consulting Project

**Financial Analysis & AI-Powered Chatbot for Global Finance Corp (GFC)**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📊 Project Overview

This project was developed as part of the **BCG GenAI Consulting Program** for **Global Finance Corp (GFC)**, a leading global financial institution. The goal was to revolutionize financial analysis through AI-powered tools.

**Client Challenge:** GFC needed faster, more efficient ways to analyze corporate financial performance from 10-K and 10-Q reports.

**Solution Delivered:** 
1. Comprehensive financial data extraction and analysis
2. AI-powered chatbot for interactive financial insights

---

## 🎯 Key Features

### **Task 1: Financial Data Analysis**
- ✅ Extracted data from **3 Fortune 500 companies** (Microsoft, Tesla, Apple)
- ✅ Analyzed **3 fiscal years** (2022-2024)
- ✅ Calculated **10+ financial metrics** (Profit Margin, ROA, ROE, etc.)
- ✅ Created professional visualizations
- ✅ Generated actionable insights

### **Task 2: AI-Powered Chatbot**
- ✅ Rule-based chatbot with **5 predefined queries**
- ✅ Instant financial insights (< 0.1s response time)
- ✅ **100% accuracy** on all queries
- ✅ User-friendly command-line interface
- ✅ Comprehensive error handling

---

## 📁 Project Structure

```
BCG_Project/
├── README.md
├── Task1_Financial_Analysis/
│   ├── financial_data.csv                    # Raw financial data
│   ├── BCG_Financial_Analysis.ipynb          # Jupyter analysis
│   ├── financial_analysis_dashboard.png      # Visualizations
│   └── financial_data_processed.csv          # Processed data
│
└── Task2_Financial_Chatbot/
    ├── simple_chatbot.py                     # Main chatbot script
    ├── documentation.txt                     # Technical docs
    ├── README.txt                            # User guide
    └── test_results.txt                      # Testing log
```

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8 or higher
- pip package manager

### **Installation**

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/bcg-genai-project.git
cd bcg-genai-project
```

2. **Install dependencies:**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

3. **Run Task 1 Analysis:**
```bash
jupyter notebook Task1_Financial_Analysis/BCG_Financial_Analysis.ipynb
```

4. **Run Task 2 Chatbot:**
```bash
cd Task2_Financial_Chatbot
python simple_chatbot.py
```

---

## 💬 Chatbot Usage

The chatbot responds to **5 predefined queries**:

1. `What was Microsoft's revenue in 2024?`
2. `What is Apple's profit margin?`
3. `Which company has the highest cash flow?`
4. `How did Tesla's net income change from 2023 to 2024?`
5. `Compare the ROE of all three companies`

**Example Session:**
```
💬 Your Query: What was Microsoft's revenue in 2024?

🤖 Chatbot Response:
📊 Microsoft's Revenue in 2024:
   $245,122 million
   
💡 Context: This represents a 15.7% increase from 2023...
```

Type `exit` to quit.

---

## 📊 Key Findings

### **Microsoft** 🖥️
- **Revenue Growth:** 23.6% (2022-2024)
- **Profit Margin:** 36.0% (Highest)
- **Cash Flow:** $118B
- **Insight:** Strong growth driven by Azure and AI investments

### **Tesla** 🚗
- **Revenue Growth:** 19.9% (2022-2024)
- **Net Income Decline:** -52.7% (2023-2024)
- **Profit Margin:** 7.3%
- **Insight:** Pricing pressure impacting profitability

### **Apple** 🍎
- **Revenue:** Stable ~$390B
- **Profit Margin:** 24.0%
- **ROE:** 164.6% (Best)
- **Insight:** Mature dominance with exceptional profitability

---

## 🛠️ Technologies Used

### **Data Analysis & Visualization**
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

### **Chatbot Development**
- Pure Python (no external dependencies)
- Rule-based if-else logic
- Command-line interface

### **Data Sources**
- SEC EDGAR Database
- Official 10-K filings (2022-2024)

---

## 📈 Results & Impact

### **Efficiency Gains**
- **Manual Analysis:** Hours to days
- **Chatbot:** < 0.1 seconds
- **Time Savings:** 99%+

### **Accuracy**
- **Data Validation:** 100%
- **Test Success Rate:** 100% (12/12 tests passed)
- **Response Accuracy:** 100%

### **Business Value**
- Faster decision-making for GFC clients
- Reduced analysis costs through automation
- Improved client experience with instant insights
- Scalable foundation for future enhancements

---

## 🧪 Testing

Comprehensive testing performed with **12 test cases**:

| Category | Tests | Passed | Pass Rate |
|----------|-------|--------|-----------|
| Valid Queries | 5 | 5 | 100% |
| Invalid Queries | 3 | 3 | 100% |
| Edge Cases | 4 | 4 | 100% |
| **TOTAL** | **12** | **12** | **100%** |

See `Task2_Financial_Chatbot/test_results.txt` for detailed results.

---

## 📚 Documentation

- **Task 1:** See Jupyter Notebook for detailed analysis methodology
- **Task 2:** See `documentation.txt` for chatbot architecture
- **User Guide:** See `README.txt` in Task2 folder
- **Testing:** See `test_results.txt` for validation

---

## 🎓 Skills Demonstrated

### **Technical Skills**
- Python programming
- Data extraction and cleaning
- Financial analysis
- Statistical calculations
- Data visualization
- Chatbot development
- Testing and QA

### **Business Skills**
- Financial statement analysis
- Comparative analysis
- Trend identification
- Insight generation
- Client-focused solutions

### **Professional Skills**
- Requirements analysis
- Solution design
- Documentation
- Quality assurance
- Project delivery

---

## 🚀 Future Enhancements

### **Phase 2 Roadmap:**
- [ ] Natural Language Processing (NLP) integration
- [ ] Machine learning capabilities
- [ ] Real-time data integration
- [ ] Web-based graphical interface
- [ ] Support for 100+ companies
- [ ] 10+ years of historical data
- [ ] Advanced visualizations
- [ ] API integration

---

## 👥 Team

**Project Lead:** Naitik (Junior Data Scientist)  
**Team Lead:** Aisha (Senior Data Scientist)  
**Organization:** BCG GenAI Consulting Team  
**Client:** Global Finance Corp (GFC)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Boston Consulting Group (BCG)** for the GenAI Consulting Program
- **Global Finance Corp (GFC)** for the project opportunity
- **Aisha** for mentorship and guidance
- **SEC EDGAR** for financial data access

---

## 📧 Contact

**Naitik**  
 

- GitHub: https://github.com/nAItiklearn
- LinkedIn: www.linkedin.com/in/naitik181818
- Email: naiitik1526@gmail.com

---

## ⭐ Star This Repository

If you found this project interesting or useful, please consider giving it a star

---

**Made with 💼 by Naitik 