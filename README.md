# IMPORTANT
** How to restore python's venv installations from file:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

---

## **Prerequisites**

Before you begin, ensure you have the following installed and set up:

1. **Visual Studio Code (VSCode):**
   - Download and install from [here](https://code.visualstudio.com/).

2. **Git:**
   - Download and install from [here](https://git-scm.com/downloads).
   - Verify installation by opening your terminal (Command Prompt, PowerShell, Terminal, etc.) and running:
     ```
     git --version
     ```

3. **GitHub Account:**
   - If you don’t have one, sign up [here](https://github.com/).

4. **(Optional) GitHub CLI:**
   - For enhanced GitHub interactions, install the [GitHub CLI](https://cli.github.com/).

---

## **Step 1: Create a New Project Folder**

1. **Choose a Location:**
   - Decide where you want to store your project on your computer.

2. **Create the Folder:**
   - **Windows:**
     - Open File Explorer, navigate to your desired parent directory, right-click, select **New > Folder**, and name it (e.g., `my-web-project`).
   - **Mac/Linux:**
     - Open Finder or your file manager, navigate to the desired location, and create a new folder named `my-web-project`.

---

## **Step 2: Open the Project in VSCode**

1. **Launch VSCode:**
   - Open Visual Studio Code.

2. **Open the Folder:**
   - Click on `File` > `Open Folder...` (or `Open` on Mac).
   - Navigate to and select your newly created `my-web-project` folder.
   - Click `Select Folder` (or `Open` on Mac).

---

## **Step 3: Initialize Your Web Project**

1. **Create Essential Files:**
   - In the **Explorer** pane (left sidebar), click the `New File` icon.
   - Create the following files:
     - `index.html` – Your main HTML file.
     - `style.css` – Your CSS stylesheet.
     - `app.js` – Your JavaScript file.

2. **Add Basic Content:**
   - **index.html:**
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>My Web Project</title>
         <link rel="stylesheet" href="style.css">
     </head>
     <body>
         <h1>Hello, World!</h1>
         <script src="app.js"></script>
     </body>
     </html>
     ```
   - **style.css:**
     ```css
     body {
         font-family: Arial, sans-serif;
         text-align: center;
         margin-top: 50px;
     }
     ```
   - **app.js:**
     ```javascript
     console.log("Hello, World!");
     ```

3. **(Optional) Initialize Node.js (If Using Node):**
   - Open the terminal in VSCode by clicking `View` > `Terminal` or pressing `` Ctrl+` ``.
   - Run:
     ```
     npm init -y
     ```
   - This creates a `package.json` file with default settings.

---

## **Step 4: Initialize a Local Git Repository**

1. **Initialize Git:**
   - In the terminal, ensure you’re in your project directory (`my-web-project`).
   - Run:
     ```
     git init
     ```
   - This initializes a new Git repository in your project folder.

2. **Create a `.gitignore` File:**
   - In the **Explorer** pane, create a new file named `.gitignore`.
   - Add the following (adjust as needed):
     ```
     node_modules/
     .env
     dist/
     ```
   - This file tells Git which files or directories to ignore.

---

## **Step 5: Make Your Initial Commit**

1. **Stage Your Files:**
   - In the terminal, run:
     ```
     git add .
     ```
   - This stages all files in your project for the commit.

2. **Commit the Files:**
   - Run:
     ```
     git commit -m "Initial commit"
     ```
   - This creates a commit with your staged files and the message "Initial commit".

---

## **Step 6: Create a New Repository on GitHub**

1. **Log In to GitHub:**
   - Go to [GitHub](https://github.com/) and log in to your account.

2. **Create a New Repository:**
   - Click the `+` icon in the top-right corner and select `New repository`.
   - **Repository Name:** `my-web-project` (or your preferred name).
   - **Description:** (Optional) A short description of your project.
   - **Public/Private:** Choose based on your preference.
   - **Initialize Repository:**
     - **Do NOT** check `Initialize this repository with a README` since you already have a local repository.
   - Click `Create repository`.

---

## **Step 7: Link Your Local Repository to GitHub**

After creating the repository, GitHub provides instructions to push an existing repository. Follow these steps:

1. **Add the Remote Repository:**
   - In your VSCode terminal, run:
     ```
     git remote add origin https://github.com/your-username/my-web-project.git
     ```
     - Replace `your-username` with your actual GitHub username.
     - Replace `my-web-project` with your repository name if different.

2. **Verify the Remote:**
   - Run:
     ```
     git remote -v
     ```
   - You should see something like:
     ```
     origin  https://github.com/your-username/my-web-project.git (fetch)
     origin  https://github.com/your-username/my-web-project.git (push)
     ```

3. **Push Your Code to GitHub:**
   - If your local branch is `master`, run:
     ```
     git push -u origin master
     ```
   - If you prefer using `main` as the default branch, you can rename it:
     ```
     git branch -M main
     git push -u origin main
     ```

   - This pushes your local commits to GitHub and sets the remote `origin` as the upstream for your branch.

---

## **Step 8: Verify Your Repository on GitHub**

1. **Navigate to Your Repository:**
   - Go to `https://github.com/your-username/my-web-project` in your browser.

2. **Check Files:**
   - You should see all your project files (`index.html`, `style.css`, `app.js`, `.gitignore`, etc.) listed.

---

## **Step 9: Set Up Additional Configurations (Optional)**

1. **Add a README:**
   - Create a `README.md` file in VSCode with information about your project.
   - Stage and commit the file:
     ```
     git add README.md
     git commit -m "Add README"
     git push
     ```

2. **Set Up Branch Protection (Optional):**
   - In your GitHub repository, go to `Settings` > `Branches`.
   - Add branch protection rules to safeguard your main branch.

3. **Install VSCode Extensions:**
   - **GitLens:** Enhances Git capabilities within VSCode.
   - **Prettier:** Code formatter.
   - **ESLint:** Linting for JavaScript.
   - To install, go to the Extensions pane (left sidebar) and search for these extensions.

---

## **Tips for Efficient Workflow**

- **Use VSCode's Integrated Git:**
  - The **Source Control** pane in VSCode (icon with branches) allows you to stage, commit, and push changes without using the terminal.

- **Regular Commits:**
  - Commit changes frequently with meaningful messages to track progress effectively.

- **Use Branches for Features:**
  - Create separate branches for new features or bug fixes to keep the `main` branch stable.
  - Example:
    ```
    git checkout -b feature/new-feature
    ```

- **Pull Before Pushing:**
  - Especially when collaborating, always pull the latest changes before pushing to avoid conflicts:
    ```
    git pull origin main
    ```

---

## **Summary**

1. **Set Up Environment:**
   - Install VSCode, Git, and ensure you have a GitHub account.

2. **Create and Open Project:**
   - Make a new project folder and open it in VSCode.

3. **Initialize Project Files:**
   - Create essential web files (`index.html`, `style.css`, `app.js`).

4. **Initialize Git:**
   - Run `git init` and create a `.gitignore` file.

5. **Make Initial Commit:**
   - Stage and commit your files with a message.

6. **Create GitHub Repository:**
   - Set up a new repo on GitHub without initializing it with a README.

7. **Link and Push:**
   - Add the GitHub repo as a remote and push your local commits.

8. **Verify and Enhance:**
   - Check your GitHub repo and set up additional configurations as needed.

---

Feel free to reach out if you have any questions or need further assistance with any of the steps!