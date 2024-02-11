import axios from 'axios';
const REST_API_BASE_URL = "http://127.0.0.1:5000";

export const chat = async (chatRequest) => {
    const response = await axios.post(REST_API_BASE_URL + "/chat", chatRequest)
    return response.data }

export const submitSurvey = async (predictRequest) => {
    const response = await axios.post(REST_API_BASE_URL + "/predict", predictRequest)
    return response.data }