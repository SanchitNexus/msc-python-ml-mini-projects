## Book Recommendation Using Tags (Open Library API)

### Problem Statement
Recommend similar books based on text descriptions/subject tags, without user ratings.

### Dataset
**Free API #3:** [Open Library Subjects API](https://openlibrary.org/dev/docs/api/subjects), no key, obtains fiction titles/subjects. Fallback `data/books.csv` contains 15 **hand-curated teaching examples** and works offline. Live catalog contents may change.

### Approach
TF-IDF vectorize each book's subjects; calculate pairwise cosine similarity and show top five neighbors excluding the query itself.

### Result
Verified offline run: for “The Time Machine”, science-fiction books rank among the positively similar items.

### Key Insight
Content similarity can surface books with shared themes without reader histories, but it also creates a cold-start weakness for books with few or vague subject tags.

### How to Run
`pip install -r requirements.txt`; run `python main.py`, `python main.py --offline`, or `python main.py --offline --title "Dracula"`.
