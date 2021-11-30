import { callApi } from './callApi';
import sha1 from 'sha1';

export const loginUserAPI = async (username, pass_hash) => {
  return await callApi({ endpoint: 'login', method: 'post', body: { username, pass_hash: sha1(pass_hash) } })
}

export const getBTCPrice = async (id) => {
  return await callApi({ endpoint: `https://api.coindesk.com/v1/bpi/currentprice.json`, fullUrl: true })
};

export const getAllTransactions = async (id) => {
  return await callApi({ endpoint: 'trader/gettransactions', method: 'get' })
};

export const getAllData = async (type) => {
  return await callApi({ endpoint: 'manager/gettypedata', method: 'post', body: { type } })
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

export const getPendingTransactions = async () => {
  return await callApi({ endpoint: 'trader/getPendingTransactions', method: 'get' })
};

export const ApproveTrade = async (txid, currBTC, txtype) => {
  return await callApi({ endpoint: 'transactions/approveTrade', method: 'post', body: { txid, currBTC, txtype } })
};

export const RejectTrade = async (txid, txtype) => {
  return await callApi({ endpoint: 'transactions/rejectTrade', method: 'post', body: { txid, txtype } })
};

export const getDailyData = async (start_date, end_date) => {
  return await callApi({ endpoint: 'manager/daily', method: 'post', body: { start_date, end_date } })
};

export const getWeeklyData = async (start_date, end_date) => {
  return await callApi({ endpoint: 'manager/weekly', method: 'post', body: { start_date, end_date } })
};

export const getMonthlyData = async (start_date, end_date) => {
  return await callApi({ endpoint: 'manager/monthly', method: 'post', body: { start_date, end_date } })
};

export const getSearchData = async (searchKey, type) => {
  return await callApi({ endpoint: 'trader/search', method: 'post', body: { key: searchKey, type } })
};

