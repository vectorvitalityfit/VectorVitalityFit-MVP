# VectorVitalityFit MVP

## Overview
An AI-powered platform combining muscle growth modelling, BFR training coaching, and workout plan generation using Azure AI services and Replit AI.

## Project Structure
- `azure_ml/`: Muscle growth model and Azure ML deployment scripts.
- `azure_bot/`: Azure Bot Service chatbot and LUIS intents.
- `data_factory/`: Azure Data Factory pipeline JSON for CSV ingestion
- `replit_ai/`: Script to generate workout plans with Replit AI.

## Setup Instructions

1. Set up Azure resources: Azure ML workspce, Azure Bot Service, LUIS, Data Factory, Synapse Analytics.
2. Deploy the muscle growth model using `azure_ml/deploy_ml.py`.
3. Publish the LUIS app using `azure_bot/luis_intents.json`.
4. Deploy chatbot with `azure_bot/bot.py`
5. Set up the Data Factory pipeline with `data_factory/pipeline.json`.
6. Use `replit_ai/workout_plan_generator.py` to generate workout plans via Replit AI API.

## Contact
Sheraz Arshad – sherazarshad27@gmail.com