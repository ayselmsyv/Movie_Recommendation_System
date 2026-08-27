# Recommendation Engine Design

## Problem

Given a movie title, recommend movies with similar content.

## Input

A movie title entered by the user.

## Output

Up to 10 recommended movie titles with similarity scores.

## Features

- genres
- overview
- keywords
- cast
- director

## Pipeline

CSV
→ validation
→ cleaning
→ feature combination
→ TF-IDF vectorization
→ cosine similarity
→ ranking
→ recommendations

## Initial Algorithm

Content-based filtering using TF-IDF and cosine similarity.

## Limitations

- Does not use user ratings
- Can over-recommend movies with similar metadata
- New or poorly described movies may receive weak recommendations