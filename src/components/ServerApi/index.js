import { callApi } from './callApi';
import sha1 from 'sha1';

export const loginUserAPI = async (username, pass_hash) => {
  return await callApi({endpoint:'login', method:'post', body:{username,pass_hash:sha1(pass_hash)}})
}

export const getBTCPrice = async (id, token) => {
  return await callApi({ endpoint: `https://api.coindesk.com/v1/bpi/currentprice.json`, fullUrl: true })
};