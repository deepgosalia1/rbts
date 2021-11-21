import { callApi } from './callApi';

export const loginUserAPI = async (uid,username, pass_hash) => {
  return await callApi({endpoint:'login', method:'post', body:{uid,username,pass_hash}})
}

export const getBTCPrice = async (id, token) => {
  return await callApi({ endpoint: `https://api.coindesk.com/v1/bpi/currentprice.json`, fullUrl: true })
};