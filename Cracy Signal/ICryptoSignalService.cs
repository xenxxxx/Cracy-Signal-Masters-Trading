
using CryptoSignalChecker.HttpClients.Models;
using CryptoSignalChecker.Models;

namespace CryptoSignalChecker.Interfaces
{
    public interface ICryptoSignalService
    {
        Task<SignalStatsResponseModel> GetRate(SignalStatsRequestModel request);
    }
}