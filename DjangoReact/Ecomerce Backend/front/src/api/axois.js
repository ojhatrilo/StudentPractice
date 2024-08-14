// src/api/axios.js
import axios from 'axios';

// Create an Axios instance with global configuration
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Replace with your API base URL
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json',
    // Add other headers as needed
  },
});

// Request interceptor to add token or modify requests globally
axiosInstance.interceptors.request.use(
  config => {
    // Add token to headers if needed
    // const token = localStorage.getItem('token');
    // if (token) {
    //   config.headers.Authorization = `Bearer ${token}`;
    // }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle global responses
axiosInstance.interceptors.response.use(
  response => {
    return response;
  },
  error => {

    // Any status codes outside the range of 2xx cause this function to trigger
    if (error.response && error.response.status === 401) {
      // Handle unauthorized access

      console.error('Unauthorized access, redirecting to login...');
      // Optionally redirect to login page
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
