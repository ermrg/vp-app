import axios from "axios";

const server = `${process.env.REACT_APP_SERVER}/api/`;
const api = {
  loadCollectors: () => axios.get(`${server}collectors/`),
  loadWada: () => axios.get(`${server}wards/`),
  loadMarga: () => axios.get(`${server}margas/`),
  loadBasti: () => axios.get(`${server}bastis/`),
};

export default api;
