# Restaurant Finder Application

## Overview
Restaurant Finder is a web-based application that allows users to search for restaurants based on a food item. Users can either enter a food name or upload an image, and the system retrieves relevant restaurant data.

## Features
- Search for restaurants by food name or image upload.
- Utilize the Gemini API (via `google.generativeai`) for food image recognition.
- Query a JSON-based restaurant database to fetch relevant results.

## Technology Stack
- **Frontend:** React.js, HTML, CSS
- **Backend:** Node.js, Express.js
- **Database:** JSON-based storage (extendable to MongoDB or MySQL)
- **APIs Used:** Google Gemini API (for image processing)

## Installation
### Prerequisites
- Node.js and npm installed
- Git installed

### Steps to Install
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd restaurant-finder
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the backend server:
   ```sh
   node server.js
   ```
4. Start the frontend:
   ```sh
   cd client
   npm start
   ```

## Usage
1. Open the application in your browser.
2. Enter a food item or upload an image.
3. View the list of restaurants serving the specified food.

## Future Enhancements
- Expand database to include real-time restaurant data.
- Improve image recognition accuracy.
- Optimize performance and scalability.



