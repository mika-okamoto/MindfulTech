import axios from 'axios';
const REST_API_BASE_URL = "http://localhost:5000";

export const chat = async (chatRequest) => {
    const response = await axios.post(REST_API_BASE_URL + "/predict", request)
    return response.data }

export const generateText = async (predictRequest) => {
    const response = await axios.post(REST_API_BASE_URL + "/chat", request)
    return response.data }