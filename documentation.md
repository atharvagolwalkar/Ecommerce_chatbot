# Technical Documentation: E-commerce Sales Chatbot

## 1. Overview
The E-commerce Sales Chatbot is a web-based application that integrates a chatbot interface to assist users in interacting with an e-commerce platform. The system allows users to perform actions like registering, logging in, searching for products, and receiving recommendations, all while maintaining a smooth, real-time interaction with the chatbot.

The project is built using a React frontend for the user interface and Flask as the backend server. The database is handled using SQLite and SQLAlchemy ORM to store and manage user data, products, and chat history.

## 2. Architecture
### 2.1 High-Level Architecture
The architecture follows a client-server model with the following key components:

Frontend (React): The user interface of the application is built with React, enabling interactive features such as registration, login, product search, and chat interactions.
Backend (Flask): The Flask application manages API routes, handles user authentication, and processes requests for product retrieval and chat history.
Database (SQLite): The backend uses SQLite for storing information about users, products, and chat messages.
API Communication: A separate api.js file in the React app (built using JavaScript/Node) handles communication between the frontend and backend using HTTP requests.

## 3. Technology Stack
### 3.1 Frontend
React: The frontend is built using React, providing a responsive and dynamic user interface. The following components are used:
src/index.js: The entry point of the React application.
src/App.js: Main component that sets up the application structure and routing.
src/components/Chatbot.js: Chatbot component responsible for user interactions, authentication, message input, and API communication.
src/services/api.js: Contains functions to interact with the Flask backend API for user registration, login, product search, and chat history.
Tailwind CSS: The frontend is styled using Tailwind CSS, which is configured using postcss.config.js and tailwind.config.js files.
### 3.2 Backend
Flask: The backend is built with Flask, which exposes RESTful API endpoints to handle user authentication, product search, and chat message management. The main file is:
backend/app.py: Contains the routes for user registration (/auth/register), login (/auth/login), product search (/products/search), and saving chat messages.
SQLite: The backend uses SQLite to store user data, products, and chat messages. The database is interacted with via SQLAlchemy, a powerful ORM.

## 4. Functionality Breakdown
### 4.1 User Authentication
Backend: User authentication is handled by the Flask application through the /auth/register and /auth/login routes. The POST requests to these endpoints are processed to register or authenticate users based on their credentials.
Frontend: The React components allow users to input their credentials and send requests to the backend for registration and login.
### 4.2 Product Search
Backend: The Flask backend exposes the /products/search endpoint, which allows the frontend to search for products by query and category. The backend processes this and returns matching product data.
Frontend: The frontend makes API calls to search products and displays the results in an interactive UI.
### 4.3 Chatbot Interaction
Backend: The backend stores and processes chat messages using the /chat/message endpoint. Users can send messages to the chatbot, which are stored in the database for future retrieval.
Frontend: The Chatbot.js component handles user input and displays chatbot responses in real-time, allowing for interactive conversation.

## 5. Database Design
The application uses SQLite for managing the following entities:

User:

id: Primary key, unique identifier for each user.
username: The user's username.
password: The user's password (stored securely).
Product:

id: Primary key, unique identifier for each product.
name: The name of the product.
category: The category to which the product belongs.
price: The price of the product.
ChatMessage:

id: Primary key, unique identifier for each message.
user_id: Foreign key to the User who sent the message.
content: The message content (text).
type: Type of message (e.g., user or bot).
timestamp: Timestamp for when the message was sent.

## 6. Key Files and Their Purpose
### 6.1 Frontend (React)
src/index.js: Entry point for the application, rendering the App component and setting up the root structure.
src/App.js: Main application component that manages routing and renders child components such as the Chatbot and product search features.
src/components/Chatbot.js: Handles all chatbot-related functionality, including message input, displaying messages, and interacting with the backend API.
src/services/api.js: Contains functions for making API requests to the Flask backend for user authentication, product search, and chat message handling.
register(username, password): Sends a request to the /auth/register endpoint to create a new user.
login(username, password): Sends a request to the /auth/login endpoint to authenticate the user.
searchProducts(query, category): Sends a request to the /products/search endpoint to search for products based on the provided query and category.
### 6.2 Backend (Flask)
backend/app.py: Contains the Flask application and the API routes for managing authentication, product search, and chat history.
database: The SQLite database is used to store users, products, and chat messages. SQLAlchemy ORM is used to interact with the database.
### 6.3 Styling
src/index.css: Contains global styles for the application.
src/App.css: Custom styles specific to the App component.
tailwind.config.js: Configuration file for Tailwind CSS, including theme customizations and content paths.
### 6.4 Package Management
package.json: Manages dependencies for both frontend and testing, such as React, Axios, Jest, and Tailwind CSS.

## 7. Challenges and Solutions
### 7.1 Challenge 1: Real-time Chatbot Integration
Problem: Maintaining a real-time interaction with the chatbot while storing and retrieving chat messages.
Solution: The frontend uses React’s state management to handle real-time updates. Messages are sent to the backend via API calls and stored in the SQLite database. When needed, the chat history is fetched from the backend.
### 7.2 Challenge 2: Product Search Efficiency
Problem: Efficiently handling product searches across multiple parameters (query, category, etc.).
Solution: The backend filters products by parameters provided in the API request, and uses indexing in the database to improve search performance.
### 7.3 Challenge 3: User Authentication Without JWT
Problem: Implementing user authentication securely without using JWT.
Solution: Authentication is handled via session-based management on the backend, where users' credentials are validated and authenticated via Flask routes.

## 8. Conclusion
This E-commerce Sales Chatbot project integrates a responsive and user-friendly chatbot into an e-commerce platform. The system is powered by a React frontend for interactivity and a Flask backend for handling API requests and business logic. The SQLite database efficiently stores user data, products, and chat history. The application also offers a smooth, real-time interaction experience through the chatbot, while the SQLAlchemy ORM ensures effective database management.