# REQUIREMENTS

## **Part 1: Documenting the Requirements**

### **1. Introduction**

**Project Overview:**

Create a web application that runs on an Android TV web browser. The application will serve as a building dashboard, displaying essential information and media, such as time, date, messages, photos, weather updates, news, and a to-do list. The application should sync with Google services like Sheets and Photos and use APIs for weather and news updates.

---

### **2. Functional Requirements**

Let's break down each feature into detailed functional requirements.

#### **2.1 Header**

- **Description**: A consistent header displayed across all screens of the application.
- **Requirements**:
  - Display the application name or building address.
  - Include navigation links or icons (if multiple pages are used).
  - Use a design suitable for viewing on a TV screen.

#### **2.2 Time and Date**

- **Description**: Real-time display of the current time and date.
- **Requirements**:
  - Automatically update every minute.
  - Display in a large, easy-to-read font.
  - Support for different time formats (12-hour or 24-hour).

#### **2.3 Building Messages**

- **Description**: Display messages retrieved from a Google Sheets document.
- **Requirements**:
  - Sync with a specific Google Sheets file.
  - Automatically refresh messages at set intervals (e.g., every 5 minutes).
  - Display messages in chronological order.
  - Highlight unread messages (optional).
  - Allow for message deletion or archiving (optional).

#### **2.4 Building Photos**

- **Description**: Show photos from a shared Google Photos album.
- **Requirements**:
  - Integrate with a specific shared album in Google Photos.
  - Display photos in a slideshow format.
  - Allow configuration of slideshow intervals (e.g., time per slide).
  - Support pause, play, and navigation controls (optional).

#### **2.5 Current Weather Forecast**

- **Description**: Display current weather conditions and forecasts.
- **Requirements**:
  - Use a reliable weather API (e.g., OpenWeatherMap).
  - Show current temperature, weather conditions, and an icon representing the weather.
  - Provide a forecast for the next few days.
  - Update weather information every hour.

#### **2.6 News Breaks**

- **Description**: Display the latest news headlines.
- **Requirements**:
  - Fetch news using RSS feeds or a simple news API.
  - Allow selection of news sources (e.g., BBC, CNN).
  - Display headlines with brief summaries.
  - Update news feed every 30 minutes.

#### **2.7 To-Do List**

- **Description**: Show a Building to-do list synced with Google Sheets.
- **Requirements**:
  - Sync with a specific Google Sheets file.
  - Display tasks in a list format.
  - Indicate completed tasks (optional).
  - Allow addition or removal of tasks via Google Sheets.

---

### **3. Non-Functional Requirements**

#### **3.1 Performance**

- The application should load quickly on an Android TV web browser.
- Data updates should not noticeably disrupt the user experience.

#### **3.2 Usability**

- The interface should be intuitive and easy to navigate using a TV remote.
- Text and images must be legible from a typical viewing distance.

#### **3.3 Compatibility**

- The application must run smoothly on standard Android TV web browsers.
- Should be compatible with common TV screen resolutions (e.g., 720p, 1080p).

#### **3.4 Security**

- Secure handling of API keys and authentication tokens.
- Compliance with Google API usage policies.
- Protect any personal or sensitive data.

#### **3.5 Maintainability**

- The codebase should be modular and well-documented.
- Use version control with GitLab for code management.

#### **3.6 Scalability**

- The design should allow for easy addition of new features in the future.
- Efficient data handling to accommodate potential increases in data volume.

---

### **4. Constraints and Assumptions**

#### **Constraints**

- **Technology Stack**: Use Python for backend development; avoid Android-specific frameworks.
- **Web Technologies**: Minimal prior experience, so the solution should be straightforward to implement.
- **Hosting**: Should work with both free and paid hosting solutions.

#### **Assumptions**

- Users will access the application via an Android TV web browser.
- The Building is comfortable using Google Sheets and Google Photos for data input.
- Internet connectivity is available for API access and data synchronization.

---

## **Part 2: Design**

### **1. System Architecture**

#### **1.1 Overview**

The application will follow a client-server architecture:

- **Client**: The Android TV web browser rendering the web application.
- **Server**: A Python-based web server handling data retrieval, processing, and serving HTML content.

#### **1.2 Components**

- **Web Server**: Built using Flask (a lightweight Python web framework).
- **Templates**: HTML templates rendered by Flask using Jinja2 templating engine.
- **Static Assets**: CSS for styling and minimal JavaScript for interactivity.
- **Data Retrieval Modules**: Python scripts or modules to interact with external APIs and services.

#### **1.3 Data Flow**

1. **Client Request**: The user accesses the web application URL on the Android TV browser.
2. **Server Processing**:
   - Retrieves data from Google Sheets (messages and to-do list).
   - Fetches photos from Google Photos.
   - Calls weather and news APIs for the latest information.
3. **Response**: The server renders an HTML page with the latest data and sends it back to the client.
4. **Client Display**: The browser displays the rendered page to the user.

---

### **2. Component Design**

#### **2.1 Backend Components**

- **App Initialization**: The main Flask application instance.
- **Routes**: Define endpoints for the main page and any additional pages.
- **Data Fetching Functions**:
  - **Google Sheets Module**: Handles authentication and data retrieval for messages and to-do lists.
  - **Google Photos Module**: Retrieves images from the shared album.
  - **Weather Module**: Fetches weather data using the selected API.
  - **News Module**: Parses RSS feeds or API responses to get news headlines.
- **Data Processing**: Functions to process and format data for template rendering.

#### **2.2 Frontend Components**

- **Templates**:
  - **Base Template**: Contains common elements like the header and includes placeholders for dynamic content.
  - **Index/Home Template**: Extends the base template and includes sections for each feature.
- **Static Files**:
  - **CSS Stylesheets**: For styling the application.
  - **JavaScript Files**: For any client-side interactions (kept minimal).

---

### **3. User Interface (UI) Design**

#### **3.1 Layout**

- **Header**:
  - Positioned at the top.
  - Displays the application title or Building name.
- **Main Sections**:
  - **Time and Date**: Prominently displayed, possibly in the header or a dedicated section.
  - **Building Messages**: Scrollable area showing the latest messages.
  - **Building Photos**: Slideshow area cycling through images.
  - **Weather Forecast**: Widget displaying current weather and forecasts.
  - **News Breaks**: Section listing the latest news headlines.
  - **To-Do List**: List of tasks retrieved from Google Sheets.
- **Footer** (optional):
  - May include copyright information or additional navigation.

#### **3.2 Navigation and Interaction**

- **Remote-Friendly Controls**:
  - Large buttons and touch targets.
  - Simple navigation paths to avoid complex interactions.
- **Font and Color Choices**:
  - High contrast for readability.
  - Font sizes suitable for viewing from a distance.

---

### **4. Data Models**

Define data models to represent the information handled by the application.

#### **4.1 Message Model**

- **Attributes**:
  - Author
  - Content
  - Timestamp

#### **4.2 Photo Model**

- **Attributes**:
  - Image URL
  - Caption (optional)
  - Date added

#### **4.3 Weather Model**

- **Attributes**:
  - Current temperature
  - Weather condition description
  - Icon URL
  - Forecast data (e.g., next 3 days)

#### **4.4 News Item Model**

- **Attributes**:
  - Headline
  - Summary
  - Source
  - URL to full article

#### **4.5 To-Do Item Model**

- **Attributes**:
  - Task description
  - Assigned to (optional)
  - Due date (optional)
  - Completion status

---

### **5. Sequence Diagrams**

Creating sequence diagrams can help visualize the interactions between components for each use case. Here's an example for fetching and displaying Building messages:

**Use Case**: Display Building Messages

1. **Client** sends a request to the server for the homepage.
2. **Server** receives the request and calls the `fetch_messages()` function.
3. **`fetch_messages()`** authenticates with Google Sheets API.
4. **Google Sheets API** returns the latest messages data.
5. **`fetch_messages()`** processes and formats the data.
6. **Server** renders the homepage template, injecting the messages data.
7. **Server** sends the rendered HTML back to the **Client**.
8. **Client** displays the messages to the user.

---

### **6. UML Class Diagram**

Represent the system's classes and their relationships.

- **Classes**:
  - **FlaskApp**
    - Manages routes and application configuration.
  - **DataFetcher**
    - **Methods**: `fetch_messages()`, `fetch_photos()`, `fetch_weather()`, `fetch_news()`, `fetch_todo_list()`.
  - **Message**, **Photo**, **Weather**, **NewsItem**, **ToDoItem**
    - Data models representing each type of content.
  - **APIClient**
    - Handles authentication and requests to external APIs.

---

## **Part 3: Getting Started**

### **1. Set Up Your Development Environment**

- **Install Python 3.x** if not already installed.
- **Create a Virtual Environment**:
  ```bash
  python3 -m venv env
  source env/bin/activate  # On Windows use env\Scripts\activate
  ```
- **Install Required Packages**:
  ```bash
  pip install flask requests google-api-python-client google-auth-httplib2 google-auth-oauthlib feedparser
  ```

### **2. Initialize Git and GitLab Repository**

- **Initialize Git Repository**:
  ```bash
  git init
  ```
- **Create a .gitignore File**:
  - Exclude virtual environment folders and any sensitive files.
- **Create a New Project on GitLab**:
  - Follow GitLab's instructions to create a new repository.
  - Link your local repository to GitLab:
    ```bash
    git remote add origin https://gitlab.com/your-username/your-repo-name.git
    ```
- **Make Initial Commit and Push**:
  ```bash
  git add .
  git commit -m "Initial commit with project structure and documentation."
  git push -u origin master
  ```

### **3. Document the Requirements**

- **Create a 'docs' Folder** in your project directory.
- **Write the Requirements Document**:
  - Use Markdown (`requirements.md`) or a text document.
  - Include all sections from Part 1 above.
- **Version Control**:
  - Add and commit the requirements document to GitLab.

### **4. Start the Design Documentation**

- **Create Design Diagrams**:
  - Use tools like [Draw.io](https://app.diagrams.net/), [Lucidchart](https://www.lucidchart.com/), or [StarUML](https://staruml.io/).
  - Save diagrams in the 'docs' folder.
- **Write the Design Document**:
  - Document the architecture, component designs, data models, and sequence diagrams.
  - Save as `design.md` or similar.

### **5. Plan Your Development Workflow**

- **Create a Task List**:
  - Break down the project into smaller tasks or user stories.
  - Examples:
    - Set up Flask application structure.
    - Implement Google Sheets data retrieval.
    - Design HTML templates for the homepage.
    - Integrate weather API data.
- **Use GitLab Issues**:
  - Create issues for each task to track progress.
- **Consider Using GitLab's Wiki or Project Management Tools**:
  - For better collaboration and tracking.

### **6. Begin Learning Web Technologies**

- **HTML and CSS Basics**:
  - Start with tutorials on [W3Schools](https://www.w3schools.com/) or [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn).
- **Jinja2 Templating**:
  - Read the [Flask Templating Documentation](https://flask.palletsprojects.com/en/2.0.x/templating/).
- **Flask Framework**:
  - Go through the [Flask Quickstart Guide](https://flask.palletsprojects.com/en/2.0.x/quickstart/).

### **7. Set Up API Access**

- **Google APIs**:
  - **Create a Google Cloud Project**: Go to the [Google Cloud Console](https://console.cloud.google.com/).
  - **Enable APIs**: Enable Google Sheets and Google Photos APIs.
  - **Obtain Credentials**:
    - Create OAuth 2.0 Client IDs.
    - Download the `credentials.json` file.
  - **Set Up Authentication**: Follow the [Python Quickstart Guides](https://developers.google.com/sheets/api/quickstart/python) for proper authentication flow.
- **Weather and News APIs**:
  - **Register for API Keys**:
    - OpenWeatherMap: [Sign Up](https://home.openweathermap.org/users/sign_up).
    - NewsAPI.org or alternative: Register and obtain an API key.
  - **Secure Your API Keys**:
    - Do not commit API keys to version control.
    - Use environment variables or a configuration file excluded from Git.

---

## **Additional Tips**

- **Keep It Iterative**: Develop and test one feature at a time to ensure stability.
- **Code Organization**: Follow best practices for structuring your Flask application (e.g., using Blueprints for modularity).
- **Testing**: Regularly test the application on both desktop and the Android TV browser to catch compatibility issues early.
- **Community Resources**: Don't hesitate to seek help from online communities like Stack Overflow or the Flask community if you encounter challenges.

---

## **Conclusion**

By systematically documenting your requirements and design, you've laid a strong foundation for your project. The next steps involve setting up your development environment, familiarizing yourself with necessary technologies, and beginning the coding process. Remember to keep your project organized with proper version control and documentation.
