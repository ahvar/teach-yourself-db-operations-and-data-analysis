## Query Steps to Find Consecutive Numbers

1. **Self-join the table three times**
   - Join `Logs` table with itself to compare consecutive rows
   - Use aliases (l1, l2, l3) to represent three consecutive rows

2. **Match consecutive IDs**
   - Join condition: `l1.id = l2.id - 1 AND l2.id = l3.id - 1`
   - This ensures we're looking at rows with IDs n, n+1, n+2

3. **Match same numbers**
   - Condition: `l1.num = l2.num AND l2.num = l3.num`
   - This ensures the same number appears in all three consecutive rows

4. **Select distinct numbers**
   - `SELECT DISTINCT l1.num AS ConsecutiveNums`
   - Use `DISTINCT` to avoid duplicates if a number appears consecutively more than 3 times

## SQL Solution

```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1
JOIN Logs l3 ON l2.id = l3.id - 1
WHERE l1.num = l2.num AND l2.num = l3.num;
```

## Explanation
- For the sample data, this finds that number `1` appears in rows with IDs 1, 2, and 3 consecutively
- Number `2` only appears twice consecutively (IDs 6, 7), so it doesn't meet the "at least three times" requirement

...existing content...