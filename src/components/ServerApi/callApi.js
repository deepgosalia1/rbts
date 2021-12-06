import fetch from 'isomorphic-fetch';
import ip from 'local-ip-url'
import defaultGateway from 'default-gateway'
// import {internalIpV6, internalIpV4} from 'internal-ip';

// import { HOST } from "react-dotenv"

export async function callApi({ endpoint, method = 'get', body = undefined, fullUrl = false }) {
    console.log(ip('private', 'ipv4'), await defaultGateway.v4())
    let url = ''
    if (fullUrl) {
        url = endpoint;
    } else {
        url = `http://192.168.1.149:4000/${endpoint}`;
    }
    // console.log('body', body)
    return await fetch(url, { method, body: JSON.stringify(body) })
        .then(async (response) => {
            if (!response.ok) {
                alert('An error Occured. Please verify the inputs/operation you are trying to perform.')
                return response.json()
                    .then((json) => {
                        return Promise.reject(json)
                    });
            }
            return response.json() || response.text();
        });
}