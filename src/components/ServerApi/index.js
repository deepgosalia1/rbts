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

export const placeIndependentTrade = async (cid, txamount, txtype, txdate, currBTCPriceinUSD) => {
  return await callApi({ endpoint: 'client/independentTrade', method: 'post', body: { cid, txamount, txtype, txdate, currBTC: currBTCPriceinUSD } })
};

export const placeTraderDependentTrade = async (cid, txamount, txtype, commtype, txdate, currBTCPriceinUSD) => {
  return await callApi({ endpoint: 'client/dependentTrade', method: 'post', body: { cid, txamount, txtype, commtype, txdate, currBTC: currBTCPriceinUSD } })
};

export const placeTopUpRequest = async (cid, fiatamount, txdate) => {
  return await callApi({ endpoint: 'transactions/topup', method: 'post', body: { cid, fiatamount, txtype: 2, txdate } })
};

export const ApproveTopupRequet = async (txid, cid, fiatamount, txdate) => {
  return await callApi({ endpoint: 'transactions/approveTopup', method: 'post', body: { txid, cid, fiatamount, txdate } })
};

export const RejectTopup = async (txid, cid, txdate) => {
  return await callApi({ endpoint: 'transactions/rejectTopup', method: 'post', body: { txid, cid, txdate } })
};