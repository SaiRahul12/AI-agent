// src/api.js
import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api"; // Update to your backend URL

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

export const performSearch = async (query) => {
  const response = await axios.post(`${API_BASE_URL}/search`, query);
  return response.data;
};
