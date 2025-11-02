# genai-llm-agent-langchain-gemini

A Langchain agent for processing product return request. The aim of this project is to create a transparent langchain agent shoring each api calls happening to LLM- mainly for auditing and cost consideration.

This agent fetches reqired data autonomously in multiple steps and use it to make decision.

## Features
- Transparent auditing showing each api calls happening to LLM
- Built on langchain
- Uses Gemini api which is free to use
- Fully functional agent capable of using tools autonomously in multiple steps to arrive at conclusion

## Quick Start
```bash
git clone https://github.com/akhil-jr/genai-llm-agent-langchain-gemini.git
```
```bash
cd genai-llm-agent-langchain-gemini
```
```bash
pip install -r requirements.txt
```
```bash
cp .env.example .env
#Add your gemini API key in .env file
```
```bash
python -m src.main

```