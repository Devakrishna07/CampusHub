import axios from "axios";

const BASE_URL = 'https://campushub-ys56.onrender.com';

const axiosInstance = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

axiosInstance.interceptors.request.use(
  (config) => {
    const publicPaths = ['/users/register/', '/users/login/'];
    const isPublic = publicPaths.some((path) => config.url.includes(path));

    if (!isPublic) {
      const token = localStorage.getItem('accessToken');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
    }
    return config;
  },
  (error) => Promise.reject(error)
);


const api = {
  get: (url, config = {}) => axiosInstance.get(url, config),
  post: (url, data, config = {}) => axiosInstance.post(url, data, config),
  put: (url, data, config = {}) => axiosInstance.put(url, data, config),
  del: (url, config = {}) => axiosInstance.delete(url, config),
};

export default api;
