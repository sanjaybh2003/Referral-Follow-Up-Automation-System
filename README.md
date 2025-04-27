# Expense Tracker Full-Stack App

A full-stack web application built with **React**, **Express**, and **MongoDB** for recording, managing, and visualizing your expenses.

---

## Technologies Used

- **Frontend**: React, Axios, React-Chartjs-2 (Chart.js)  
- **Backend**: Node.js, Express.js, Mongoose  
- **Database**: MongoDB (local or Atlas)  
- **Styling**: Custom CSS  
---

## Features

- **Add**, **Edit**, and **Delete** expense records  
- **Category**-based tracking  
- **Pie chart** for category distribution  
- **Bar chart** for monthly spending  
- Responsive, user-friendly interface  

---

## Backend

cd backend
npm install
# create .env with:
# MONGO_URI=mongodb://localhost:27017/expense-tracker
# PORT=5000
npm start

## Frontend 

cd ../frontend
npm install
# create .env with:
# REACT_APP_API_URL=http://localhost:5000/expenses
npm start

## API Endpoints 

GET /expenses — list all expenses
POST /expenses — add new expense
PUT /expenses/:id — update expense
DELETE /expenses/:id — remove expense

## Screenshots

I've added screenshots of working both forntend and backend servers in Screenshots Folder in Project Structure

