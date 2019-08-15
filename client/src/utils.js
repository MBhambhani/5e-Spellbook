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
  return axios.post(
    `${API_URL}/create-spellbook`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function deleteBook(data, jwt) {
  return axios.post(
    `${API_URL}/delete-spellbook`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function getAllBooksForUser(jwt) {
  return axios.get(
    `${API_URL}/get-user-spellbooks`,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function getBook(name, jwt) {
  return axios.get(
    `${API_URL}/get-spellbook?name=${name}`,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function addSpellToBook(data, jwt) {
  return axios.post(
    `${API_URL}/add-spell-to-spellbook`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function removeSpellFromBook(data, jwt) {
  return axios.post(
    `${API_URL}/remove-spell-from-spellbook`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function getCustomSpells(jwt) {
  return axios.get(
    `${API_URL}/get-custom-spells`,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function addCustomSpell(data, jwt) {
  return axios.post(
    `${API_URL}/add-custom-spell`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function deleteCustomSpell(data, jwt) {
  return axios.post(
    `${API_URL}/delete-custom-spell`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function editCustomSpell(data, jwt) {
  return axios.post(
    `${API_URL}/edit-custom-spell`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function addCustomSpellToBook(data, jwt) {
  return axios.post(
    `${API_URL}/add-custom-spell-to-spellbook`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

function removeCustomSpellFromBook(data, jwt) {
  return axios.post(
    `${API_URL}/remove-custom-spell-from-spellbook`,
    data,
    { headers: { Authorization: `Bearer: ${jwt}` } },
  );
}

export default {
  getSpells,
  register,
  login,
  createBook,
  deleteBook,
  getBook,
  getAllBooksForUser,
  addSpellToBook,
  removeSpellFromBook,
  getCustomSpells,
  addCustomSpell,
  deleteCustomSpell,
  editCustomSpell,
  addCustomSpellToBook,
  removeCustomSpellFromBook,
};
