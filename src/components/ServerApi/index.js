import { callApi } from './callApi';

export const getBTCPrice = async (id, token) => {
  return await callApi({ endpoint: `https://api.coindesk.com/v1/bpi/currentprice.json`, fullUrl: true })
};