## SMS Spam vs Ham Classification

### Problem Statement
Determine whether an SMS-like message is an unsolicited promotion (spam) or ordinary communication (ham).

### Dataset
`data/messages.csv` is a small **handwritten synthetic educational dataset** (70 messages, balanced labels). No private conversations are used; this is not a realistic spam benchmark.

### Approach
Token count vectors (`CountVectorizer`), multinomial Naive Bayes, stratified holdout evaluation and classification report.

### Result
Verified offline test: accuracy **0.952** (20/21 held-out synthetic messages).

### Key Insight
This small sample repeats promotional phrases such as 'claim' and 'free', making classification artificially easy; a real spam filter must handle deliberate spelling changes and less obvious spam.

### How to Run
`pip install -r requirements.txt` then `python main.py`. Works offline.
