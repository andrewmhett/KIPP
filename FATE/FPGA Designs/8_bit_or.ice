{
  "version": "1.2",
  "package": {
    "name": "8_bit_or",
    "version": "",
    "description": "",
    "author": "Andrew Hett",
    "image": ""
  },
  "design": {
    "board": "TinyFPGA-BX",
    "graph": {
      "blocks": [
        {
          "id": "56d220a2-c382-4573-ad95-a4d169acffe2",
          "type": "basic.code",
          "data": {
            "code": "assign out = in1 |\n                in2 |\n                in3 |\n                in4 |\n                in5 |\n                in6 |\n                in7 |\n                in8;",
            "params": [],
            "ports": {
              "in": [
                {
                  "name": "in1"
                },
                {
                  "name": "in2"
                },
                {
                  "name": "in3"
                },
                {
                  "name": "in4"
                },
                {
                  "name": "in5"
                },
                {
                  "name": "in6"
                },
                {
                  "name": "in7"
                },
                {
                  "name": "in8"
                }
              ],
              "out": [
                {
                  "name": "out"
                }
              ]
            }
          },
          "position": {
            "x": 344,
            "y": 160
          },
          "size": {
            "width": 384,
            "height": 360
          }
        }
      ],
      "wires": []
    }
  },
  "dependencies": {}
}