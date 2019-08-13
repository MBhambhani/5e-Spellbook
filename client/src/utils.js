import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

function getSpells(cls) {
  return axios.get(`${API_URL}/spells?filter=${cls}`);
}

function register(userData) {
  return axios.post(`${API_URL}/register`, userData);
}

function login(userData) {
  return axios.post(`${API_URL}/login`, userData);
}

function createBook(data, jwt) {
  return axios.post(`${API_URL}/create-spellbook`, data, { headers: { Authorization: `Bearer: ${jwt}` } });
}

function deleteBook(data, jwt) {
  return axios.post(`${API_URL}/delete-spellbook`, data, { headers: { Authorization: `Bearer: ${jwt}` } });
}

function getAllBooksForUser(data, jwt) {
  return axios.get(`${API_URL}/get-user-spellbooks`, data, { headers: { Authorization: `Bearer: ${jwt}` } });
}

function getBook(data, jwt) {
  return axios.get(`${API_URL}/get-spellbook`, data, { headers: { Authorization: `Bearer: ${jwt}` } });
}

function addToBook(data, jwt) {
  return axios.post(`${API_URL}/add-to-spellbook`, data, { headers: { Authorization: `Bearer: ${jwt}` } });
}

function removeFromBook(data, jwt) {
  return axios.post(`${API_URL}/remove-from-spellbook`, data, { headers: { Authorization: `Bearer: ${jwt}` } });
}

export default {
  getSpells,
  register,
  login,
  createBook,
  deleteBook,
  getBook,
  getAllBooksForUser,
  addToBook,
  removeFromBook,
};
