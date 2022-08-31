import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Routes, Route,BrowserRouter } from "react-router-dom"
import reportWebVitals from './reportWebVitals';
import { LinkedInCallback } from 'react-linkedin-login-oauth2';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="" element={<App />} />
        <Route path="linkedin" element={<LinkedInCallback />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
reportWebVitals();
