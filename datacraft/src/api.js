import axios from 'axios';

const API_URL = 'http://localhost:8000/test/';

export const getTests = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error("Erro ao buscar dados:", error);
        throw error;
    }
};