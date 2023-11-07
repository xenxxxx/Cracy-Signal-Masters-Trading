import 'package:crypto_app/data/model/constant/constants.dart';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:crypto_app/data/model/crypto.dart';
import 'package:flutter/services.dart';
import 'package:fluttertoast/fluttertoast.dart';

class CryptoListScreen extends StatefulWidget {
  CryptoListScreen({super.key, this.cryptoList});
  List<Crypto>? cryptoList;

  @override
  State<CryptoListScreen> createState() => _CryptoListScreenState();
}

class _CryptoListScreenState extends State<CryptoListScreen> {
  List<Crypto>? cryptoList;
  bool isVisibleLoading = false;
  DateTime ?currentBackPressTime;
  @override
  void initState() {
    super.initState();
    cryptoList = widget.cryptoList;
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: blackColor,
        centerTitle: true,
        title: Text(
          "Crypto Market",
          style: TextStyle(fontWeight: FontWeight.bold, fontFamily: 'rrr'),
          textAlign: TextAlign.center,
        ),
        automaticallyImplyLeading: false,
      ),
      backgroundColor: blackColor,
      body: WillPopScope(onWillPop: onWillPop,
        child: SafeArea(
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: TextField(
                  onChanged: (value) async {
                    isVisibleLoading = true;
                    List<Crypto> freshData = await _getData();
                    setState(() {
                      cryptoList = freshData;
                    });
                    Future.delayed(Duration(milliseconds: 700), () {
                      setState(() {
                        isVisibleLoading = false;
                      });
                    });
      
                    _searchFilter(value);
                  },
                  decoration: InputDecoration(
                      hintText: 'Enter the cryptocurrency name',
                      hintStyle: TextStyle(
                          color: Colors.white, fontWeight: FontWeight.bold),
                      border: OutlineInputBorder(
                        borderSide: BorderSide(width: 0, style: BorderStyle.none),
                        borderRadius: BorderRadius.circular(30),
                      ),
                      filled: true,
                      fillColor: greenColor),
                ),
              ),
              Visibility(
                visible: isVisibleLoading,
                child: Text(
                  'Loading the Cryptocurrencies ... ',
                  style: TextStyle(color: greenColor),
                ),
              ),
              Expanded(
                child: RefreshIndicator(
                  backgroundColor: Colors.grey[800],
                  color: greenColor,
                  onRefresh: () async {
                    isVisibleLoading = true;
                    List<Crypto> freshData = await _getData();
      
                    setState(() {
                      cryptoList = freshData;
                    });
                    Future.delayed(Duration(milliseconds: 700), () {
                      setState(() {
                        isVisibleLoading = false;
                      });
                    });
                  },
                  child: ListView.builder(
                    itemCount: cryptoList!.length,
                    itemBuilder: (context, index) {
                      return _getListTileItemBuilder(cryptoList![index]);
                    },
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _getListTileItemBuilder(Crypto crypto) {
    return ListTile(
      title: Text(
        crypto.name,
        style: TextStyle(color: greenColor),
      ),
      subtitle: Text(
        crypto.symbol,
        style: TextStyle(color: greyColor),
      ),
      leading: SizedBox(
        width: 30,
        child: Center(
          child: Text(
            crypto.rank.toString(),
            style: TextStyle(color: greyColor),
          ),
        ),
      ),
      trailing: SizedBox(
        width: 150,
        child: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              SizedBox(
                width: 80,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.attach_money,
                          color: Colors.white,
                          size: 12,
                        ),
                        Text(
                          crypto.priceUsd.toStringAsFixed(2),
                          style: TextStyle(color: Colors.white),
                        ),
                      ],
                    ),
                    Text(
                      crypto.changePercent24hr.toStringAsFixed(2),
                      style: TextStyle(
                        color: _getChangeColor(crypto.changePercent24hr),
                      ),
                    )
                  ],
                ),
              ),
              SizedBox(
                width: 20,
                child: Center(
                  child: _getIconChangePercent(crypto.changePercent24hr),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _getIconChangePercent(double change) {
    return change <= 0
        ? Icon(
            Icons.trending_down,
            color: redColor,
            size: 30,
          )
        : Icon(
            Icons.trending_up,
            color: greenColor,
            size: 30,
          );
  }

  Color _getChangeColor(double change) {
    return change <= 0 ? redColor : greenColor;
  }

  Future<List<Crypto>> _getData() async {
    var response = await Dio().get('https://api.coincap.io/v2/assets');

    List<Crypto> cryptoList = response.data['data']
        .map<Crypto>((jsonMapObject) => Crypto.fromMapJson(jsonMapObject))
        .toList();
    return cryptoList;
  }

  void _searchFilter(String enteredKeyword) {
    List<Crypto> cryptoResultList = [];

    cryptoResultList = cryptoList!.where((element) {
      return element.name.toLowerCase().contains(enteredKeyword.toLowerCase());
    }).toList();
    setState(() {
      cryptoList = cryptoResultList;
    });
  }
  Future<bool> onWillPop() {
    DateTime now = DateTime.now();
    if (currentBackPressTime == null || 
        now.difference(currentBackPressTime!) > Duration(seconds: 2)) {
      currentBackPressTime = now;
      Fluttertoast.showToast(msg: "you are exiting...");
      SystemChannels.platform.invokeMethod('SystemNavigator.pop');
      return Future.value(false);
    }
    return Future.value(true);
  }
}
