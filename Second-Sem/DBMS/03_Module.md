# SQL Basics
**Structured Query Language**
SQL is divided into **four categories** based on the type of operations they perform:

1. DDL (Data Definition Language) – Defines the Structure
 Used to **create, modify, or delete database structures** (tables, schemas, indexes).
```Example
 CREATE → Creates a new table or database.
 ALTER → Modifies an existing table.
 DROP → Deletes a table or database.
```

2. DML (Data Manipulation Language) – Works with Data
Used to **insert, update, delete, and retrieve data** in a table.
```Example
 INSERT → Adds new records.
 UPDATE → Modifies existing records.
 DELETE → Removes records.
 SELECT → Retrieves data.
```

3. DCL (Data Control Language) – Manages Access
Used to **control access permissions** in a database.
```Example
GRANT → Gives access to users.
REVOKE → Removes access from users.
```

4. TCL (Transaction Control Language) – Ensures Data Integrity
 Used to **manage transactions** (grouping multiple queries as one unit).
```Example
COMMIT → Saves all changes permanently.
ROLLBACK → Undoes changes made within a transaction.
SAVEPOINT → Creates checkpoints to rollback to a specific point if needed.
```
---
# Advanced SQL Queries
#### 1. Joins – Combining Data from Multiple Tables
Used to retrieve data by linking two or more tables based on a common column.

Types of Joins:
- **INNER JOIN** → Returns only matching rows from both tables.
- **LEFT JOIN** → Returns all rows from the left table and matching rows from the right table.
- **RIGHT JOIN** → Returns all rows from the right table and matching rows from the left table.
- **FULL JOIN** → Returns all rows when there is a match in either table.

```sql
SELECT players.name, guilds.guild_name 
FROM players 
INNER JOIN guilds ON players.guild_id = guilds.guild_id;
```
#### 2. Subqueries – Query Inside a Query
In **Dark Souls**, suppose we want to **find players whose HP is above the average HP of all players**. We need to calculate the **average HP first**, then find players who exceed it.

```SQL
SELECT player_name FROM players 
WHERE hp > (SELECT AVG(hp) FROM players);
```
- The **inner query** calculates the **average HP**.
- The **outer query** finds **players whose HP is above the average**.
#### 3. Views – Predefined Queries for Quick Access
Think of **a game leaderboard** in an **FPS like Call of Duty**. Instead of calculating the **top 10 players’ scores every time**, we **create a view** that stores the leaderboard dynamically.

```SQL
CREATE VIEW top_players AS 
SELECT player_name, score FROM players 
ORDER BY score DESC 
LIMIT 10;
```
Now, Inorder to summon the Leaderboard 
```SQL
SELECT * FROM top_players;
```

This **optimizes performance and avoids recalculating** the same data repeatedly.
#### 4.Indexing – Speeding Up Searches
In **The Witcher 3**, imagine searching for a **specific monster in the bestiary**. If we don’t have an **index**, the game **scans the entire bestiary** every time. With an **index**, it quickly jumps to the right entry.

```sql
CREATE INDEX idx_monster_name ON monsters(name);
```
This will make the searches like this
```SQL
SELECT * FROM monsters WHERE name = 'Griffin';
```
**much faster** instead of scanning all rows one by one.
Indexes help in **fast lookups, just like searching items in an organized in-game menu**.

---
# Relational Algebra
Relational Algebra is like **game mechanics** that define how data (game elements) are processed.
#### 1. Selection (σ) – Filtering Data

Selecting Players Above Level 50 (Filtering Players)**
- In **World of Warcraft**, if we want to see only **players above level 50**, we apply a **selection operation** to filter out the rest.

**Relational Algebra Notation**
```scss
σ level > 50 (Players)  
```
**SQL Equivalent**
```SQL
SELECT * FROM Players WHERE level > 50;
```

>[!info]
>Selection retrieves only the rows (records) that meet a condition.

#### 2.Projection (π) – Choosing Specific Attributes
Viewing Only Player Names & Levels (Hiding Unnecessary Info)
- In **Elden Ring**, if we only want to see **character names and levels** (ignoring HP, XP, etc.), we use **projection** to select only **specific columns**.
**Relational Algebra Notation**
```scss
π name, level (Players)  
```
**SQL Equivalent**
```sql
SELECT name, level FROM Players;
```

>[!info]
>**Projection** retrieves only **specific columns (attributes), removing unnecessary details**.

#### 3.Cartesian Product (×) – Combining Every Record with Every Other
Generating All Possible Enemy-Item Drops
In **Monster Hunter**, if we **combine all monsters with all possible loot items**, we get a **list of every monster-item combination**, even if it doesn't make sense.

**Relation Algebra Notation**
```scss
Monsters × Items  
```
**SQL Equivalent** 
```sql
SELECT * FROM Monsters, Items;
```

**Cartesian Product** **combines every row from Table A with every row from Table B**, useful in generating possible pairs before filtering.

#### 4. Set Operations (∪, ∩, −) – Combining or Comparing Data
##### (a) Union (∪) – Merging Data from Two Sources
Example:
Combining PC and Console Leaderboards, If **Call of Duty** has separate **PC and Console leaderboards**, but we want a **single leaderboard**, we use **Union**.

**Relation Algebra Notation**
```scss
PC_Players ∪ Console_Players  
```
**SQL Equivalent**
```sql
SELECT player_name FROM PC_Players 
UNION 
SELECT player_name FROM Console_Players;
```
##### #### **(b) Intersection (∩) – Finding Common Data**
Example:
Players Who Are in Both PvP and PvE Rankings
If we want to find **players ranked in both PvP and PvE**, we use **Intersection**.
**Relational Algebra Notation:**
```scss
PvP_Ranked_Players ∩ PvE_Ranked_Players  
```

SQL Equivalent
```sql
SELECT player_name FROM PvP_Ranked_Players 
INTERSECT 
SELECT player_name FROM PvE_Ranked_Players;
```
##### (c) Difference (−) – Finding What’s Missing
Players Who Are in PvP but Not in PvE
If we want to find **players ranked in PvP but NOT in PvE**, we use **Difference**.

**SQL**
```sql
SELECT player_name FROM PvP_Ranked_Players 
EXCEPT 
SELECT player_name FROM PvE_Ranked_Players;
```

| **Operation**           | **Game Example**                          | **Purpose**                          |
|-------------------------|------------------------------------------|--------------------------------------|
| **Selection (σ)**       | Selecting players above level 50        | Filters rows based on conditions    |
| **Projection (π)**      | Viewing only player names and levels    | Chooses specific columns            |
| **Cartesian Product (×)** | Generating all possible enemy-item drops | Combines every row from Table A with Table B |
| **Union (∪)**          | Combining PC and Console leaderboards   | Merges two sets of data             |
| **Intersection (∩)**    | Players in both PvP & PvE rankings      | Finds common records                |
| **Difference (−)**      | Players in PvP but NOT in PvE           | Finds missing records               |

---
# Query Optimization Techniques
Query Optimization is like improving game performance—you want fast load times, smooth FPS, and minimal lag. Similarly, databases need optimized queries to fetch data quickly.
#### 1. Indexing 
Searching for a Quest in an Open-World RPG (The Witcher 3, Skyrim)
- Without an index, searching a quest would mean checking every NPC, every location, every log entry.
- With an index, it’s like having a mini-map marker that quickly points to the right place.

 **SQL Optimization:**
```sql
CREATE INDEX idx_player_name ON Players(name);
```
- Makes `WHERE name = 'Geralt'` **much faster** by jumping directly to the data.

#### **2. Avoiding SELECT *** 
**Loading Only Nearby Objects in an Open World (GTA, Cyberpunk 2077)
- If a game loads the entire map at once, it lags and crashes.
- Instead, it loads only what’s around the player for better performance.
- Bad Query (Loads Everything! Slow & Expensive)

**Bad Query (Loads Everything! Slow & Expensive)**
```sql
SELECT * FROM Players;
```
**Optimized Query (Loads Only Needed Columns)**
```sql
SELECT name, level FROM Players;
```
**Faster, less memory usage, better performance!**

#### **3. Use JOINS Efficiently – Optimize Player Matching in Multiplayer**
Fast Matchmaking in Online Games (Valorant, Call of Duty)
- Imagine matchmaking where the system **checks every player manually**—slow and frustrating.
- Instead, it **pre-matches players based on rank and skill** using optimized **JOINs**
**Bad Query (Inefficient Join, Scans Every Row)**\
```sql
SELECT * FROM Players, Guilds WHERE Players.guild_id = Guilds.guild_id;
```

**Optimized Query (Uses INNER JOIN for Better Performance)**
```sql
SELECT Players.name, Guilds.guild_name 
FROM Players 
INNER JOIN Guilds ON Players.guild_id = Guilds.guild_id;
```
**Faster retrieval, only relevant data!**
#### **4. Query Caching – Reusing Data Like a Game’s Quick-Load Feature**
Fast-Travel in Skyrim or Save States in Emulator Games
- Instead of recalculating everything from scratch, the system **saves recent results** and reuses them.
- **Databases use caching to store frequent queries, avoiding redundant work.**
**SQL Optimization (Enabling Query Cache)**
```sql
SET GLOBAL query_cache_size = 1000000;
```
Reduces load, speeds up response time!
#### **5. Using LIMIT – Don’t Load Unnecessary Data 📦**
Showing Only Top 10 Players in a Leaderboard (Fortnite, Apex Legends)
- If we ask for **ALL players**, it’s **slow and unnecessary**. Instead, we use **LIMIT** to fetch only **what we need**.
**Bad Query (Loads Everything, Even Unneeded Data)**
```sql
SELECT * FROM Leaderboard ORDER BY score DESC;
```
**Optimized Query (Loads Only the Top 10 Players)**
```sql
SELECT name, score FROM Leaderboard 
ORDER BY score DESC 
LIMIT 10;
```
Faster, lighter, and just enough data for display!
#### **6. Use EXPLAIN to Analyze Query Performance 🔍**
Debugging Performance Issues in Game Development**
- Just like developers **profile game performance (FPS, CPU, GPU usage)**, we can **profile SQL queries** using `EXPLAIN`.
```sql
EXPLAIN SELECT name FROM Players WHERE level > 50;
```

| Optimization Technique | Game Example                             | Purpose                        |
|------------------------|------------------------------------------|--------------------------------|
| Indexing               | Mini-map marker in an open world        | Faster search queries          |
| **Avoid SELECT ***     | Load only nearby objects in a game      | Reduce memory usage            |
| Optimize JOINS         | Fast matchmaking in online games       | Speed up data retrieval        |
| Query Caching          | Quick-load feature in games            | Reuse frequent queries         |
| Use LIMIT              | Show only Top 10 in a leaderboard      | Fetch only necessary data      |
| EXPLAIN Query          | Debugging game performance             | Analyze and improve SQL queries|
