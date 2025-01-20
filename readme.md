![Demo](/demo.gif)
![Demo2](/demo2.gif)

## Table of Contents:

- [BakeBook API 🍰](#bakebook-api-🍰)
- [BakeBook WebUI 🕸️](#bakebook-webui-🕸️)

# BakeBook API 🍰

Velkom mama mia to **BakeBook**, your ~~totally not~~ one-stop ~~buggy~~ recipe-sharing platform! Whether you're a seasoned chef or a curious beginner, thus API makes it easy to browse, seach, and share your favorite recipes. With seamless integration and an intuitive design, this hellish of an API is your gateway to deliciosness. 😋

## Base URL

The BakeBook API is hosted at: [https://bakebook-xn4v.onrender.com/](https://bakebook-xn4v.onrender.com/)

Live demo on: [https://sayhan1610.github.io/bakebook/](https://sayhan1610.github.io/bakebook/)

## Endpoints

Below is a detailed guide to all the endpoints BakeBook offers:

---

### 1. **Get a Specific Recipe**

`GET /recipes/{recipe_name}`

Retrieve a recipe by its name. Perfect for when you already know what you're craving!

#### Request Parameters

- **`recipe_name`** _(string)_: The name of the recipe you want (case-insensitive).

#### Example Request

```bash
GET https://bakebook-xn4v.onrender.com/recipes/pancake
```

#### Example Response

```json
{
  "name": "Pancake",
  "description": "Fluffy and delicious pancakes.",
  "ingredients": [
    "Eggs (2pcs)",
    "Milk (20ml / tsp)",
    "All purpose flour (30g / 3.3 tbsp)",
    "Sugar (25g / 2 tbsp)",
    "Hand Crushed Cardamom Seeds (from 3-4 of them)"
  ],
  "procedure": "Start by separating 2 large eggs into yolks and whites. Mix the yolks with 20 ml (4 teaspoons) of milk until smooth. Sift 30 grams (3.3 tablespoons) of all-purpose or low-gluten flour into the yolk mixture, then mix well. Sift crushed cardamom seeds to the mixture, and stir until the batter is smooth. Next, whip the egg whites with an electric whisk on medium-high speed. Gradually add 25 grams (2 tablespoons) of sugar in three portions: first when large bubbles appear, then when smaller bubbles form, and finally when the texture becomes more visible. Continue beating on medium-low speed until stiff peaks form. Fold one-third of the whipped egg whites into the yolk batter and mix gently. Pour this mixture back into the remaining meringue and combine carefully to maintain the fluffy texture. Transfer the batter into a piping bag. Preheat a non-stick pan over low heat, add a drop of cooking oil, and spread it evenly using kitchen paper. Pipe the batter into the pan, creating three pancakes. Add 2 teaspoons of water to the pan, cover it, and cook on low heat for about 5 minutes. Flip the pancakes carefully, add 1 teaspoon of water, cover, and cook for another 5 minutes. Once done, remove the pancakes from the pan, and serve with butter and syrup for a deliciously fluffy treat.",
  "hardness": 3
}
```

#### Errors

- **404 Not Found**: Recipe not found.
  ```json
  {
    "detail": "Recipe for {recipe_name} not found."
  }
  ```

---

### 2. **Search Recipes by Keyword**

`GET /search`

Find recipes that match a keyword in their name or description. Great for exploring new ideas!

#### Query Parameters

- **`keyword`** _(string)_: The search term to filter recipes.

#### Example Request

```bash
GET https://bakebook-xn4v.onrender.com/search?keyword=cookie
```

#### Example Response

```json
{
  "chocolate-chip-cookie": {
    "name": "Chocolate Chip Cookie",
    "description": "Classic cookies loaded with chocolate chips.",
    "ingredients": [
      "Unsalted butter (200g/0.875 cup)",
      "Brown sugar (80g/0.5 cup)",
      "Granulated sugar (90g/0.5 cup)",
      "Eggs (2)",
      "All-purpose flour (200g/1.6 cups)",
      "Cake flour (120g/1 cup)",
      "Cornstarch (6g/2 teaspoons)",
      "Baking powder (4g/1 teaspoon)",
      "Baking soda (3g/0.5 teaspoon)",
      "Chopped walnuts (200g/2 cups)",
      "Chocolate (320g/2 cups)"
    ],
    "procedure": "To make these simple and delicious cookies, begin by creaming together 200 grams (7/8 cup) of unsalted butter, 80 grams (1/2 cup) of brown sugar, and 90 grams (1/2 cup) of granulated sugar in a mixing bowl. Stir the mixture first, then whip it with electric beaters until it becomes slightly whitened. Beat in 2 eggs and whisk the mixture until well combined, using a spatula to clean the sides of the bowl as needed. In a separate bowl, combine the dry ingredients: 200 grams (1.6 cups) of all-purpose or wheat flour, 120 grams (1 cup) of cake flour, 6 grams (2 teaspoons) of cornstarch, 4 grams (1 teaspoon) of baking powder, and 3 grams (1/2 teaspoon) of baking soda. Mix these thoroughly and then gradually add them to the wet ingredients. Stir in 200 grams (2 cups) of chopped walnuts and 320 grams (2 cups) of chocolate, mixing well to ensure even distribution. Take about 160 grams of the dough, knead it, and form it into balls. This recipe makes approximately 8 dough balls. Place the balls into a container, cover them with plastic wrap, and refrigerate for at least 2 hours or overnight for best results. When ready to bake, place the dough balls on a baking sheet and bake in a preheated oven at 180°C (360°F) for 20 minutes. Let the cookies cool before serving. Enjoy!!",
    "hardness": 5
  }
}
```

#### Errors

- **404 Not Found**: No recipes match the search criteria.
  ```json
  {
    "detail": "No recipes match your search criteria."
  }
  ```

---

### 3. **List All Available Recipes**

`GET /recipes`

Get a list of all the recipe names currently in BakeBook. Handy for browsing the menu!

#### Example Request

```bash
GET https://bakebook-xn4v.onrender.com/recipes
```

#### Example Response

```json
{
  "endpoints": [
    "pancake",
    "chocolate-chip-cookie",
    "cheese-bread",
    "cloud-bread",
    "cranberry-bread",
    "milk-bread"
  ]
}
```

---

### 4. **Submit a New Recipe**

`POST /submit`

Got a culinary masterpiece to share? Submit it to BakeBook, and we’ll review it. Submissions are sent to my Telegram for review and will appear in the system after approval.

#### Request Body

| Field         | Type     | Description                                 | Constraints          |
| ------------- | -------- | ------------------------------------------- | -------------------- |
| `name`        | `string` | Name of the recipe                          | Required             |
| `description` | `string` | Brief description of the recipe             | Required             |
| `ingredients` | `list`   | List of ingredients (with amounts)          | Required             |
| `procedure`   | `string` | Step-by-step procedure to make the recipe   | Required             |
| `hardness`    | `int`    | Difficulty level of the recipe (1-10 scale) | Required; 1 ≤ x ≤ 10 |

#### Example Request

```json
POST https://bakebook-xn4v.onrender.com/submit
Content-Type: application/json

{
  "name": "Lemon Tart",
  "description": "A zesty, refreshing dessert for lemon lovers.",
  "ingredients": ["2 cups flour", "1/2 cup sugar", "1/4 cup butter", "4 lemons"],
  "procedure": "1. Prepare the crust. 2. Make the filling. 3. Bake at 375°F.",
  "hardness": 6
}
```

#### Example Response

```json
{
  "message": "Submission received! It'll be reviewed shortly."
}
```

#### Errors

- **500 Internal Server Error**: Failed to send the recipe to Telegram.

---

### 5. **Ping the API**

`GET /`

Check if the BakeBook API is live and get basic usage instructions.

#### Example Response

```json
{
  "message": "message":"Welcome to BakeBook! Use /recipes, /search to search for one to see available recipes, or /submit to submit a new recipe. Alternatively, visit https://sayhan1610.github.io/BakeBook/ to use the GUI."
}
```

---

## Features & Extras

- **Cross-Origin Requests**: Supports requests from any origin, making it easy to integrate with your frontend.
- **Telegram Integration**: Recipe submissions are instantly sent to Telegram for quick reviews.
- **Ease of Use**: Clear and detailed error messages for effortless debugging.

## Requirements

To run the API locally:

- **Python 3.9+**
- `fastapi`
- `pydantic`
- `uvicorn`
- `requests`

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

# BakeBook WebUI 🕸️

### **Frontend (Web Files Overview)**

The site is hosted on [GitHub Pages](https://sayhan1610.github.io/bakebook/)

**HTML:**

- **Buttons:** There are two main buttons:
  1. **Load Recipes** – Displays a list of all available recipes. (Still a bit buggy)
  2. **Submit New Recipe** – Allows users to submit their own recipes to the system.
- **Containers:**
  - **Recipes** – Where the list of available recipes appears once loaded.
  - **Recipe Details** – A detailed view of each recipe when clicked from the list.
  - **Submit Form** – A form to submit new recipes, including fields for recipe name, description, ingredients, procedure, and hardness.

**CSS:**

- The **background** is a warm color, reminiscent of baked goods, while **buttons** and containers use soft colors that match the cozy kitchen vibe. ~~(Idk mate orange screams kitchen to me)~~
- **Form Design:** The input fields and buttons are designed to be simple and approachable, guiding the user to fill out the form and submit their recipe easily. ~~(I promise my 6th grade english teacher didn't write this)~~

---

### **JavaScript (Functionality)**

- **Falling Emoji Animation:**
  - Emojis randomly drops from the top of the screen using CSS animations. ~~It's and looks cute, so why not?~~
- **Load Recipes Button:** ~~Do I really need to tell you what it does?~~

  - When clicked, it makes an API call to the backend to fetch the available recipe names.
  - The list of recipe names is displayed in a clean, clickable format. Each recipe name, when clicked, fetches the full details from the backend (name, description, ingredients, procedure, and hardness) and displays them.

- **Submit Recipe Button:** ~~Again, for real dude?~~

  - Clicking this button reveals the form to submit a new recipe.
  - Once the form is filled, it sends a POST request to the API with the recipe data.

- **Form Submission:** ~~Yes I do receive them~~
  - When the form is submitted, the recipe is sent to the backend API using a `POST` request.

---

### **How It All Connects** ~~In case you decided to read this far~~

1. **User Interaction:**

   - When users land on the page, they can either **load recipes** or **submit a new recipe**.
   - **Loading Recipes:** On click, the frontend calls the backend `/recipes` endpoint, loads the list of recipe names, and displays them.
   - **Recipe Details:** On clicking any recipe name, the frontend calls the `/recipes/{recipe_name}` endpoint and displays the full recipe details.
   - **Submitting a Recipe:** Clicking "Submit New Recipe" reveals the form where users can input their recipe. Once submitted, the frontend sends the data to the `/submit` endpoint, and a confirmation message is shown.

2. **API Interactions:**
   - The **API** is hosted at `https://bakebook-xn4v.onrender.com/`. It connects with the frontend to deliver the necessary data (recipe names, details) and to handle submissions. The API also interacts with **Telegram** to notify admins _(which is only me btw)_ about new submissions.
