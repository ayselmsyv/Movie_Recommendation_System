# Edge Cases

## Missing genres

Replace missing genres with an empty string.

## Multiple genres

Split genres using `|`, trim whitespace, normalize case, and combine them.

## Uppercase and lowercase

Normalize text before comparison.

## Unknown movie title

Return a clear movie-not-found error.

## Duplicate titles

Use movie ID or release year to disambiguate them.

## Selected movie in results

Remove the input movie from the recommendation list.

## Fewer than ten movies

Return all available recommendations without failing.

## Empty metadata

Exclude or flag movies whose combined feature text is empty.