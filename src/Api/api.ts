import axios from "axios";

const server = "http://127.0.0.1:8000/api/";
const api = {
  loadCollectors: () => axios.get(`${server}collectors/`),
  loadWada: () => axios.get(`${server}wards/`),
  loadMarga: () => axios.get(`${server}margas/`),
  loadBasti: () => axios.get(`${server}bastis/`),
};

export default api;
