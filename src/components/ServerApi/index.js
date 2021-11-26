import { callApi } from './callApi';
import sha1 from 'sha1';

export const loginUserAPI = async (username, pass_hash) => {
  return await callApi({ endpoint: 'login', method: 'post', body: { username, pass_hash: sha1(pass_hash) } })
}

export const getBTCPrice = async (id) => {
  return await callApi({ endpoint: `https://api.coindesk.com/v1/bpi/currentprice.json`, fullUrl: true })
};

export const getClientTransactions = async (id) => {
  return await callApi({ endpoint: 'client/transactions', method: 'post', body: { cid: id } })
};