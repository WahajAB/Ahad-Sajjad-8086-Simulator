import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';

class DIVMEMTOREG extends StatelessWidget {
  DIVMEMTOREG({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: <Widget>[
          Stack(
            children: <Widget>[
              Container(
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: const AssetImage(''),
                    fit: BoxFit.fill,
                  ),
                ),
                margin: EdgeInsets.fromLTRB(-1496.0, 0.0, -1584.0, 0.0),
              ),
              Container(
                decoration: BoxDecoration(
                  color: const Color(0xffffffff),
                  border:
                      Border.all(width: 1.0, color: const Color(0xff707070)),
                ),
              ),
            ],
          ),
          Align(
            alignment: Alignment(-0.51, 0.435),
            child: SizedBox(
              width: 227.0,
              height: 55.0,
              child: Stack(
                children: <Widget>[
                  Container(
                    color: const Color(0xff032a29),
                  ),
                  Padding(
                    padding: EdgeInsets.fromLTRB(18.0, 8.0, 33.0, 6.0),
                    child: SizedBox.expand(
                        child: Text(
                      'DIV AX,M[5]',
                      style: TextStyle(
                        fontFamily: 'Nunito',
                        fontSize: 30,
                        color: const Color(0xffffffff),
                        fontWeight: FontWeight.w700,
                      ),
                      softWrap: false,
                    )),
                  ),
                ],
              ),
            ),
          ),
          Align(
            alignment: Alignment(-0.329, 0.104),
            child: SizedBox(
              width: 227.0,
              height: 55.0,
              child: Stack(
                children: <Widget>[
                  Container(
                    color: const Color(0xff032a29),
                  ),
                  Padding(
                    padding: EdgeInsets.fromLTRB(18.0, 8.0, 33.0, 6.0),
                    child: SizedBox.expand(
                        child: Text(
                      'DIV AX,M[5]',
                      style: TextStyle(
                        fontFamily: 'Nunito',
                        fontSize: 30,
                        color: const Color(0xffffffff),
                        fontWeight: FontWeight.w700,
                      ),
                      softWrap: false,
                    )),
                  ),
                ],
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 196.0, middle: 0.7613),
            Pin(size: 79.0, end: 118.0),
            child: Stack(
              children: <Widget>[
                Container(
                  color: const Color(0xff072d30),
                ),
                Pinned.fromPins(
                  Pin(start: 21.0, end: 24.0),
                  Pin(size: 46.0, middle: 0.5152),
                  child: Text(
                    'AX / M[5]',
                    style: TextStyle(
                      fontFamily: 'Nunito',
                      fontSize: 34,
                      color: const Color(0xffffffff),
                      fontWeight: FontWeight.w700,
                    ),
                    softWrap: false,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
