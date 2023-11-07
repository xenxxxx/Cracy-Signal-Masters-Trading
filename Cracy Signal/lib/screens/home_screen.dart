import 'package:crypto_app/data/model/constant/constants.dart';
import 'package:crypto_app/screens/crypto_list_screen.dart';
import 'package:dio/dio.dart';
import 'package:crypto_app/data/model/crypto.dart';
import 'package:flutter/material.dart';
import 'package:loading_animation_widget/loading_animation_widget.dart';

class HomeScreen extends StatefulWidget {
  HomeScreen({super.key, this.cryptoList});
  List<Crypto>? cryptoList;

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<Crypto>? cryptoList;

  @override
  void initState() {
    super.initState();

    getData();
  }

  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[800],
      body: SafeArea(
        child: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Image(
                image: AssetImage('assets/images/logo.png'),
              ),
              SizedBox(
                height: 100,
              ),
              LoadingAnimationWidget.discreteCircle(color: greenColor, size: 50)
            ],
          ),
        ),
      ),
    );
  }

  Future<void> getData() async {
    
      var response = await Dio().get('https://api.coincap.io/v2/assets');

      List<Crypto> cryptoList = response.data['data']
          .map<Crypto>((jsonMapObject) => Crypto.fromMapJson(jsonMapObject))
          .toList();
    
    
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => CryptoListScreen(
          cryptoList: cryptoList,
        ),
      ),
    );
  }
}
