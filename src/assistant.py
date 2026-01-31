import argparse
from pathlib import Path


def load_prompt() -> str:
    """Load the base prompt template."""
    return Path("prompts/sql_prompt.txt").read_text()


def generate_sql(question: str) -> str:
    """
    Stub generator.
    In future iterations, this will call an LLM.
    For now, it returns a safe, readable SQL template.
    """
    return f"""
SQL:
-- Example template for question:
-- "{question}"

SELECT
  DATE_TRUNC('week', order_date) AS week,
  SUM(amount) / COUNT(DISTINCT order_id) AS aov
FROM orders
GROUP BY 1
ORDER BY 1;

Explanation:
- Assumes an orders table with columns: order_id, order_date, amount
- Aggregates data weekly
- AOV defined as total revenue divided by unique orders
- Query is a template and should be reviewed before execution
"""


def main():
    parser = argparse.ArgumentParser(description="GenAI Analytics Assistant")
    parser.add_argument("question", type=str, help="Business question")
    args = parser.parse_args()

    prompt = load_prompt()
    output = generate_sql(args.question)

    print(prompt)
    print(output)


if __name__ == "__main__":
    main()
