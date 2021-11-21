import fetch from 'isomorphic-fetch';
// import { HOST } from "react-dotenv"

export async function callApi({ endpoint, method = 'get', body = undefined, token = undefined, fullUrl = false }) {
    let url = ''
    if (fullUrl) {
        url = endpoint;
    } else {
        url = `http://192.168.1.149:4000/${endpoint}`;
    }

    const headers = {
        'content-type': 'application/json',
    }

    if (token) headers['Authorization'] = `Bearer ${token}`

    return await fetch(url, { method, body: JSON.stringify(body) })
        .then(async (response) => {
            if (!response.ok) {
                return response.json()
                    .then((json) => {
                        return Promise.reject(json)
                    });
            }
            return response.json() || response.text();
        });
}