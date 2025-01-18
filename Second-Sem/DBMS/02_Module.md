# (ER) Entity Relationship Model
## Entity
An **entity** is any object that exists in the database and has attributes. It can be a **person, place, object, or event** that we need to store information about.
##### Examples:
- **Elden Ring**: Entities would include **Player**, **Enemy**, **Weapon**, and **Boss**.
- **The Witcher 3**: Entities would be **Geralt (Player)**, **Triss (NPC)**, **Sword (Item)**, and **Kaer Morhen (Location)**.

Each of these **entities** has its own properties, which we call **attributes**.
## Attributes
Attributes define **characteristics** of an entity. Each entity has multiple attributes, and each attribute holds specific data.
##### Examples:
- **Player (Entity)** → Attributes: `Name`, `Health`, `Level`, `Experience Points`, `Inventory Capacity`.
##### Types of Attributes:
1. **Simple Attributes** → Cannot be divided further (e.g., `Character Name`, `Weapon Type`).
2. **Composite Attributes** → Can be broken down (e.g., `Full Name` can be split into `First Name` and `Last Name`).
3. **Derived Attributes** → Values derived from other attributes (e.g., `Character Age` is derived from `Date of Birth`).
4. **Multivalued Attributes** → Can have multiple values (e.g., a **Player** can have multiple **Weapons** in their inventory).
## Relationships
A relationship defines how **two or more entities are connected**, like **interactions between objects in a game**, like a **player using a weapon, an NPC giving a quest, or an enemy attacking a player**.
#### Types of Relationships:

1. **One-to-One (1:1) Relationship**
- Each entity in **A** is related to only one entity in **B**.
- **Example:** In **Cyberpunk 2077**, the **Player** (V) has **one main apartment** (unique home location).
- **ER Representation:** `Player (1) ←→ (1) Apartment`.
![One-to-One](./Figures/1-1.png)

1. One-to-Many (1:M) Relationship
-  One entity in **A** is related to many entities in **B**.
- **Example:** In **The Witcher 3**, one **Quest** can have **multiple objectives**.
- **ER Representation:** `Quest (1) ←→ (M) Objectives`.
![onetomany](./Figures/One-to-Many.png)

1. Many-to-Many (M:M) Relationship
- Many entities in **A** are related to many entities in **B**.
- **Example:** In **World of Warcraft**, a **Player** can complete **multiple Quests**, and each **Quest** can be completed by **multiple Players**.
- **ER Representation:** `Player (M) ←→ (M) Quest`.

>[!info]
>**Entities** = Objects in the game (Player, Weapon, NPC, Enemy).
>**Attributes** = Stats and properties (Health, Level, Damage, Name).
>**Relationships** = How entities interact (Player uses Weapon, Player fights Enemy, Player completes Quest).

![ER-Model](./Figures/ER-Model.png)

---

