{
  "version": "1.2",
  "package": {
    "name": "RAM",
    "version": "",
    "description": "",
    "author": "",
    "image": ""
  },
  "design": {
    "board": "TinyFPGA-BX",
    "graph": {
      "blocks": [
        {
          "id": "787bbfe9-1e82-4665-874f-948373477b89",
          "type": "basic.output",
          "data": {
            "name": "bit1",
            "virtual": false
          },
          "position": {
            "x": 992,
            "y": 160
          }
        },
        {
          "id": "d7435755-3f0d-4fca-8cda-0e464c51a7fe",
          "type": "basic.input",
          "data": {
            "name": "bit1",
            "clock": false,
            "virtual": false
          },
          "position": {
            "x": 264,
            "y": 216
          }
        },
        {
          "id": "6035eba0-5acd-4b34-852a-b36ecf4b06b8",
          "type": "basic.output",
          "data": {
            "name": "bit2",
            "virtual": false
          },
          "position": {
            "x": 992,
            "y": 272
          }
        },
        {
          "id": "b0a590cc-c33b-4157-a41a-9e29ccfe2e0a",
          "type": "basic.input",
          "data": {
            "name": "bit2",
            "clock": false,
            "virtual": false
          },
          "position": {
            "x": 264,
            "y": 288
          }
        },
        {
          "id": "fae51e78-3ae7-494a-a225-243885079818",
          "type": "basic.input",
          "data": {
            "name": "bit3",
            "clock": false,
            "virtual": false
          },
          "position": {
            "x": 264,
            "y": 360
          }
        },
        {
          "id": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f",
          "type": "basic.output",
          "data": {
            "name": "bit3",
            "virtual": false
          },
          "position": {
            "x": 992,
            "y": 376
          }
        },
        {
          "id": "18d1e45c-1ab0-49fb-a691-2a3198b7a214",
          "type": "basic.input",
          "data": {
            "name": "bit4",
            "clock": false,
            "virtual": false
          },
          "position": {
            "x": 264,
            "y": 432
          }
        },
        {
          "id": "27eb76a7-8354-49b9-b1ae-c087b8147866",
          "type": "basic.output",
          "data": {
            "name": "bit4",
            "virtual": false
          },
          "position": {
            "x": 992,
            "y": 488
          }
        },
        {
          "id": "5f813a88-7daf-46fa-92a0-962afb84e05d",
          "type": "basic.input",
          "data": {
            "name": "write",
            "clock": false,
            "virtual": false
          },
          "position": {
            "x": 264,
            "y": 504
          }
        },
        {
          "id": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
          "type": "basic.code",
          "data": {
            "code": "reg ram[4:0];\n\nalways @ (posedge clk)\n    begin\n        if (write) begin\n            ram[0] <= bit1_in;\n            ram[1] <= bit2_in;\n            ram[2] <= bit3_in;\n            ram[3] <= bit4_in;\n        end\nend\n\nassign bit1_out = ram[0];\nassign bit2_out = ram[1];\nassign bit3_out = ram[2];\nassign bit4_out = ram[3];",
            "params": [],
            "ports": {
              "in": [
                {
                  "name": "clk"
                },
                {
                  "name": "bit1_in"
                },
                {
                  "name": "bit2_in"
                },
                {
                  "name": "bit3_in"
                },
                {
                  "name": "bit4_in"
                },
                {
                  "name": "write"
                }
              ],
              "out": [
                {
                  "name": "bit1_out"
                },
                {
                  "name": "bit2_out"
                },
                {
                  "name": "bit3_out"
                },
                {
                  "name": "bit4_out"
                }
              ]
            }
          },
          "position": {
            "x": 416,
            "y": 136
          },
          "size": {
            "width": 512,
            "height": 440
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "d7435755-3f0d-4fca-8cda-0e464c51a7fe",
            "port": "out"
          },
          "target": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit1_in"
          }
        },
        {
          "source": {
            "block": "b0a590cc-c33b-4157-a41a-9e29ccfe2e0a",
            "port": "out"
          },
          "target": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit2_in"
          }
        },
        {
          "source": {
            "block": "fae51e78-3ae7-494a-a225-243885079818",
            "port": "out"
          },
          "target": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit3_in"
          }
        },
        {
          "source": {
            "block": "18d1e45c-1ab0-49fb-a691-2a3198b7a214",
            "port": "out"
          },
          "target": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit4_in"
          }
        },
        {
          "source": {
            "block": "5f813a88-7daf-46fa-92a0-962afb84e05d",
            "port": "out"
          },
          "target": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "write"
          }
        },
        {
          "source": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit1_out"
          },
          "target": {
            "block": "787bbfe9-1e82-4665-874f-948373477b89",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit2_out"
          },
          "target": {
            "block": "6035eba0-5acd-4b34-852a-b36ecf4b06b8",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit3_out"
          },
          "target": {
            "block": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
            "port": "bit4_out"
          },
          "target": {
            "block": "27eb76a7-8354-49b9-b1ae-c087b8147866",
            "port": "in"
          }
        }
      ]
    }
  },
  "dependencies": {}
}