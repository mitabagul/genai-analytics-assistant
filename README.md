# GenAI Analytics Assistant

## Problem Statement
Data teams often translate business questions into SQL repeatedly. This project provides a lightweight GenAI assistant that converts natural-language questions into SQL templates with clear assumptions and guardrails.

## What It Does
- Accepts a business question (e.g., “What is AOV by week?”)
- Produces a SQL template aligned to common analytics schemas
- Explains assumptions and limitations

## What It Does NOT Do
- Execute SQL
- Access production data
- Make irreversible decisions

## Repository Structure
- `src/` — core assistant logic
- `prompts/` — prompt templates
- `examples/` — example inputs and outputs

## Usage
Instructions will be added as the assistant evolves.

## Trade-offs & Assumptions
- Prioritizes clarity and safety over autonomy
- Outputs templates, not executed queries
