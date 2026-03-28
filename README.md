# Game Community Dynamics & Launch Performance Analysis

## Overview
This repository presents a cleaned showcase of my individual contribution to a larger team project on Reddit community signals and game launch performance.

The broader project explored three research questions related to network structure, emotional engagement, and launch outcomes in game communities. My primary focus was the final research question (RQ3), which examines how pre-launch and post-launch community dynamics relate to game launch performance, measured by peak concurrent users (CCU).

This repository includes my supporting analysis from earlier stages of the project (Part A), but the main focus is on the RQ3 analysis developed in Part B.

---

## Research Context
The larger team project explored three research questions:

- **RQ1:** Network and community structure in game subreddits  
- **RQ2:** Emotional features and comment engagement across genres  
- **RQ3:** How pre-launch and post-launch community dynamics (sentiment, emotion, comment volume) relate to launch performance (peak CCU), and whether this relationship differs across genres  

This repository focuses primarily on **RQ3**, which was my main analytical contribution.

---

## My Contribution
This repository highlights my individual work from a larger group project.

I was responsible for the final research question (RQ3), including:

- Cleaning and preparing SteamDB player-count data
- Building analysis workflows for pre-launch and post-launch comparison
- Merging launch-performance metrics with Reddit-based sentiment, emotion, and discussion features
- Creating visualizations to compare community dynamics and launch performance
- Analyzing genre-level differences between Shooting and Simulation games

In addition, I also developed the Part A notebook included here as supporting analysis for the broader project workflow.

---

## Research Question
**RQ3: Community Dynamics → Concurrent Users (CCU)**

How do pre-launch and post-launch community dynamics — including sentiment, emotion, and comment volume — relate to a game’s launch performance (peak CCU), and does this relationship differ across genres?

---

## Methods

### Data Preparation
- Cleaned SteamDB player-count data and standardized date/time columns
- Prepared launch-window data for downstream analysis
- Exported cleaned game-level files for launch-performance comparison

### Feature Integration
- Combined Reddit discussion features with game launch-performance metrics
- Structured separate pre-launch and post-launch comparison windows
- Built game-level summary variables for analysis

### Analysis
- Compared pre-launch and post-launch community dynamics
- Examined how sentiment, emotion, and discussion volume related to peak CCU
- Evaluated whether predictive relationships differed across genres
- Used regression-based comparison and visualization to identify genre-specific patterns

---

## Key Insights
- Discussion volume appeared to be more strongly associated with launch performance than sentiment alone  
- The relationship between community activity and CCU differed across genres  
- Simulation games showed a stronger volume–CCU relationship than Shooting games  
- Pre-launch and post-launch social signals were not equally informative across all game types  

---

## Repository Structure
- `steamdb_cleaning_code.py` – SteamDB data cleaning and launch-window preparation
- `Part_A.ipynb` – supporting analysis notebook from earlier stages of the broader project
- `PART_B.ipynb` – main notebook for RQ3 analysis, including community-dynamics and CCU comparison

---

## Data
Large raw datasets are not included in this repository due to size constraints.

This repository focuses on the analysis workflow, cleaned processing logic, and project outputs rather than storing full raw data files.

---

## Tech Stack
**Tech:** Python, pandas, Sentiment Analysis, Data Visualization, Regression Analysis, Behavioral Data Analysis

---

## Notes
- This is a cleaned showcase version of my individual contribution to a larger team project
- While the broader project included multiple research questions, this repository is centered on my work for **RQ3**
- Part A is included as supporting analysis that I also developed
- Other team members’ work is not included unless necessary for project context
