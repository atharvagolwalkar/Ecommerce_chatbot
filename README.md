# E-Commerce Chatbot Application

## Project Overview
This project is an e-commerce chatbot application built with a **React** frontend and a **Flask** backend. It allows users to interact with the system for product searches, recommendations, and chat-based assistance, providing a seamless shopping experience.

## Objectives
The main objective of this project is to enhance user engagement through a chatbot interface, providing product information, recommendations, and helping users search for products. The chatbot aims to simplify product exploration while offering a smooth and intuitive user experience.

## Technologies Used
### Frontend
- **React**: A JavaScript library for building user interfaces, used to create the chatbot and user interface components.
- **CSS**:  Used for styling and enhancing UI/UX.

### Backend
- **Python (Flask)**: A lightweight WSGI web application framework used to create the backend APIs for user authentication, product retrieval, and chat history management.
- **SQLite**: A lightweight database used to store user data, products, and chat history.

### Other Tools
- **SQLAlchemy**: An ORM used to manage database interactions in Python.
- **JavaScript (Fetch API)**: Used for making API requests from the React frontend to the Flask backend.

## Installation and Setup
### Prerequisites
Before you begin, ensure you have the following installed:
- Node.js (for the frontend)
- Python 3.8+ (for the backend)
- SQLite (for database)

### Backend Setup (Flask)
1. Clone the repository and navigate to the backend directory:
   ```bash
   git clone <repository-url>
   cd backend
2.  Create a virtual environment and activate it and install required packages:
    
   ``` bash  
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate` `
	'pip install -r requirements.txt'	
```
4.  Run the Flask application:
    
    ``` bash
     'flask run' 
    ```

### Frontend Setup (React)

1.  Navigate to the frontend directory:
    
    ``` bash    
        `cd src` 
    ```
    
2.  Install dependencies:
    
    ``` bash 
        `npm install` 
    ```
    
3.  Start the React development server:
    
    ``` bash
	    `npm start` 
``` bash
The application will be available at `http://localhost:3000` for the frontend and `http://localhost:5000` for the backend.
```
## API Documentation

### User Authentication

-   **POST** `/auth/register`: Registers a new user.
-   **POST** `/auth/login`: Authenticates a user and returns a session.

### Product Endpoints

-   **GET** `/products?search=<query>&category=<category>`: Search for products by query and category.
-   **GET** `/products/category/<category>`: Get products by category.
-   **GET** `/products/price-range?min_price=<min>&max_price=<max>`: Filter products by price range.

### Chat Endpoints

-   **POST** `/chat/message`: Stores a user’s chat message.
-   **GET** `/chat/history?user_id=<userId>`: Retrieves chat history for a user.

## Methodology and Approach

-   **Modular Architecture**: The frontend and backend are decoupled, allowing for easier maintainability and scalability. Each component in React is self-contained, handling specific tasks like user input and chatbot responses.
-   **API-driven Development**: All interactions between the frontend and backend happen via APIs, making the system extensible for future features.
-   **Error Handling**: Error handling mechanisms are in place to ensure the application fails gracefully in case of issues with API calls or database queries.

## Challenges Faced and Solutions

1.  **Managing Authentication**: One of the key challenges was managing user sessions across the chatbot interface. This was handled by building custom login functionality with session handling in Flask.
    
2.  **Efficient Product Search**: To ensure a fast and efficient search experience, we implemented search filters for product categories and price ranges, optimizing API queries.
    
3.  **State Management in React**: Handling the chatbot’s conversation flow required careful state management, ensuring that both the user input and the bot’s responses were in sync.
    

## Learnings

-   Leveraging **React** for building complex user interfaces allowed for a clean separation of concerns between components.
-   Using **Flask** for the backend API made it simple to create RESTful endpoints and integrate with a database.
-   Implementing user authentication and session management in **Flask** provided a deeper understanding of web security principles.

## Results and Screenshots

-   **Product Search Interface**: Users can search for products by name or filter by category and price range.
-   **Chatbot Interaction**: Users can interact with the chatbot for personalized product recommendations.
-   **Registration**: User can create an account.
-   **Login**: User can log in to their account.

_Include screenshots here_
#### Chatbot Interface
![Chatbot Screenshot](ecommerce-chatbot\assets\1.png)

#### Product Search Results
![Product Search Results](ecommerce-chatbot\assets\2.png)

#### Registration
![Registration](ecommerce-chatbot\assets\3.png)

#### Login
![Login](ecommerce-chatbot\assets\4.png)

## Conclusion

This project demonstrates the integration of a chatbot within an e-commerce platform, enhancing the shopping experience with an interactive and intelligent interface. The use of modern frameworks like **React** and **Flask** ensures a maintainable, scalable, and modular codebase. Future enhancements could include adding recommendation systems using machine learning algorithms and expanding the chatbot’s functionality to handle complex user queries.