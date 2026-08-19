# Knowledge Base AI Chatbot

## Overview
This project is an AI-powered knowledge base chatbot designed to answer work-related questions. It uses a combination of vector embeddings and an online Large Language Model (LLM) to intelligently route user queries to the appropriate predefined "skills" without exposing sensitive information to external APIs.

## Architecture & Workflow

To minimize token usage and maximize data privacy, the system processes queries in the following sequence:

1. **Vector Pre-filtering:** User prompts are converted to vectors. The system compares this query vector against preprocessed vectors of all skill descriptions. Only skills with a cosine similarity above a set threshold are kept.
2. **LLM Decision (Tool 1):** The LLM reads the filtered list of `description.md` files. Based on this metadata, the LLM decides which skill best answers the user's question.
3. **Local Content Delivery (Tool 2):** Once the LLM returns the chosen skill name, the system locally loads the corresponding `skill.md` and displays the rendered Markdown content to the user. 
*Note: The contents of `skill.md` are **never** passed to the LLM to strictly protect sensitive information.*

## Directory Structure

The knowledge base is organized around a core `/skills` directory. Each individual skill has its own subdirectory containing exactly two files:

```text
/skills
  ├── /skill_name_1
  │     ├── description.md
  │     └── skill.md
  ├── /skill_name_2
  │     ├── description.md
  │     └── skill.md
  └── ...