using CryptoSignalChecker.Enums;
using CryptoSignalChecker.HttpClients;
using CryptoSignalChecker.HttpClients.Models;
using CryptoSignalChecker.Interfaces;
using CryptoSignalChecker.Models;

namespace CryptoSignalChecker.Services
{
    public class CryptoSignalService : ICryptoSignalService
    {
        private readonly BinanceHttpClient _binanceHttpClient;
        private readonly int _serverHoursDiff;

        public CryptoSignalService(BinanceHttpClient binanceHttpClient)
        {
            _binanceHttpClient = binanceHttpClient;
            var serverTimeUnixMs = _binanceHttpClient.GetBinanceServerTime().GetAwaiter().GetResult();
            _serverHoursDiff = (DateTime.Now - DateTimeFromUnixMs(serverTimeUnixMs.ServerTime)).Hours;
        }

        public async Task<SignalStatsResponseModel> GetRate(SignalStatsRequestModel request)
        {
            var interval = "1m";
            var startTimeMs = new DateTimeOffset(request.SignalDateTime.AddHours(-_serverHoursDiff)).ToUnixTimeMilliseconds();
            var endTime = (DateTime.Now > request.SignalEndDateTime ? DateTime.Now : request.SignalEndDateTime).AddHours(-_serverHoursDiff);
            var endTimeMs = new DateTimeOffset(endTime).ToUnixTimeMilliseconds();

            var tokenRates = await _binanceHttpClient.GetTokenRates(request.TokenPair, interval, startTimeMs, endTimeMs);

            while(tokenRates.LastOrDefault().KlineCloseTime < endTimeMs)
            {
                startTimeMs = tokenRates.LastOrDefault().KlineCloseTime;
                var addTokenRates = await _binanceHttpClient.GetTokenRates(request.TokenPair, interval, startTimeMs, endTimeMs);
                if (addTokenRates.Count() == 0) break;
                tokenRates = tokenRates.Concat(addTokenRates);
            }

            var result = new SignalStatsResponseModel();
            double approximateLiquidation = (100 + (request.FuturesType == FuturesType.Long ? -100 / 1.1 : 100 / 1.4) / request.Leverage) * request.Entry / 100;

            Func<double, double, DateTime, bool, bool> compareFunc =
                (price, comparePrice, compareDateTime, isTakeProfit) => (isTakeProfit ?
                    (request.FuturesType == FuturesType.Long ?
                        price >= comparePrice :
                        price <= comparePrice) : 
                    (request.FuturesType == FuturesType.Long ?
                        price <= comparePrice :
                        price >= comparePrice))
                    && compareDateTime == default;

            foreach (var tokenRate in tokenRates)
            {

                if (compareFunc(GetPriceByFuturesType(tokenRate, request.FuturesType, false), request.StopLoss, result.StopLoss, false))
                {
                    result.StopLoss = DateTimeFromUnixMs(tokenRate.KlineOpenTime).AddHours(_serverHoursDiff);
                    continue;
                }

                if (compareFunc(GetPriceByFuturesType(tokenRate, request.FuturesType, false), approximateLiquidation, result.AprxmtLiquidation, false))
                {
                    result.AprxmtLiquidation = DateTimeFromUnixMs(tokenRate.KlineOpenTime).AddHours(_serverHoursDiff);
                    continue;
                }

                if (request.TakeProfits.Any(takeProfit =>
                        compareFunc(GetPriceByFuturesType(tokenRate, request.FuturesType, true),
                            takeProfit.Value, takeProfit.DateTime, true)))
                {
                    var takeProfits = request.TakeProfits.Where(takeProfit =>
                        compareFunc(GetPriceByFuturesType(tokenRate, request.FuturesType, true),
                            takeProfit.Value, takeProfit.DateTime, true)).ToList();

                    takeProfits.ForEach(x => x.DateTime = DateTimeFromUnixMs(tokenRate.KlineOpenTime).AddHours(_serverHoursDiff));
                    result.TakeProfitStats.AddRange(takeProfits);
                }
            }

            return result;
            //https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1s&startTime=1664852400000&endTime=1664881200000
        }


        private static double GetPriceByFuturesType(TokenRate tokenRate, FuturesType futuresType, bool isTakeProfit)
        {
            if (isTakeProfit)
            {
                if (futuresType == FuturesType.Long)
                {
                    return tokenRate.HighPrice;
                }
                return tokenRate.LowPrice;
            }

            if (futuresType == FuturesType.Long)
            {
                return tokenRate.LowPrice;
            }
            return tokenRate.HighPrice;
        }

        private static DateTime DateTimeFromUnixMs(long millis)
        {
            return DateTime.UnixEpoch.AddMilliseconds(millis);
        }
    }
}
