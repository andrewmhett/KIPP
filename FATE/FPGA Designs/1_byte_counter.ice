{
  "version": "1.2",
  "package": {
    "name": "",
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
          "id": "f4293845-b76b-42f0-bda2-1fb1ad0fa786",
          "type": "basic.output",
          "data": {
            "name": "led1",
            "pins": [
              {
                "index": "0",
                "name": "PIN_24",
                "value": "A6"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 1720,
            "y": 0
          }
        },
        {
          "id": "6e84e27d-a45a-4fcf-b9dc-4679e53dd5fa",
          "type": "basic.output",
          "data": {
            "name": "led2",
            "pins": [
              {
                "index": "0",
                "name": "PIN_23",
                "value": "B6"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 1816,
            "y": 40
          }
        },
        {
          "id": "e9ec7e2c-8c30-4b3e-9532-3de6d553b126",
          "type": "basic.output",
          "data": {
            "name": "led3",
            "pins": [
              {
                "index": "0",
                "name": "PIN_22",
                "value": "A7"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 1912,
            "y": 80
          }
        },
        {
          "id": "3726345c-1760-4d51-8709-a2e3da119fea",
          "type": "basic.output",
          "data": {
            "name": "led4",
            "pins": [
              {
                "index": "0",
                "name": "PIN_21",
                "value": "B7"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 2008,
            "y": 120
          }
        },
        {
          "id": "94e7432b-9a58-469e-bff9-dbd47cad98c2",
          "type": "basic.output",
          "data": {
            "name": "seg_B",
            "pins": [
              {
                "index": "0",
                "name": "PIN_5",
                "value": "C1"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 128
          }
        },
        {
          "id": "f4450e6c-df43-4ff7-9f44-75eede98b577",
          "type": "basic.input",
          "data": {
            "name": "button_in",
            "pins": [
              {
                "index": "0",
                "name": "PIN_13",
                "value": "H2"
              }
            ],
            "virtual": false,
            "clock": false
          },
          "position": {
            "x": -256,
            "y": 160
          }
        },
        {
          "id": "e4294d31-d6c7-4cef-985f-ba67d0d3469b",
          "type": "basic.output",
          "data": {
            "name": "led5",
            "pins": [
              {
                "index": "0",
                "name": "PIN_20",
                "value": "A8"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 1720,
            "y": 160
          }
        },
        {
          "id": "dfd12c82-85af-4c23-ba0c-84e47653d815",
          "type": "basic.output",
          "data": {
            "name": "seg_F",
            "pins": [
              {
                "index": "0",
                "name": "PIN_6",
                "value": "D2"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 192
          }
        },
        {
          "id": "65317161-bfd6-45d8-aa23-ffccfcd6c90e",
          "type": "basic.output",
          "data": {
            "name": "led6",
            "pins": [
              {
                "index": "0",
                "name": "PIN_19",
                "value": "B8"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 1816,
            "y": 200
          }
        },
        {
          "id": "c6e8d67f-cdd0-4f73-bf54-df8add6ac54b",
          "type": "basic.output",
          "data": {
            "name": "led7",
            "pins": [
              {
                "index": "0",
                "name": "PIN_18",
                "value": "A9"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 1912,
            "y": 240
          }
        },
        {
          "id": "70e623f9-6f12-4114-977f-41453224af79",
          "type": "basic.output",
          "data": {
            "name": "seg_A",
            "pins": [
              {
                "index": "0",
                "name": "PIN_7",
                "value": "D1"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 256
          }
        },
        {
          "id": "b44f1ddf-e460-4f89-8ebc-bd25c24d831f",
          "type": "basic.output",
          "data": {
            "name": "led8",
            "pins": [
              {
                "index": "0",
                "name": "PIN_17",
                "value": "C9"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 2008,
            "y": 280
          }
        },
        {
          "id": "35bb9139-9402-4c8c-922e-f4b27e406cab",
          "type": "basic.output",
          "data": {
            "name": "seg_G",
            "pins": [
              {
                "index": "0",
                "name": "PIN_8",
                "value": "E2"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 320
          }
        },
        {
          "id": "317a5228-8b79-4bda-8ec0-32a32888ef3e",
          "type": "basic.input",
          "data": {
            "name": "button_in",
            "pins": [
              {
                "index": "0",
                "name": "PIN_12",
                "value": "J1"
              }
            ],
            "virtual": false,
            "clock": false
          },
          "position": {
            "x": -256,
            "y": 336
          }
        },
        {
          "id": "b2381057-8c2f-4993-aa0f-f0d1305222fe",
          "type": "basic.output",
          "data": {
            "name": "seg_C",
            "pins": [
              {
                "index": "0",
                "name": "PIN_9",
                "value": "E1"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 384
          }
        },
        {
          "id": "e9a5d99e-91c8-4ee9-b13b-be213ab95943",
          "type": "basic.output",
          "data": {
            "name": "seg_D",
            "pins": [
              {
                "index": "0",
                "name": "PIN_10",
                "value": "G2"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 448
          }
        },
        {
          "id": "2f6ccd81-e0fe-44f2-908b-6897022f3f79",
          "type": "basic.output",
          "data": {
            "name": "seg_E",
            "pins": [
              {
                "index": "0",
                "name": "PIN_11",
                "value": "H1"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 4752,
            "y": 512
          }
        },
        {
          "id": "298719c4-d636-451e-9c01-ed2e8c13c27d",
          "type": "basic.output",
          "data": {
            "name": "dig1",
            "pins": [
              {
                "index": "0",
                "name": "PIN_4",
                "value": "C2"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 2264,
            "y": 1104
          }
        },
        {
          "id": "6ca17fb3-895a-4047-aae4-56ed82c4bd7d",
          "type": "basic.output",
          "data": {
            "name": "dig2",
            "pins": [
              {
                "index": "0",
                "name": "PIN_3",
                "value": "B1"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 2264,
            "y": 1184
          }
        },
        {
          "id": "20844a07-74ef-4e03-8783-090018ab2a98",
          "type": "basic.output",
          "data": {
            "name": "dig3",
            "pins": [
              {
                "index": "0",
                "name": "PIN_2",
                "value": "A1"
              }
            ],
            "virtual": false
          },
          "position": {
            "x": 2264,
            "y": 1256
          }
        },
        {
          "id": "57cb928e-f99e-4aa1-86ba-1fe2e5be4e3c",
          "type": "basic.constant",
          "data": {
            "name": "div",
            "value": "16",
            "local": false
          },
          "position": {
            "x": 1400,
            "y": 1080
          }
        },
        {
          "id": "392816c0-02bb-4742-9f32-a27d272548bf",
          "type": "bbe640301f15e3846e94b7b003f360bfb828c2e3",
          "position": {
            "x": 1288,
            "y": 8
          },
          "size": {
            "width": 96,
            "height": 320
          }
        },
        {
          "id": "03042326-58e4-4c9d-b073-349e16914732",
          "type": "basic.code",
          "data": {
            "code": "reg last_pos;\ninitial begin\n  last_pos=0;\nend\nassign monostable_out = !last_pos & debounced_in;\nalways @(posedge clk) begin\n  last_pos=debounced_in;\nend",
            "params": [],
            "ports": {
              "in": [
                {
                  "name": "debounced_in"
                },
                {
                  "name": "clk"
                }
              ],
              "out": [
                {
                  "name": "monostable_out"
                }
              ]
            }
          },
          "position": {
            "x": 88,
            "y": 136
          },
          "size": {
            "width": 512,
            "height": 168
          }
        },
        {
          "id": "b185a7d0-b047-43b1-ac3d-4a222b03563d",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -672
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "95623bec-ea76-4bc6-9b11-9daf851a31df",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -624
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1656ac41-02ff-47f0-94e2-12e53b399682",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -608
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1804f7c1-182f-4289-8258-69d715f97459",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -560
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "45fb68f9-cdbb-4b07-a0a2-c6d2d96c9c50",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -544
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "80750bfa-f934-49a5-a614-0f4302e42e5c",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -496
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "fc1067ba-4b45-4775-9c1e-fd7bc712aae2",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -480
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "8a728ff8-1c3e-45f2-bc53-316e351b58cc",
          "type": "cfd9babc26edba88e2152493023c4bef7c47f247",
          "position": {
            "x": -104,
            "y": 144
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f95bbe64-c90c-46e2-b354-f36f1dcdb3ce",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -416
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ad9175b6-e82d-4f30-ad2c-36d40d732eeb",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -432
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "49ce1917-5620-457a-8b30-f5eba727eb90",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -352
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "8a2ab9d1-c180-463f-9c8a-1b3dc02205ba",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -368
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1150007e-811e-447e-81df-a13f4b91aafd",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -288
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "973645e1-5a9a-45ac-9afb-e3ffb212b3d6",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -304
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "4f7e49ed-6f36-4872-9926-7cc46ebfb147",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 872,
            "y": -224
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1d8a3bd6-3411-4508-82a7-9d63a74ddede",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 744,
            "y": -240
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "41465f8b-096b-4214-9362-68369376cb93",
          "type": "basic.code",
          "data": {
            "code": "reg last_pos;\ninitial begin\n  last_pos=0;\nend\nassign monostable_out = !last_pos & debounced_in;\nalways @(posedge clk) begin\n  last_pos=debounced_in;\nend",
            "params": [],
            "ports": {
              "in": [
                {
                  "name": "debounced_in"
                },
                {
                  "name": "clk"
                }
              ],
              "out": [
                {
                  "name": "monostable_out"
                }
              ]
            }
          },
          "position": {
            "x": 88,
            "y": 312
          },
          "size": {
            "width": 512,
            "height": 168
          }
        },
        {
          "id": "0d16eb99-418e-4280-b8ef-38efbc69df4c",
          "type": "cfd9babc26edba88e2152493023c4bef7c47f247",
          "position": {
            "x": -104,
            "y": 320
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f6412e65-0afb-4a04-8e9d-f07e2aa9c3b5",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 432
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ecc27659-a537-4c75-8696-c3574210d148",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 368
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "4028e515-1d1d-4217-bfe5-037f99b65c88",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 304
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f70ceda4-2908-4171-b542-3aa6d3b53363",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 240
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "6d17dd9b-a4a7-462a-8077-2e86723d53be",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 176
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "6c6cfea2-cf38-419b-8880-aca5814e73e0",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 112
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "0ae516ca-536a-4700-9954-7d7a5e08d676",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": 48
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "4f702287-f4e0-4867-ab23-12ddcb8e3307",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": -16
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f29d047f-5bcd-47cc-91ae-627168234e50",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 1128,
            "y": -80
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "c43beef8-5180-4888-a21d-a1944d837a48",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -688
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "30628580-416a-4ac0-a2d6-2c905cd5d24c",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -624
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "5be3f29a-bb0d-4282-b3ff-b612170c371f",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -560
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "4822d1da-0664-4d67-ace9-ae5fd0ace926",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -496
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a624675a-0cdf-495b-b91c-42463384a936",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -432
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "3d798afc-a33f-424e-819d-e2ea0d3a9ccd",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -368
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "3fc7f9c7-0b44-4d51-9298-c169566dd47c",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -304
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "2f9567a8-b41c-47e2-ac62-05022ee5374e",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": -240
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "83b93d29-8c3e-4b85-a6ba-385158a0cfac",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 504
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "5d7be987-4e08-43de-bf0b-0fc6701c0e98",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 632
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "36a4df5d-f4ac-497d-aa3c-b556831aa953",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 760
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "83886452-c9f1-479d-b13e-15b24b6918f6",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 888
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "825d6e2b-98f6-4f53-a3aa-ac71fabdfa44",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 1016
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "5812c7a8-1512-493c-a032-8884dc09b495",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 1144
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f5bd9282-01cd-41de-ad48-c5bca40501fd",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 1000,
            "y": 1272
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a1cf8419-a8be-49eb-8f5a-d9640c63675b",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 992,
            "y": 1400
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "6410abdf-2b47-4a8b-a72e-c41aa8b4632e",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 520
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1aa78aa3-0c9e-4d2b-93b2-6a84a4df6e83",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 584
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "b3e54a1b-6295-4519-8d59-c7ba0aa94a16",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 568
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "4e7c1aeb-5115-47d0-a998-5521a2063a6d",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 648
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ae643328-0f7b-403d-8ae7-5dd5ee082970",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 712
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "16df7145-899d-44f9-b6f3-1fcb71a8cf13",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 696
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "8d40082c-82bd-4ae7-b261-e65736127bd2",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 776
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "368f5c6d-353e-4afc-8da3-c862fd781268",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 840
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "3deb4436-8ed2-41a2-a4a7-e97c57c4544f",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 824
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f00c2f04-6b15-4666-8cc0-f9a1fd574d1e",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 904
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "6ab21d8f-e822-47e0-beaa-c7a519812d4b",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 968
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "7a5f7d49-c663-4b1b-8469-64b8a1b7aa99",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 952
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "dcbc55a7-bdc8-4655-8f71-45222cd09c37",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 1032
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "5fb21faf-b680-4253-9bc5-5e3818ddd170",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 1096
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "010ed9f9-c037-4b2a-bfbf-4de3ee865128",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 1080
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ae35bbac-8bda-46c7-9a18-f6b41c6a9f2b",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 1160
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "deb37e74-38b7-4329-88a9-9d9f586ebc55",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 1224
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "59aa36e7-5ff3-43a5-932a-6d18756ec57a",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 1208
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "611feedd-e6d9-49c1-baae-420a7f46d1d6",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 1288
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "22bee802-0f67-44a2-8464-64741cb8e0ec",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 816,
            "y": 1352
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "2522d25b-e083-455f-91c5-e2c859c3cb78",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 688,
            "y": 1336
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a17de55a-31e3-4db8-bbd7-61a4f397c106",
          "type": "e9ceb27ad69f0785afc607dcd7f0924f517182e9",
          "position": {
            "x": 816,
            "y": 1416
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "8711dd10-c535-49d2-b734-ebc80e47d5d6",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 4624,
            "y": 256
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "988d91e1-ffc0-40e0-bb96-02b83470429d",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 4624,
            "y": 192
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "899ba77e-43cc-466c-a007-d61b92ae2f22",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 4624,
            "y": 128
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "03ada777-2822-4ec8-bd4a-e792d306d56a",
          "type": "basic.code",
          "data": {
            "code": "reg [7:0] binary;\nreg [3:0] hundreds;\nreg [3:0] tens;\nreg [3:0] ones;\ninteger i;\nalways @(posedge clk) begin\n    binary[0] = bit1;\n    binary[1] = bit2;\n    binary[2] = bit3;\n    binary[3] = bit4;\n    binary[4] = bit5;\n    binary[5] = bit6;\n    binary[6] = bit7;\n    binary[7] = bit8;\n    hundreds = 4'd0;\n    tens = 4'd0;\n    ones = 4'd0;\n    for (i =7;i>=0;i=i-1) begin\n        if (hundreds >= 5)\n            hundreds = hundreds + 3;\n        if (tens >= 5)\n            tens = tens + 3;\n        if (ones >= 5)\n            ones = ones + 3;\n        hundreds = hundreds << 1;\n        hundreds[0] = tens[3];\n        tens = tens << 1;\n        tens[0] = ones[3];\n        ones = ones << 1;\n        ones[0] = binary[i];\n    end\nend\nassign hundred_bit1 = hundreds[0];\nassign hundred_bit2 = hundreds[1];\nassign hundred_bit3 = hundreds[2];\nassign hundred_bit4 = hundreds[3];\nassign ten_bit1 = tens[0];\nassign ten_bit2 = tens[1];\nassign ten_bit3 = tens[2];\nassign ten_bit4 = tens[3];\nassign one_bit1 = ones[0];\nassign one_bit2 = ones[1];\nassign one_bit3 = ones[2];\nassign one_bit4 = ones[3];",
            "params": [],
            "ports": {
              "in": [
                {
                  "name": "clk"
                },
                {
                  "name": "bit1"
                },
                {
                  "name": "bit2"
                },
                {
                  "name": "bit3"
                },
                {
                  "name": "bit4"
                },
                {
                  "name": "bit5"
                },
                {
                  "name": "bit6"
                },
                {
                  "name": "bit7"
                },
                {
                  "name": "bit8"
                }
              ],
              "out": [
                {
                  "name": "hundred_bit1"
                },
                {
                  "name": "hundred_bit2"
                },
                {
                  "name": "hundred_bit3"
                },
                {
                  "name": "hundred_bit4"
                },
                {
                  "name": "ten_bit1"
                },
                {
                  "name": "ten_bit2"
                },
                {
                  "name": "ten_bit3"
                },
                {
                  "name": "ten_bit4"
                },
                {
                  "name": "one_bit1"
                },
                {
                  "name": "one_bit2"
                },
                {
                  "name": "one_bit3"
                },
                {
                  "name": "one_bit4"
                }
              ]
            }
          },
          "position": {
            "x": 1512,
            "y": 392
          },
          "size": {
            "width": 528,
            "height": 688
          }
        },
        {
          "id": "9655c907-44da-413b-966b-d9b0cd4b134c",
          "type": "basic.code",
          "data": {
            "code": "integer counter;\nalways @(posedge prescaled_clk) begin\n    dig1 = 0;\n    dig2 = 0;\n    dig3 = 0;\n    if (counter == 0)\n        dig1 = 1;\n    else if (counter == 1)\n        dig2 = 1;\n    else if (counter == 2)\n        dig3 = 1;\n    counter = counter + 1;\n    if (counter == 3)\n        counter=0;\nend",
            "params": [],
            "ports": {
              "in": [
                {
                  "name": "prescaled_clk"
                }
              ],
              "out": [
                {
                  "name": "dig1"
                },
                {
                  "name": "dig2"
                },
                {
                  "name": "dig3"
                }
              ]
            }
          },
          "position": {
            "x": 1592,
            "y": 1096
          },
          "size": {
            "width": 456,
            "height": 232
          }
        },
        {
          "id": "5b95161d-85f5-4daa-bab1-859147af3578",
          "type": "6a50747141af6d1cfb3bb9d0093fb94862ff5a65",
          "position": {
            "x": 1400,
            "y": 1184
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "f375ba83-6565-4d21-ba3a-a86e202dda6e",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 232
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "52e27743-2dd0-4438-a5e2-ef6177a06ccf",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 296
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "da27e5a0-0a1b-462d-ae32-98b0b7c6e80d",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 360
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "847236c0-df93-4d80-ad34-066d1cdf2f6f",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 424
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1cfb435e-8362-43a5-9c70-766d210b744e",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 544
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "b9629145-2704-4cf1-ac11-76c55c732b57",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 608
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "d0c94d23-5bc5-4497-aeb9-f3608e3452c5",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 672
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "d201531e-3a33-4b9f-95f2-a906e0a60d83",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 736
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "bf751ea2-588e-45cf-a2ec-7224feae0df2",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 864
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "8cc58777-e019-486a-ba45-30010633c8cd",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 928
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "433a5bf9-7240-41c7-87e8-c5a868d0cfff",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 992
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "5fae3c52-de8b-426f-b6f6-7abfceeb7eda",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 2440,
            "y": 1056
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "79f63366-253c-439c-9f08-6166e3a1dbcf",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2680,
            "y": 536
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2808,
            "y": 552
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "838d33dc-85fb-4d1a-bb5d-ab2ed7bb49ef",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2680,
            "y": 600
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2808,
            "y": 616
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ac77a40c-4ed7-4ba6-a1ab-19e3378646c3",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2680,
            "y": 664
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "0a65e039-270d-48c6-b811-74b6a6b016e7",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2808,
            "y": 680
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "30a25b91-e71f-43e5-aabb-9ffe6c0e5994",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2680,
            "y": 728
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "da12a310-ff59-48a9-a7f0-1bf96491554e",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 2808,
            "y": 744
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "9d771bac-874a-48b2-86ed-6ad84d166d66",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 112
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "474650d2-594c-4079-abb8-5bc26be274ec",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 176
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "89c882d4-31cc-4378-91ff-a061112f5a58",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 288
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a7c331fd-0f9f-47d7-aaa2-f664d039915e",
          "type": "24496a3459008104b5ea76b1d9ae1f2cca902ed6",
          "position": {
            "x": 3328,
            "y": 320
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "82032572-8122-4437-be66-a26d696a9550",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3328,
            "y": 256
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "51d55c06-52ff-434c-a6e7-5a5986577d09",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 3328,
            "y": 128
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "07e45b85-fb96-4b6f-9480-6fd8bde815ed",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 3328,
            "y": 192
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "eaf98418-3b00-4d67-a5bf-2593d6a8d2d7",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3200,
            "y": 128
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a2564573-de9b-4823-b0a7-1ce6625aee12",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3072,
            "y": 112
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "e9bc0fa9-20b4-43fd-8186-adc68a4803f9",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3200,
            "y": 192
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "b40506f9-105d-439a-9253-c7d66eb57354",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3072,
            "y": 176
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "1c02c663-aae2-4060-a3e2-51420175619a",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 368
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "139949b8-607b-4a96-b3f5-fd6cddec377f",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 3328,
            "y": 384
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "b02c87df-2bea-4778-85da-458e30ad6743",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3200,
            "y": 384
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "b0222d59-09aa-4efa-8882-f75883bfb5d4",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3072,
            "y": 368
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 480
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "6c9012f6-a169-48aa-96cf-2039d66d70fb",
          "type": "24496a3459008104b5ea76b1d9ae1f2cca902ed6",
          "position": {
            "x": 3328,
            "y": 512
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "377c6156-451b-42ad-8f60-9d8e43f2ba74",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3328,
            "y": 448
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4304,
            "y": -544
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4352,
            "y": -288
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4408,
            "y": -32
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "47115719-ec05-4e07-b65f-43145e2d60d8",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4472,
            "y": 224
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "ce1a1603-d1c5-4a6e-942c-694be594b303",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4424,
            "y": 480
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "3ef025a2-4b80-429a-98f6-ed19b9719801",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4376,
            "y": 736
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "dfd79b91-0145-4334-b06c-17e6fb7a2cd9",
          "type": "5f16128c7663e7000ae1ed91dce54fa121050cd9",
          "position": {
            "x": 4328,
            "y": 992
          },
          "size": {
            "width": 96,
            "height": 256
          }
        },
        {
          "id": "d536098f-f290-4f71-bf57-36327528a894",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 608
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "28cac1ac-c964-4210-824e-5913cc672eb3",
          "type": "24496a3459008104b5ea76b1d9ae1f2cca902ed6",
          "position": {
            "x": 3328,
            "y": 640
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "631ae235-3e93-4ba1-a339-58eac344ddae",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3328,
            "y": 576
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "67762aea-95f9-4790-84bf-34e4cc0e218f",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3200,
            "y": 688
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "ca37d9d9-c966-4e3c-8ec5-204cbcbb8908",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3328,
            "y": 704
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "210e6d97-5db4-4d02-813e-2402424acf14",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 3328,
            "y": 768
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a2b88a33-38a2-4b73-a01b-235e88ff5961",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 736
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "c01f4cb3-205f-465f-8b84-5574a817dee2",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 816
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "892b0f78-f1f8-4281-8620-7682bc6e4f46",
          "type": "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139",
          "position": {
            "x": 3328,
            "y": 832
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "58986953-5a1a-4663-8b42-91d4870460ce",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3200,
            "y": 832
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "a1881dc6-00ba-41e3-92f6-e4130f9dae9c",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 3072,
            "y": 816
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "577f849f-52d6-47a2-9160-282d332d7c02",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 928
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "df2c554b-d5f9-48ea-9b58-d975e85e3c10",
          "type": "24496a3459008104b5ea76b1d9ae1f2cca902ed6",
          "position": {
            "x": 3328,
            "y": 960
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "aab0179d-b7b1-4bbd-aac9-a031004ad47c",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3328,
            "y": 896
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "890e08f8-8003-4942-82ac-7bbca9ca66e0",
          "type": "24496a3459008104b5ea76b1d9ae1f2cca902ed6",
          "position": {
            "x": 3328,
            "y": 1024
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "fae20f7d-8059-46de-9501-7085491c87bf",
          "type": "24496a3459008104b5ea76b1d9ae1f2cca902ed6",
          "position": {
            "x": 3328,
            "y": 1088
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
          "type": "7ebc902cbb1c4db116741533a86182485900ecda",
          "position": {
            "x": 3456,
            "y": 1056
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "242a953c-69a0-4ae9-a5ae-713e0ed39418",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 4624,
            "y": 384
          },
          "size": {
            "width": 96,
            "height": 64
          }
        },
        {
          "id": "d741616a-0988-4a62-9ec4-84d92169402d",
          "type": "528969443d4d498610fee60503f6bdebb087af5e",
          "position": {
            "x": 4624,
            "y": 16
          },
          "size": {
            "width": 96,
            "height": 64
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "787bbfe9-1e82-4665-874f-948373477b89"
          },
          "target": {
            "block": "f4293845-b76b-42f0-bda2-1fb1ad0fa786",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "6035eba0-5acd-4b34-852a-b36ecf4b06b8"
          },
          "target": {
            "block": "6e84e27d-a45a-4fcf-b9dc-4679e53dd5fa",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f"
          },
          "target": {
            "block": "e9ec7e2c-8c30-4b3e-9532-3de6d553b126",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "787bbfe9-1e82-4665-874f-948373477b89"
          },
          "target": {
            "block": "b185a7d0-b047-43b1-ac3d-4a222b03563d",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "b185a7d0-b047-43b1-ac3d-4a222b03563d",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "787bbfe9-1e82-4665-874f-948373477b89"
          },
          "target": {
            "block": "95623bec-ea76-4bc6-9b11-9daf851a31df",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "95623bec-ea76-4bc6-9b11-9daf851a31df",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "95623bec-ea76-4bc6-9b11-9daf851a31df",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1656ac41-02ff-47f0-94e2-12e53b399682",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "6035eba0-5acd-4b34-852a-b36ecf4b06b8"
          },
          "target": {
            "block": "1656ac41-02ff-47f0-94e2-12e53b399682",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "95623bec-ea76-4bc6-9b11-9daf851a31df",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1804f7c1-182f-4289-8258-69d715f97459",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "6035eba0-5acd-4b34-852a-b36ecf4b06b8"
          },
          "target": {
            "block": "1804f7c1-182f-4289-8258-69d715f97459",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "1804f7c1-182f-4289-8258-69d715f97459",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "45fb68f9-cdbb-4b07-a0a2-c6d2d96c9c50",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f"
          },
          "target": {
            "block": "45fb68f9-cdbb-4b07-a0a2-c6d2d96c9c50",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "1804f7c1-182f-4289-8258-69d715f97459",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "80750bfa-f934-49a5-a614-0f4302e42e5c",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f"
          },
          "target": {
            "block": "80750bfa-f934-49a5-a614-0f4302e42e5c",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "80750bfa-f934-49a5-a614-0f4302e42e5c",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "fc1067ba-4b45-4775-9c1e-fd7bc712aae2",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "27eb76a7-8354-49b9-b1ae-c087b8147866"
          },
          "target": {
            "block": "fc1067ba-4b45-4775-9c1e-fd7bc712aae2",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "f4450e6c-df43-4ff7-9f44-75eede98b577",
            "port": "out"
          },
          "target": {
            "block": "8a728ff8-1c3e-45f2-bc53-316e351b58cc",
            "port": "c9e1af2a-6f09-4cf6-a5b3-fdf7ec2c6530"
          }
        },
        {
          "source": {
            "block": "ad9175b6-e82d-4f30-ad2c-36d40d732eeb",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f95bbe64-c90c-46e2-b354-f36f1dcdb3ce",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "8a2ab9d1-c180-463f-9c8a-1b3dc02205ba",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "49ce1917-5620-457a-8b30-f5eba727eb90",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "973645e1-5a9a-45ac-9afb-e3ffb212b3d6",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1150007e-811e-447e-81df-a13f4b91aafd",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "1d8a3bd6-3411-4508-82a7-9d63a74ddede",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4f7e49ed-6f36-4872-9926-7cc46ebfb147",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5"
          },
          "target": {
            "block": "f95bbe64-c90c-46e2-b354-f36f1dcdb3ce",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "597f2698-469c-4ee0-901d-b6cdbea789c2"
          },
          "target": {
            "block": "49ce1917-5620-457a-8b30-f5eba727eb90",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "506848a8-90d0-44f9-ad22-25d922af1bb7"
          },
          "target": {
            "block": "1150007e-811e-447e-81df-a13f4b91aafd",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "b0b76e6f-c437-4af7-8657-de8de965513c"
          },
          "target": {
            "block": "4f7e49ed-6f36-4872-9926-7cc46ebfb147",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "27eb76a7-8354-49b9-b1ae-c087b8147866"
          },
          "target": {
            "block": "ad9175b6-e82d-4f30-ad2c-36d40d732eeb",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "80750bfa-f934-49a5-a614-0f4302e42e5c",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ad9175b6-e82d-4f30-ad2c-36d40d732eeb",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ad9175b6-e82d-4f30-ad2c-36d40d732eeb",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "8a2ab9d1-c180-463f-9c8a-1b3dc02205ba",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "8a2ab9d1-c180-463f-9c8a-1b3dc02205ba",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "973645e1-5a9a-45ac-9afb-e3ffb212b3d6",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "973645e1-5a9a-45ac-9afb-e3ffb212b3d6",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1d8a3bd6-3411-4508-82a7-9d63a74ddede",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5"
          },
          "target": {
            "block": "8a2ab9d1-c180-463f-9c8a-1b3dc02205ba",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "597f2698-469c-4ee0-901d-b6cdbea789c2"
          },
          "target": {
            "block": "973645e1-5a9a-45ac-9afb-e3ffb212b3d6",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "506848a8-90d0-44f9-ad22-25d922af1bb7"
          },
          "target": {
            "block": "1d8a3bd6-3411-4508-82a7-9d63a74ddede",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5"
          },
          "target": {
            "block": "e4294d31-d6c7-4cef-985f-ba67d0d3469b",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "597f2698-469c-4ee0-901d-b6cdbea789c2"
          },
          "target": {
            "block": "65317161-bfd6-45d8-aa23-ffccfcd6c90e",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "506848a8-90d0-44f9-ad22-25d922af1bb7"
          },
          "target": {
            "block": "c6e8d67f-cdd0-4f73-bf54-df8add6ac54b",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "b0b76e6f-c437-4af7-8657-de8de965513c"
          },
          "target": {
            "block": "b44f1ddf-e460-4f89-8ebc-bd25c24d831f",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "27eb76a7-8354-49b9-b1ae-c087b8147866"
          },
          "target": {
            "block": "3726345c-1760-4d51-8709-a2e3da119fea",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "8a728ff8-1c3e-45f2-bc53-316e351b58cc",
            "port": "22ff3fa1-943b-4d1a-bd89-36e1c054d077"
          },
          "target": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "debounced_in"
          }
        },
        {
          "source": {
            "block": "0d16eb99-418e-4280-b8ef-38efbc69df4c",
            "port": "22ff3fa1-943b-4d1a-bd89-36e1c054d077"
          },
          "target": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "debounced_in"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "317a5228-8b79-4bda-8ec0-32a32888ef3e",
            "port": "out"
          },
          "target": {
            "block": "0d16eb99-418e-4280-b8ef-38efbc69df4c",
            "port": "c9e1af2a-6f09-4cf6-a5b3-fdf7ec2c6530"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "f6412e65-0afb-4a04-8e9d-f07e2aa9c3b5",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "f6412e65-0afb-4a04-8e9d-f07e2aa9c3b5",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "f6412e65-0afb-4a04-8e9d-f07e2aa9c3b5",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "5f813a88-7daf-46fa-92a0-962afb84e05d"
          }
        },
        {
          "source": {
            "block": "ecc27659-a537-4c75-8696-c3574210d148",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "34cdafa5-5f88-4d70-9b0f-08648d0f10bf"
          }
        },
        {
          "source": {
            "block": "4028e515-1d1d-4217-bfe5-037f99b65c88",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "33e38e36-6560-456d-98b1-d5fb6c6b76db"
          }
        },
        {
          "source": {
            "block": "f70ceda4-2908-4171-b542-3aa6d3b53363",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4f090c3a-649e-4155-840b-a893133102aa"
          }
        },
        {
          "source": {
            "block": "6d17dd9b-a4a7-462a-8077-2e86723d53be",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "cfc15446-4cc7-4379-bfab-767d7555dc48"
          }
        },
        {
          "source": {
            "block": "6c6cfea2-cf38-419b-8880-aca5814e73e0",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "18d1e45c-1ab0-49fb-a691-2a3198b7a214"
          }
        },
        {
          "source": {
            "block": "0ae516ca-536a-4700-9954-7d7a5e08d676",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fae51e78-3ae7-494a-a225-243885079818"
          }
        },
        {
          "source": {
            "block": "4f702287-f4e0-4867-ab23-12ddcb8e3307",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "b0a590cc-c33b-4157-a41a-9e29ccfe2e0a"
          }
        },
        {
          "source": {
            "block": "f29d047f-5bcd-47cc-91ae-627168234e50",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "d7435755-3f0d-4fca-8cda-0e464c51a7fe"
          }
        },
        {
          "source": {
            "block": "b185a7d0-b047-43b1-ac3d-4a222b03563d",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "c43beef8-5180-4888-a21d-a1944d837a48",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "1656ac41-02ff-47f0-94e2-12e53b399682",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "30628580-416a-4ac0-a2d6-2c905cd5d24c",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "45fb68f9-cdbb-4b07-a0a2-c6d2d96c9c50",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "5be3f29a-bb0d-4282-b3ff-b612170c371f",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "fc1067ba-4b45-4775-9c1e-fd7bc712aae2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4822d1da-0664-4d67-ace9-ae5fd0ace926",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "f95bbe64-c90c-46e2-b354-f36f1dcdb3ce",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a624675a-0cdf-495b-b91c-42463384a936",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "49ce1917-5620-457a-8b30-f5eba727eb90",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3d798afc-a33f-424e-819d-e2ea0d3a9ccd",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "1150007e-811e-447e-81df-a13f4b91aafd",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3fc7f9c7-0b44-4d51-9298-c169566dd47c",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "4f7e49ed-6f36-4872-9926-7cc46ebfb147",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2f9567a8-b41c-47e2-ac62-05022ee5374e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "30628580-416a-4ac0-a2d6-2c905cd5d24c",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "5be3f29a-bb0d-4282-b3ff-b612170c371f",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "4822d1da-0664-4d67-ace9-ae5fd0ace926",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": [
            {
              "x": 984,
              "y": -528
            }
          ]
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "a624675a-0cdf-495b-b91c-42463384a936",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "3d798afc-a33f-424e-819d-e2ea0d3a9ccd",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "3fc7f9c7-0b44-4d51-9298-c169566dd47c",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "2f9567a8-b41c-47e2-ac62-05022ee5374e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03042326-58e4-4c9d-b073-349e16914732",
            "port": "monostable_out"
          },
          "target": {
            "block": "c43beef8-5180-4888-a21d-a1944d837a48",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "c43beef8-5180-4888-a21d-a1944d837a48",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f29d047f-5bcd-47cc-91ae-627168234e50",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "30628580-416a-4ac0-a2d6-2c905cd5d24c",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4f702287-f4e0-4867-ab23-12ddcb8e3307",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "5be3f29a-bb0d-4282-b3ff-b612170c371f",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "0ae516ca-536a-4700-9954-7d7a5e08d676",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "4822d1da-0664-4d67-ace9-ae5fd0ace926",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6c6cfea2-cf38-419b-8880-aca5814e73e0",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "a624675a-0cdf-495b-b91c-42463384a936",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6d17dd9b-a4a7-462a-8077-2e86723d53be",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "3d798afc-a33f-424e-819d-e2ea0d3a9ccd",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f70ceda4-2908-4171-b542-3aa6d3b53363",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "3fc7f9c7-0b44-4d51-9298-c169566dd47c",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4028e515-1d1d-4217-bfe5-037f99b65c88",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "2f9567a8-b41c-47e2-ac62-05022ee5374e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ecc27659-a537-4c75-8696-c3574210d148",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "83b93d29-8c3e-4b85-a6ba-385158a0cfac",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f29d047f-5bcd-47cc-91ae-627168234e50",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "5d7be987-4e08-43de-bf0b-0fc6701c0e98",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4f702287-f4e0-4867-ab23-12ddcb8e3307",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "36a4df5d-f4ac-497d-aa3c-b556831aa953",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "0ae516ca-536a-4700-9954-7d7a5e08d676",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "83886452-c9f1-479d-b13e-15b24b6918f6",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6c6cfea2-cf38-419b-8880-aca5814e73e0",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "825d6e2b-98f6-4f53-a3aa-ac71fabdfa44",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6d17dd9b-a4a7-462a-8077-2e86723d53be",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "5812c7a8-1512-493c-a032-8884dc09b495",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f70ceda4-2908-4171-b542-3aa6d3b53363",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "f5bd9282-01cd-41de-ad48-c5bca40501fd",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4028e515-1d1d-4217-bfe5-037f99b65c88",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "a1cf8419-a8be-49eb-8f5a-d9640c63675b",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ecc27659-a537-4c75-8696-c3574210d148",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "83b93d29-8c3e-4b85-a6ba-385158a0cfac",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "5d7be987-4e08-43de-bf0b-0fc6701c0e98",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "36a4df5d-f4ac-497d-aa3c-b556831aa953",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "83886452-c9f1-479d-b13e-15b24b6918f6",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "825d6e2b-98f6-4f53-a3aa-ac71fabdfa44",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "5812c7a8-1512-493c-a032-8884dc09b495",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "f5bd9282-01cd-41de-ad48-c5bca40501fd",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "a1cf8419-a8be-49eb-8f5a-d9640c63675b",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "b3e54a1b-6295-4519-8d59-c7ba0aa94a16",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1aa78aa3-0c9e-4d2b-93b2-6a84a4df6e83",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "1aa78aa3-0c9e-4d2b-93b2-6a84a4df6e83",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "41465f8b-096b-4214-9362-68369376cb93",
            "port": "monostable_out"
          },
          "target": {
            "block": "6410abdf-2b47-4a8b-a72e-c41aa8b4632e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "787bbfe9-1e82-4665-874f-948373477b89"
          },
          "target": {
            "block": "6410abdf-2b47-4a8b-a72e-c41aa8b4632e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "787bbfe9-1e82-4665-874f-948373477b89"
          },
          "target": {
            "block": "b3e54a1b-6295-4519-8d59-c7ba0aa94a16",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "6410abdf-2b47-4a8b-a72e-c41aa8b4632e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "83b93d29-8c3e-4b85-a6ba-385158a0cfac",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "16df7145-899d-44f9-b6f3-1fcb71a8cf13",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ae643328-0f7b-403d-8ae7-5dd5ee082970",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "4e7c1aeb-5115-47d0-a998-5521a2063a6d",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "5d7be987-4e08-43de-bf0b-0fc6701c0e98",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "6035eba0-5acd-4b34-852a-b36ecf4b06b8"
          },
          "target": {
            "block": "16df7145-899d-44f9-b6f3-1fcb71a8cf13",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "6035eba0-5acd-4b34-852a-b36ecf4b06b8"
          },
          "target": {
            "block": "4e7c1aeb-5115-47d0-a998-5521a2063a6d",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "1aa78aa3-0c9e-4d2b-93b2-6a84a4df6e83",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ae643328-0f7b-403d-8ae7-5dd5ee082970",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "1aa78aa3-0c9e-4d2b-93b2-6a84a4df6e83",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "4e7c1aeb-5115-47d0-a998-5521a2063a6d",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "3deb4436-8ed2-41a2-a4a7-e97c57c4544f",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "368f5c6d-353e-4afc-8da3-c862fd781268",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f"
          },
          "target": {
            "block": "3deb4436-8ed2-41a2-a4a7-e97c57c4544f",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f"
          },
          "target": {
            "block": "8d40082c-82bd-4ae7-b261-e65736127bd2",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ae643328-0f7b-403d-8ae7-5dd5ee082970",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "368f5c6d-353e-4afc-8da3-c862fd781268",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "ae643328-0f7b-403d-8ae7-5dd5ee082970",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "8d40082c-82bd-4ae7-b261-e65736127bd2",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "8d40082c-82bd-4ae7-b261-e65736127bd2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "36a4df5d-f4ac-497d-aa3c-b556831aa953",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "7a5f7d49-c663-4b1b-8469-64b8a1b7aa99",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6ab21d8f-e822-47e0-beaa-c7a519812d4b",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "27eb76a7-8354-49b9-b1ae-c087b8147866"
          },
          "target": {
            "block": "7a5f7d49-c663-4b1b-8469-64b8a1b7aa99",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "27eb76a7-8354-49b9-b1ae-c087b8147866"
          },
          "target": {
            "block": "f00c2f04-6b15-4666-8cc0-f9a1fd574d1e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "368f5c6d-353e-4afc-8da3-c862fd781268",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6ab21d8f-e822-47e0-beaa-c7a519812d4b",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "368f5c6d-353e-4afc-8da3-c862fd781268",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f00c2f04-6b15-4666-8cc0-f9a1fd574d1e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "f00c2f04-6b15-4666-8cc0-f9a1fd574d1e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "83886452-c9f1-479d-b13e-15b24b6918f6",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "010ed9f9-c037-4b2a-bfbf-4de3ee865128",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "5fb21faf-b680-4253-9bc5-5e3818ddd170",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5"
          },
          "target": {
            "block": "010ed9f9-c037-4b2a-bfbf-4de3ee865128",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5"
          },
          "target": {
            "block": "dcbc55a7-bdc8-4655-8f71-45222cd09c37",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "6ab21d8f-e822-47e0-beaa-c7a519812d4b",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "5fb21faf-b680-4253-9bc5-5e3818ddd170",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "6ab21d8f-e822-47e0-beaa-c7a519812d4b",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "dcbc55a7-bdc8-4655-8f71-45222cd09c37",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "dcbc55a7-bdc8-4655-8f71-45222cd09c37",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "825d6e2b-98f6-4f53-a3aa-ac71fabdfa44",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "59aa36e7-5ff3-43a5-932a-6d18756ec57a",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "deb37e74-38b7-4329-88a9-9d9f586ebc55",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "597f2698-469c-4ee0-901d-b6cdbea789c2"
          },
          "target": {
            "block": "59aa36e7-5ff3-43a5-932a-6d18756ec57a",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "597f2698-469c-4ee0-901d-b6cdbea789c2"
          },
          "target": {
            "block": "ae35bbac-8bda-46c7-9a18-f6b41c6a9f2b",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "5fb21faf-b680-4253-9bc5-5e3818ddd170",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "deb37e74-38b7-4329-88a9-9d9f586ebc55",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "5fb21faf-b680-4253-9bc5-5e3818ddd170",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ae35bbac-8bda-46c7-9a18-f6b41c6a9f2b",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "ae35bbac-8bda-46c7-9a18-f6b41c6a9f2b",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "5812c7a8-1512-493c-a032-8884dc09b495",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "2522d25b-e083-455f-91c5-e2c859c3cb78",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "22bee802-0f67-44a2-8464-64741cb8e0ec",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "506848a8-90d0-44f9-ad22-25d922af1bb7"
          },
          "target": {
            "block": "2522d25b-e083-455f-91c5-e2c859c3cb78",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "506848a8-90d0-44f9-ad22-25d922af1bb7"
          },
          "target": {
            "block": "611feedd-e6d9-49c1-baae-420a7f46d1d6",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "deb37e74-38b7-4329-88a9-9d9f586ebc55",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "22bee802-0f67-44a2-8464-64741cb8e0ec",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "deb37e74-38b7-4329-88a9-9d9f586ebc55",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "611feedd-e6d9-49c1-baae-420a7f46d1d6",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "611feedd-e6d9-49c1-baae-420a7f46d1d6",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "f5bd9282-01cd-41de-ad48-c5bca40501fd",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "b0b76e6f-c437-4af7-8657-de8de965513c"
          },
          "target": {
            "block": "a17de55a-31e3-4db8-bbd7-61a4f397c106",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "22bee802-0f67-44a2-8464-64741cb8e0ec",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a17de55a-31e3-4db8-bbd7-61a4f397c106",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "a17de55a-31e3-4db8-bbd7-61a4f397c106",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a1cf8419-a8be-49eb-8f5a-d9640c63675b",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "8711dd10-c535-49d2-b734-ebc80e47d5d6",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "70e623f9-6f12-4114-977f-41453224af79",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "988d91e1-ffc0-40e0-bb96-02b83470429d",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "dfd12c82-85af-4c23-ba0c-84e47653d815",
            "port": "in"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "899ba77e-43cc-466c-a007-d61b92ae2f22",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "94e7432b-9a58-469e-bff9-dbd47cad98c2",
            "port": "in"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "787bbfe9-1e82-4665-874f-948373477b89"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit1"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "6035eba0-5acd-4b34-852a-b36ecf4b06b8"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit2"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit3"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "27eb76a7-8354-49b9-b1ae-c087b8147866"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit4"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit5"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "597f2698-469c-4ee0-901d-b6cdbea789c2"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit6"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "506848a8-90d0-44f9-ad22-25d922af1bb7"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit7"
          }
        },
        {
          "source": {
            "block": "392816c0-02bb-4742-9f32-a27d272548bf",
            "port": "b0b76e6f-c437-4af7-8657-de8de965513c"
          },
          "target": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "bit8"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig1"
          },
          "target": {
            "block": "298719c4-d636-451e-9c01-ed2e8c13c27d",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig2"
          },
          "target": {
            "block": "6ca17fb3-895a-4047-aae4-56ed82c4bd7d",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig3"
          },
          "target": {
            "block": "20844a07-74ef-4e03-8783-090018ab2a98",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "5b95161d-85f5-4daa-bab1-859147af3578",
            "port": "7e07d449-6475-4839-b43e-8aead8be2aac"
          },
          "target": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "prescaled_clk"
          }
        },
        {
          "source": {
            "block": "57cb928e-f99e-4aa1-86ba-1fe2e5be4e3c",
            "port": "constant-out"
          },
          "target": {
            "block": "5b95161d-85f5-4daa-bab1-859147af3578",
            "port": "de2d8a2d-7908-48a2-9e35-7763a45886e4"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig1"
          },
          "target": {
            "block": "f375ba83-6565-4d21-ba3a-a86e202dda6e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig1"
          },
          "target": {
            "block": "52e27743-2dd0-4438-a5e2-ef6177a06ccf",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig1"
          },
          "target": {
            "block": "da27e5a0-0a1b-462d-ae32-98b0b7c6e80d",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig1"
          },
          "target": {
            "block": "847236c0-df93-4d80-ad34-066d1cdf2f6f",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "hundred_bit1"
          },
          "target": {
            "block": "f375ba83-6565-4d21-ba3a-a86e202dda6e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "hundred_bit2"
          },
          "target": {
            "block": "52e27743-2dd0-4438-a5e2-ef6177a06ccf",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "hundred_bit3"
          },
          "target": {
            "block": "da27e5a0-0a1b-462d-ae32-98b0b7c6e80d",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "hundred_bit4"
          },
          "target": {
            "block": "847236c0-df93-4d80-ad34-066d1cdf2f6f",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig2"
          },
          "target": {
            "block": "1cfb435e-8362-43a5-9c70-766d210b744e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig2"
          },
          "target": {
            "block": "b9629145-2704-4cf1-ac11-76c55c732b57",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig2"
          },
          "target": {
            "block": "d0c94d23-5bc5-4497-aeb9-f3608e3452c5",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig2"
          },
          "target": {
            "block": "d201531e-3a33-4b9f-95f2-a906e0a60d83",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig3"
          },
          "target": {
            "block": "bf751ea2-588e-45cf-a2ec-7224feae0df2",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig3"
          },
          "target": {
            "block": "8cc58777-e019-486a-ba45-30010633c8cd",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig3"
          },
          "target": {
            "block": "433a5bf9-7240-41c7-87e8-c5a868d0cfff",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "9655c907-44da-413b-966b-d9b0cd4b134c",
            "port": "dig3"
          },
          "target": {
            "block": "5fae3c52-de8b-426f-b6f6-7abfceeb7eda",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "ten_bit1"
          },
          "target": {
            "block": "1cfb435e-8362-43a5-9c70-766d210b744e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "ten_bit2"
          },
          "target": {
            "block": "b9629145-2704-4cf1-ac11-76c55c732b57",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "ten_bit3"
          },
          "target": {
            "block": "d0c94d23-5bc5-4497-aeb9-f3608e3452c5",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "ten_bit4"
          },
          "target": {
            "block": "d201531e-3a33-4b9f-95f2-a906e0a60d83",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "one_bit1"
          },
          "target": {
            "block": "bf751ea2-588e-45cf-a2ec-7224feae0df2",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "one_bit2"
          },
          "target": {
            "block": "8cc58777-e019-486a-ba45-30010633c8cd",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "one_bit3"
          },
          "target": {
            "block": "433a5bf9-7240-41c7-87e8-c5a868d0cfff",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03ada777-2822-4ec8-bd4a-e792d306d56a",
            "port": "one_bit4"
          },
          "target": {
            "block": "5fae3c52-de8b-426f-b6f6-7abfceeb7eda",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "79f63366-253c-439c-9f08-6166e3a1dbcf",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "f375ba83-6565-4d21-ba3a-a86e202dda6e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "79f63366-253c-439c-9f08-6166e3a1dbcf",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "1cfb435e-8362-43a5-9c70-766d210b744e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "79f63366-253c-439c-9f08-6166e3a1dbcf",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "bf751ea2-588e-45cf-a2ec-7224feae0df2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "838d33dc-85fb-4d1a-bb5d-ab2ed7bb49ef",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "ac77a40c-4ed7-4ba6-a1ab-19e3378646c3",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "52e27743-2dd0-4438-a5e2-ef6177a06ccf",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "838d33dc-85fb-4d1a-bb5d-ab2ed7bb49ef",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "b9629145-2704-4cf1-ac11-76c55c732b57",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "838d33dc-85fb-4d1a-bb5d-ab2ed7bb49ef",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "8cc58777-e019-486a-ba45-30010633c8cd",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "da27e5a0-0a1b-462d-ae32-98b0b7c6e80d",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ac77a40c-4ed7-4ba6-a1ab-19e3378646c3",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "d0c94d23-5bc5-4497-aeb9-f3608e3452c5",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ac77a40c-4ed7-4ba6-a1ab-19e3378646c3",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "433a5bf9-7240-41c7-87e8-c5a868d0cfff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "30a25b91-e71f-43e5-aabb-9ffe6c0e5994",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "847236c0-df93-4d80-ad34-066d1cdf2f6f",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "30a25b91-e71f-43e5-aabb-9ffe6c0e5994",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "d201531e-3a33-4b9f-95f2-a906e0a60d83",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "30a25b91-e71f-43e5-aabb-9ffe6c0e5994",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "5fae3c52-de8b-426f-b6f6-7abfceeb7eda",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "9d771bac-874a-48b2-86ed-6ad84d166d66",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "a7c331fd-0f9f-47d7-aaa2-f664d039915e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a7c331fd-0f9f-47d7-aaa2-f664d039915e",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a7c331fd-0f9f-47d7-aaa2-f664d039915e",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "82032572-8122-4437-be66-a26d696a9550",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "82032572-8122-4437-be66-a26d696a9550",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "82032572-8122-4437-be66-a26d696a9550",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "a2564573-de9b-4823-b0a7-1ce6625aee12",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eaf98418-3b00-4d67-a5bf-2593d6a8d2d7",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a2564573-de9b-4823-b0a7-1ce6625aee12",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a2564573-de9b-4823-b0a7-1ce6625aee12",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eaf98418-3b00-4d67-a5bf-2593d6a8d2d7",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "eaf98418-3b00-4d67-a5bf-2593d6a8d2d7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "51d55c06-52ff-434c-a6e7-5a5986577d09",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "b40506f9-105d-439a-9253-c7d66eb57354",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "e9bc0fa9-20b4-43fd-8186-adc68a4803f9",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b40506f9-105d-439a-9253-c7d66eb57354",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b40506f9-105d-439a-9253-c7d66eb57354",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "e9bc0fa9-20b4-43fd-8186-adc68a4803f9",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "e9bc0fa9-20b4-43fd-8186-adc68a4803f9",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "07e45b85-fb96-4b6f-9480-6fd8bde815ed",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "b02c87df-2bea-4778-85da-458e30ad6743",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "139949b8-607b-4a96-b3f5-fd6cddec377f",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "b0222d59-09aa-4efa-8882-f75883bfb5d4",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b02c87df-2bea-4778-85da-458e30ad6743",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b0222d59-09aa-4efa-8882-f75883bfb5d4",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b0222d59-09aa-4efa-8882-f75883bfb5d4",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b02c87df-2bea-4778-85da-458e30ad6743",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1c02c663-aae2-4060-a3e2-51420175619a",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "139949b8-607b-4a96-b3f5-fd6cddec377f",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "1c02c663-aae2-4060-a3e2-51420175619a",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "07e45b85-fb96-4b6f-9480-6fd8bde815ed",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "51d55c06-52ff-434c-a6e7-5a5986577d09",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "9d771bac-874a-48b2-86ed-6ad84d166d66",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "6c9012f6-a169-48aa-96cf-2039d66d70fb",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "377c6156-451b-42ad-8f60-9d8e43f2ba74",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "377c6156-451b-42ad-8f60-9d8e43f2ba74",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "377c6156-451b-42ad-8f60-9d8e43f2ba74",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6c9012f6-a169-48aa-96cf-2039d66d70fb",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "6c9012f6-a169-48aa-96cf-2039d66d70fb",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "899ba77e-43cc-466c-a007-d61b92ae2f22",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "988d91e1-ffc0-40e0-bb96-02b83470429d",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "35bb9139-9402-4c8c-922e-f4b27e406cab",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "e9a5d99e-91c8-4ee9-b13b-be213ab95943",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "dfd79b91-0145-4334-b06c-17e6fb7a2cd9",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "2f6ccd81-e0fe-44f2-908b-6897022f3f79",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "9d771bac-874a-48b2-86ed-6ad84d166d66",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          },
          "vertices": [
            {
              "x": 4304,
              "y": 72
            }
          ]
        },
        {
          "source": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "9d771bac-874a-48b2-86ed-6ad84d166d66",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          }
        },
        {
          "source": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          }
        },
        {
          "source": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "dfd79b91-0145-4334-b06c-17e6fb7a2cd9",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          }
        },
        {
          "source": {
            "block": "474650d2-594c-4079-abb8-5bc26be274ec",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          }
        },
        {
          "source": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          }
        },
        {
          "source": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "1c02c663-aae2-4060-a3e2-51420175619a",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "08a84b3f-1f40-47f8-bfe9-42d5076ee854"
          }
        },
        {
          "source": {
            "block": "1c02c663-aae2-4060-a3e2-51420175619a",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "1c02c663-aae2-4060-a3e2-51420175619a",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "1c02c663-aae2-4060-a3e2-51420175619a",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "80f65afd-1f6d-4577-93ee-252b5aa97bd2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "28cac1ac-c964-4210-824e-5913cc672eb3",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "631ae235-3e93-4ba1-a339-58eac344ddae",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "631ae235-3e93-4ba1-a339-58eac344ddae",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "631ae235-3e93-4ba1-a339-58eac344ddae",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "28cac1ac-c964-4210-824e-5913cc672eb3",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "28cac1ac-c964-4210-824e-5913cc672eb3",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "d93abc14-5898-4612-974e-f8263f29c2a1"
          }
        },
        {
          "source": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "dfd79b91-0145-4334-b06c-17e6fb7a2cd9",
            "port": "d6809ced-7be5-4c95-aad0-2956065685ad"
          }
        },
        {
          "source": {
            "block": "d536098f-f290-4f71-bf57-36327528a894",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "67762aea-95f9-4790-84bf-34e4cc0e218f",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ca37d9d9-c966-4e3c-8ec5-204cbcbb8908",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ca37d9d9-c966-4e3c-8ec5-204cbcbb8908",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a2b88a33-38a2-4b73-a01b-235e88ff5961",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "210e6d97-5db4-4d02-813e-2402424acf14",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a2b88a33-38a2-4b73-a01b-235e88ff5961",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "67762aea-95f9-4790-84bf-34e4cc0e218f",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "67762aea-95f9-4790-84bf-34e4cc0e218f",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ca37d9d9-c966-4e3c-8ec5-204cbcbb8908",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "210e6d97-5db4-4d02-813e-2402424acf14",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "a2b88a33-38a2-4b73-a01b-235e88ff5961",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "d93abc14-5898-4612-974e-f8263f29c2a1"
          }
        },
        {
          "source": {
            "block": "a2b88a33-38a2-4b73-a01b-235e88ff5961",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "d93abc14-5898-4612-974e-f8263f29c2a1"
          }
        },
        {
          "source": {
            "block": "a2b88a33-38a2-4b73-a01b-235e88ff5961",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "d93abc14-5898-4612-974e-f8263f29c2a1"
          }
        },
        {
          "source": {
            "block": "892b0f78-f1f8-4281-8620-7682bc6e4f46",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "58986953-5a1a-4663-8b42-91d4870460ce",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "892b0f78-f1f8-4281-8620-7682bc6e4f46",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "a1881dc6-00ba-41e3-92f6-e4130f9dae9c",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "58986953-5a1a-4663-8b42-91d4870460ce",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a1881dc6-00ba-41e3-92f6-e4130f9dae9c",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "a1881dc6-00ba-41e3-92f6-e4130f9dae9c",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "58986953-5a1a-4663-8b42-91d4870460ce",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "50a666c1-adbc-4ec5-9f11-c36f9e937464"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "50a666c1-adbc-4ec5-9f11-c36f9e937464"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "50a666c1-adbc-4ec5-9f11-c36f9e937464"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "50a666c1-adbc-4ec5-9f11-c36f9e937464"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "d93abc14-5898-4612-974e-f8263f29c2a1"
          }
        },
        {
          "source": {
            "block": "c01f4cb3-205f-465f-8b84-5574a817dee2",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "dfd79b91-0145-4334-b06c-17e6fb7a2cd9",
            "port": "ae2df21b-88ae-429b-ab7c-45a4aafd940d"
          }
        },
        {
          "source": {
            "block": "df2c554b-d5f9-48ea-9b58-d975e85e3c10",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "aab0179d-b7b1-4bbd-aac9-a031004ad47c",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          },
          "vertices": []
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "aab0179d-b7b1-4bbd-aac9-a031004ad47c",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "aab0179d-b7b1-4bbd-aac9-a031004ad47c",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "df2c554b-d5f9-48ea-9b58-d975e85e3c10",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "df2c554b-d5f9-48ea-9b58-d975e85e3c10",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "50a666c1-adbc-4ec5-9f11-c36f9e937464"
          }
        },
        {
          "source": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "5e7526f0-d99a-4a19-862a-4558ea6f7268"
          }
        },
        {
          "source": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "47115719-ec05-4e07-b65f-43145e2d60d8",
            "port": "5e7526f0-d99a-4a19-862a-4558ea6f7268"
          }
        },
        {
          "source": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "5e7526f0-d99a-4a19-862a-4558ea6f7268"
          }
        },
        {
          "source": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "d93abc14-5898-4612-974e-f8263f29c2a1"
          }
        },
        {
          "source": {
            "block": "577f849f-52d6-47a2-9160-282d332d7c02",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "5e7526f0-d99a-4a19-862a-4558ea6f7268"
          }
        },
        {
          "source": {
            "block": "89c882d4-31cc-4378-91ff-a061112f5a58",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "6aab3758-eddc-46e5-95ba-0886bef5a348"
          }
        },
        {
          "source": {
            "block": "6432a768-0e6b-49d4-95a7-f55ce5743fe8",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "890e08f8-8003-4942-82ac-7bbca9ca66e0",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "ed7ca501-cb2f-4d9e-853e-1831ea8f6a43",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "890e08f8-8003-4942-82ac-7bbca9ca66e0",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "0a65e039-270d-48c6-b811-74b6a6b016e7",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "fae20f7d-8059-46de-9501-7085491c87bf",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "da12a310-ff59-48a9-a7f0-1bf96491554e",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "fae20f7d-8059-46de-9501-7085491c87bf",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "890e08f8-8003-4942-82ac-7bbca9ca66e0",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "fae20f7d-8059-46de-9501-7085491c87bf",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "dfd79b91-0145-4334-b06c-17e6fb7a2cd9",
            "port": "8cb094c7-ee62-4322-bd47-84d3344d026f"
          }
        },
        {
          "source": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "3ef025a2-4b80-429a-98f6-ed19b9719801",
            "port": "6aab3758-eddc-46e5-95ba-0886bef5a348"
          }
        },
        {
          "source": {
            "block": "242a953c-69a0-4ae9-a5ae-713e0ed39418",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "b2381057-8c2f-4993-aa0f-f0d1305222fe",
            "port": "in"
          }
        },
        {
          "source": {
            "block": "ce1a1603-d1c5-4a6e-942c-694be594b303",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "242a953c-69a0-4ae9-a5ae-713e0ed39418",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "242a953c-69a0-4ae9-a5ae-713e0ed39418",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "d741616a-0988-4a62-9ec4-84d92169402d",
            "port": "97b51945-d716-4b6c-9db9-970d08541249"
          }
        },
        {
          "source": {
            "block": "eca3ec02-5dbd-41a4-86e6-8276b842fbdc",
            "port": "c5959df0-0392-454a-8e63-55cbcf9f3308"
          },
          "target": {
            "block": "d741616a-0988-4a62-9ec4-84d92169402d",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "d741616a-0988-4a62-9ec4-84d92169402d",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "8711dd10-c535-49d2-b734-ebc80e47d5d6",
            "port": "18c2ebc7-5152-439c-9b3f-851c59bac834"
          }
        },
        {
          "source": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "03a5f59a-725f-42d0-9cdf-256e193dcb11",
            "port": "6aab3758-eddc-46e5-95ba-0886bef5a348"
          }
        },
        {
          "source": {
            "block": "7f5124b2-3ff0-44b6-b9d8-e3e20f9fa9ff",
            "port": "664caf9e-5f40-4df4-800a-b626af702e62"
          },
          "target": {
            "block": "2bc5835a-aea4-408e-b8c3-d8837b5d7fe6",
            "port": "6aab3758-eddc-46e5-95ba-0886bef5a348"
          }
        }
      ]
    }
  },
  "dependencies": {
    "bbe640301f15e3846e94b7b003f360bfb828c2e3": {
      "package": {
        "name": "RAM",
        "version": "",
        "description": "",
        "author": "",
        "image": ""
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "751bbe47-dbaa-40aa-92a6-4b938f1df11a",
              "type": "basic.input",
              "data": {
                "name": "clk",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": false,
                "clock": true
              },
              "position": {
                "x": 264,
                "y": 144
              }
            },
            {
              "id": "787bbfe9-1e82-4665-874f-948373477b89",
              "type": "basic.output",
              "data": {
                "name": "bit1"
              },
              "position": {
                "x": 1088,
                "y": 152
              }
            },
            {
              "id": "d7435755-3f0d-4fca-8cda-0e464c51a7fe",
              "type": "basic.input",
              "data": {
                "name": "bit1",
                "clock": false
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
                "name": "bit2"
              },
              "position": {
                "x": 1088,
                "y": 240
              }
            },
            {
              "id": "b0a590cc-c33b-4157-a41a-9e29ccfe2e0a",
              "type": "basic.input",
              "data": {
                "name": "bit2",
                "clock": false
              },
              "position": {
                "x": 264,
                "y": 288
              }
            },
            {
              "id": "fdb3f970-d3de-47ff-a6ab-649ca519ea2f",
              "type": "basic.output",
              "data": {
                "name": "bit3"
              },
              "position": {
                "x": 1088,
                "y": 328
              }
            },
            {
              "id": "fae51e78-3ae7-494a-a225-243885079818",
              "type": "basic.input",
              "data": {
                "name": "bit3",
                "clock": false
              },
              "position": {
                "x": 264,
                "y": 360
              }
            },
            {
              "id": "27eb76a7-8354-49b9-b1ae-c087b8147866",
              "type": "basic.output",
              "data": {
                "name": "bit4"
              },
              "position": {
                "x": 1088,
                "y": 424
              }
            },
            {
              "id": "18d1e45c-1ab0-49fb-a691-2a3198b7a214",
              "type": "basic.input",
              "data": {
                "name": "bit4",
                "clock": false
              },
              "position": {
                "x": 264,
                "y": 432
              }
            },
            {
              "id": "cfc15446-4cc7-4379-bfab-767d7555dc48",
              "type": "basic.input",
              "data": {
                "name": "bit5",
                "clock": false,
                "virtual": false
              },
              "position": {
                "x": 264,
                "y": 504
              }
            },
            {
              "id": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5",
              "type": "basic.output",
              "data": {
                "name": "bit5",
                "virtual": false
              },
              "position": {
                "x": 1088,
                "y": 512
              }
            },
            {
              "id": "4f090c3a-649e-4155-840b-a893133102aa",
              "type": "basic.input",
              "data": {
                "name": "bit6",
                "clock": false,
                "virtual": false
              },
              "position": {
                "x": 264,
                "y": 576
              }
            },
            {
              "id": "597f2698-469c-4ee0-901d-b6cdbea789c2",
              "type": "basic.output",
              "data": {
                "name": "bit6",
                "virtual": false
              },
              "position": {
                "x": 1088,
                "y": 608
              }
            },
            {
              "id": "33e38e36-6560-456d-98b1-d5fb6c6b76db",
              "type": "basic.input",
              "data": {
                "name": "bit7",
                "clock": false,
                "virtual": false
              },
              "position": {
                "x": 264,
                "y": 648
              }
            },
            {
              "id": "506848a8-90d0-44f9-ad22-25d922af1bb7",
              "type": "basic.output",
              "data": {
                "name": "bit7",
                "virtual": false
              },
              "position": {
                "x": 1088,
                "y": 696
              }
            },
            {
              "id": "34cdafa5-5f88-4d70-9b0f-08648d0f10bf",
              "type": "basic.input",
              "data": {
                "name": "bit8",
                "clock": false,
                "virtual": false
              },
              "position": {
                "x": 264,
                "y": 720
              }
            },
            {
              "id": "b0b76e6f-c437-4af7-8657-de8de965513c",
              "type": "basic.output",
              "data": {
                "name": "bit8",
                "virtual": false
              },
              "position": {
                "x": 1088,
                "y": 784
              }
            },
            {
              "id": "5f813a88-7daf-46fa-92a0-962afb84e05d",
              "type": "basic.input",
              "data": {
                "name": "write",
                "clock": false
              },
              "position": {
                "x": 264,
                "y": 792
              }
            },
            {
              "id": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
              "type": "basic.code",
              "data": {
                "code": "reg ram[8:0];\nreg i;\n\ninitial\n    begin\n        for (i=0;i<8;i++) begin\n            ram[i] = 1'b0;\n        end\nend\n\nalways @ (posedge clk)\n    begin\n        if (write) begin\n            ram[0] <= bit1_in;\n            ram[1] <= bit2_in;\n            ram[2] <= bit3_in;\n            ram[3] <= bit4_in;\n            ram[4] <= bit5_in;\n            ram[5] <= bit6_in;\n            ram[6] <= bit7_in;\n            ram[7] <= bit8_in;\n        end\nend\n\nassign bit1_out = ram[0];\nassign bit2_out = ram[1];\nassign bit3_out = ram[2];\nassign bit4_out = ram[3];\nassign bit5_out = ram[4];\nassign bit6_out = ram[5];\nassign bit7_out = ram[6];\nassign bit8_out = ram[7];",
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
                      "name": "bit5_in"
                    },
                    {
                      "name": "bit6_in"
                    },
                    {
                      "name": "bit7_in"
                    },
                    {
                      "name": "bit8_in"
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
                    },
                    {
                      "name": "bit5_out"
                    },
                    {
                      "name": "bit6_out"
                    },
                    {
                      "name": "bit7_out"
                    },
                    {
                      "name": "bit8_out"
                    }
                  ]
                }
              },
              "position": {
                "x": 416,
                "y": 136
              },
              "size": {
                "width": 608,
                "height": 728
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
            },
            {
              "source": {
                "block": "751bbe47-dbaa-40aa-92a6-4b938f1df11a",
                "port": "out"
              },
              "target": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "clk"
              }
            },
            {
              "source": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit5_out"
              },
              "target": {
                "block": "4d0b5883-95bd-4284-ad67-b8f0ce0841b5",
                "port": "in"
              }
            },
            {
              "source": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit6_out"
              },
              "target": {
                "block": "597f2698-469c-4ee0-901d-b6cdbea789c2",
                "port": "in"
              }
            },
            {
              "source": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit7_out"
              },
              "target": {
                "block": "506848a8-90d0-44f9-ad22-25d922af1bb7",
                "port": "in"
              }
            },
            {
              "source": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit8_out"
              },
              "target": {
                "block": "b0b76e6f-c437-4af7-8657-de8de965513c",
                "port": "in"
              }
            },
            {
              "source": {
                "block": "cfc15446-4cc7-4379-bfab-767d7555dc48",
                "port": "out"
              },
              "target": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit5_in"
              }
            },
            {
              "source": {
                "block": "4f090c3a-649e-4155-840b-a893133102aa",
                "port": "out"
              },
              "target": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit6_in"
              }
            },
            {
              "source": {
                "block": "33e38e36-6560-456d-98b1-d5fb6c6b76db",
                "port": "out"
              },
              "target": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit7_in"
              }
            },
            {
              "source": {
                "block": "34cdafa5-5f88-4d70-9b0f-08648d0f10bf",
                "port": "out"
              },
              "target": {
                "block": "3b06e2e7-4af0-45ac-925e-585209bbd4a4",
                "port": "bit8_in"
              }
            }
          ]
        }
      }
    },
    "e9ceb27ad69f0785afc607dcd7f0924f517182e9": {
      "package": {
        "name": "XOR",
        "version": "1.0.0",
        "description": "XOR logic gate",
        "author": "Carlos Diaz",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%22-252%20400.9%2090%2040%22%3E%3Cpath%20d=%22M-252%20409.9h26v2h-26zM-252%20429.9h27v2h-27zM-186.5%20419.9h24.5v2h-24.5z%22/%3E%3Cpath%20d=%22M-184.6%20420.9c0-1-.6-2-.6-2-10.3-17.8-26-18-30.6-18H-233l2%202.4s5.7%207%205.7%2017.6c0%2010.6-5.7%2017.6-5.7%2017.6l-2%202.4h17.2c2.4%200%207.7%200%2013.6-2.4%205.7-2.3%2012-6.9%2017-15.7.1%200%20.6-1%20.6-1.9zm-18.9%2014.8c-5.4%202.2-9.8%202.2-12.3%202.2H-227c1.9-3.1%204.8-9%204.8-17s-2.9-13.9-4.8-17h11.3c4.7%200%2018.3-.1%2028%2017-4.8%208.4-10.6%2012.7-15.8%2014.8z%22/%3E%3Cpath%20d=%22M-238.3%20440.9h3.6c2.3-3.7%206.5-11.6%206.5-19.8%200-8.5-4.4-16.5-6.8-20.2h-3.6c1.4%202%207.4%2011%207.4%2020.2%200%208.9-5.7%2017.7-7.1%2019.8z%22/%3E%3C/svg%3E"
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "18c2ebc7-5152-439c-9b3f-851c59bac834",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 80
              }
            },
            {
              "id": "664caf9e-5f40-4df4-800a-b626af702e62",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 752,
                "y": 144
              }
            },
            {
              "id": "97b51945-d716-4b6c-9db9-970d08541249",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 208
              }
            },
            {
              "id": "00925b04-5004-4307-a737-fa4e97c8b6ab",
              "type": "basic.code",
              "data": {
                "code": "// XOR logic gate\n\nassign c = a ^ b;",
                "params": [],
                "ports": {
                  "in": [
                    {
                      "name": "a"
                    },
                    {
                      "name": "b"
                    }
                  ],
                  "out": [
                    {
                      "name": "c"
                    }
                  ]
                }
              },
              "position": {
                "x": 256,
                "y": 48
              },
              "size": {
                "width": 384,
                "height": 256
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "18c2ebc7-5152-439c-9b3f-851c59bac834",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "a"
              }
            },
            {
              "source": {
                "block": "97b51945-d716-4b6c-9db9-970d08541249",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "b"
              }
            },
            {
              "source": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "c"
              },
              "target": {
                "block": "664caf9e-5f40-4df4-800a-b626af702e62",
                "port": "in"
              }
            }
          ]
        }
      }
    },
    "7ebc902cbb1c4db116741533a86182485900ecda": {
      "package": {
        "name": "AND",
        "version": "1.0.0",
        "description": "AND logic gate",
        "author": "Jesús Arroyo",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%22-252%20400.9%2090%2040%22%3E%3Cpath%20d=%22M-252%20409.9h26v2h-26zM-252%20429.9h27v2h-27z%22/%3E%3Cpath%20d=%22M-227%20400.9v39.9h20.4c11.3%200%2020-9%2020-20s-8.7-20-20-20H-227zm2.9%202.8h17.6c9.8%200%2016.7%207.6%2016.7%2017.1%200%209.5-7.4%2017.1-17.1%2017.1H-224c-.1.1-.1-34.2-.1-34.2z%22/%3E%3Cpath%20d=%22M-187.911%20419.9H-162v2h-25.911z%22/%3E%3C/svg%3E"
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "18c2ebc7-5152-439c-9b3f-851c59bac834",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 80
              }
            },
            {
              "id": "664caf9e-5f40-4df4-800a-b626af702e62",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 752,
                "y": 144
              }
            },
            {
              "id": "97b51945-d716-4b6c-9db9-970d08541249",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 208
              }
            },
            {
              "id": "00925b04-5004-4307-a737-fa4e97c8b6ab",
              "type": "basic.code",
              "data": {
                "code": "// AND logic gate\n\nassign c = a & b;",
                "params": [],
                "ports": {
                  "in": [
                    {
                      "name": "a"
                    },
                    {
                      "name": "b"
                    }
                  ],
                  "out": [
                    {
                      "name": "c"
                    }
                  ]
                }
              },
              "position": {
                "x": 256,
                "y": 48
              },
              "size": {
                "width": 384,
                "height": 256
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "18c2ebc7-5152-439c-9b3f-851c59bac834",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "a"
              }
            },
            {
              "source": {
                "block": "97b51945-d716-4b6c-9db9-970d08541249",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "b"
              }
            },
            {
              "source": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "c"
              },
              "target": {
                "block": "664caf9e-5f40-4df4-800a-b626af702e62",
                "port": "in"
              }
            }
          ]
        }
      }
    },
    "cfd9babc26edba88e2152493023c4bef7c47f247": {
      "package": {
        "name": "Debouncer",
        "version": "1.0.0",
        "description": "Remove the rebound on a mechanical switch",
        "author": "Juan González",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%22-252%20400.9%2090%2040%22%3E%3Cpath%20d=%22M-251.547%20436.672h22.802v-30.353h5.862v30.353h5.259v-30.353h3.447v30.353h2.984v-30.353h3.506v30.523h6.406V405.77h38.868%22%20fill=%22none%22%20stroke=%22#000%22%20stroke-width=%221.4%22%20stroke-linecap=%22round%22%20stroke-linejoin=%22round%22/%3E%3Cpath%20d=%22M-232.57%20403.877l26.946%2032.391M-205.624%20403.877l-26.946%2032.391%22%20fill=%22none%22%20stroke=%22red%22%20stroke-width=%223%22%20stroke-linecap=%22round%22/%3E%3C/svg%3E"
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "4bf41c17-a2da-4140-95f7-2a80d51b1e1a",
              "type": "basic.input",
              "data": {
                "name": "",
                "clock": true
              },
              "position": {
                "x": 48,
                "y": 144
              }
            },
            {
              "id": "22ff3fa1-943b-4d1a-bd89-36e1c054d077",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 768,
                "y": 208
              }
            },
            {
              "id": "c9e1af2a-6f09-4cf6-a5b3-fdf7ec2c6530",
              "type": "basic.input",
              "data": {
                "name": "",
                "clock": false
              },
              "position": {
                "x": 48,
                "y": 272
              }
            },
            {
              "id": "92490e7e-c3ba-4e9c-a917-2a771d99f1ef",
              "type": "basic.code",
              "data": {
                "code": "//-- Debouncer Circuit\n//-- It produces a stable output when the\n//-- input signal is bouncing\n\nreg btn_prev = 0;\nreg btn_out_r = 0;\n\nreg [16:0] counter = 0;\n\n\nalways @(posedge clk) begin\n\n  //-- If btn_prev and btn_in are differents\n  if (btn_prev ^ in == 1'b1) begin\n    \n      //-- Reset the counter\n      counter <= 0;\n      \n      //-- Capture the button status\n      btn_prev <= in;\n  end\n    \n  //-- If no timeout, increase the counter\n  else if (counter[16] == 1'b0)\n      counter <= counter + 1;\n      \n  else\n    //-- Set the output to the stable value\n    btn_out_r <= btn_prev;\n\nend\n\nassign out = btn_out_r;\n",
                "params": [],
                "ports": {
                  "in": [
                    {
                      "name": "clk"
                    },
                    {
                      "name": "in"
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
                "x": 264,
                "y": 112
              },
              "size": {
                "width": 384,
                "height": 256
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "92490e7e-c3ba-4e9c-a917-2a771d99f1ef",
                "port": "out"
              },
              "target": {
                "block": "22ff3fa1-943b-4d1a-bd89-36e1c054d077",
                "port": "in"
              }
            },
            {
              "source": {
                "block": "4bf41c17-a2da-4140-95f7-2a80d51b1e1a",
                "port": "out"
              },
              "target": {
                "block": "92490e7e-c3ba-4e9c-a917-2a771d99f1ef",
                "port": "clk"
              }
            },
            {
              "source": {
                "block": "c9e1af2a-6f09-4cf6-a5b3-fdf7ec2c6530",
                "port": "out"
              },
              "target": {
                "block": "92490e7e-c3ba-4e9c-a917-2a771d99f1ef",
                "port": "in"
              }
            }
          ]
        }
      }
    },
    "528969443d4d498610fee60503f6bdebb087af5e": {
      "package": {
        "name": "OR",
        "version": "1.0.0",
        "description": "OR logic gate",
        "author": "Jesús Arroyo",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%2290%22%20height=%2240%22%20version=%221%22%3E%3Cpath%20d=%22M65%2020h25M26%2010H0M27%2030H0%22%20fill=%22none%22%20stroke=%22#000%22%20stroke-width=%222%22/%3E%3Cpath%20d=%22M19.094%200l2%202.438s5.656%207%205.656%2017.562c0%2010.562-5.656%2017.563-5.656%2017.563l-2%202.437H36.25c2.408%200%207.69.025%2013.625-2.406s12.537-7.344%2017.688-16.875L66.25%2020l1.313-.719C57.258.216%2041.007%200%2036.25%200H19.094zm5.875%203H36.25c4.684%200%2018.287-.13%2027.969%2017-4.767%208.43-10.522%2012.684-15.719%2014.813C43.14%2037.008%2038.658%2037%2036.25%2037H25c1.874-3.108%204.75-9.05%204.75-17%200-7.973-2.909-13.9-4.781-17z%22%20fill-rule=%22evenodd%22/%3E%3C/svg%3E"
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "18c2ebc7-5152-439c-9b3f-851c59bac834",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 80
              }
            },
            {
              "id": "664caf9e-5f40-4df4-800a-b626af702e62",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 752,
                "y": 144
              }
            },
            {
              "id": "97b51945-d716-4b6c-9db9-970d08541249",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 208
              }
            },
            {
              "id": "00925b04-5004-4307-a737-fa4e97c8b6ab",
              "type": "basic.code",
              "data": {
                "code": "// OR logic gate\n\nassign c = a | b;",
                "params": [],
                "ports": {
                  "in": [
                    {
                      "name": "a"
                    },
                    {
                      "name": "b"
                    }
                  ],
                  "out": [
                    {
                      "name": "c"
                    }
                  ]
                }
              },
              "position": {
                "x": 256,
                "y": 48
              },
              "size": {
                "width": 384,
                "height": 256
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "18c2ebc7-5152-439c-9b3f-851c59bac834",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "a"
              }
            },
            {
              "source": {
                "block": "97b51945-d716-4b6c-9db9-970d08541249",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "b"
              }
            },
            {
              "source": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "c"
              },
              "target": {
                "block": "664caf9e-5f40-4df4-800a-b626af702e62",
                "port": "in"
              }
            }
          ]
        }
      }
    },
    "96f0988f8164f7c1b216c8ee122d6ce3cf6bc139": {
      "package": {
        "name": "NOT",
        "version": "1.0.0",
        "description": "NOT logic gate",
        "author": "Jesús Arroyo",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%2291.33%22%20height=%2245.752%22%20version=%221%22%3E%3Cpath%20d=%22M0%2020.446h27v2H0zM70.322%2020.447h15.3v2h-15.3z%22/%3E%3Cpath%20d=%22M66.05%2026.746c-2.9%200-5.3-2.4-5.3-5.3s2.4-5.3%205.3-5.3%205.3%202.4%205.3%205.3-2.4%205.3-5.3%205.3zm0-8.6c-1.8%200-3.3%201.5-3.3%203.3%200%201.8%201.5%203.3%203.3%203.3%201.8%200%203.3-1.5%203.3-3.3%200-1.8-1.5-3.3-3.3-3.3z%22/%3E%3Cpath%20d=%22M25.962%202.563l33.624%2018.883L25.962%2040.33V2.563z%22%20fill=%22none%22%20stroke=%22#000%22%20stroke-width=%223%22/%3E%3C/svg%3E"
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "18c2ebc7-5152-439c-9b3f-851c59bac834",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 144
              }
            },
            {
              "id": "664caf9e-5f40-4df4-800a-b626af702e62",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 752,
                "y": 144
              }
            },
            {
              "id": "5365ed8c-e5db-4445-938f-8d689830ea5c",
              "type": "basic.code",
              "data": {
                "code": "// NOT logic gate\n\nassign c = ~ a;",
                "params": [],
                "ports": {
                  "in": [
                    {
                      "name": "a"
                    }
                  ],
                  "out": [
                    {
                      "name": "c"
                    }
                  ]
                }
              },
              "position": {
                "x": 256,
                "y": 48
              },
              "size": {
                "width": 384,
                "height": 256
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "18c2ebc7-5152-439c-9b3f-851c59bac834",
                "port": "out"
              },
              "target": {
                "block": "5365ed8c-e5db-4445-938f-8d689830ea5c",
                "port": "a"
              }
            },
            {
              "source": {
                "block": "5365ed8c-e5db-4445-938f-8d689830ea5c",
                "port": "c"
              },
              "target": {
                "block": "664caf9e-5f40-4df4-800a-b626af702e62",
                "port": "in"
              }
            }
          ]
        }
      }
    },
    "6a50747141af6d1cfb3bb9d0093fb94862ff5a65": {
      "package": {
        "name": "PrescalerN",
        "version": "0.1",
        "description": "Parametric N-bits prescaler",
        "author": "Juan Gonzalez (Obijuan)",
        "image": ""
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "e19c6f2f-5747-4ed1-87c8-748575f0cc10",
              "type": "basic.input",
              "data": {
                "name": "",
                "clock": true
              },
              "position": {
                "x": 0,
                "y": 256
              }
            },
            {
              "id": "7e07d449-6475-4839-b43e-8aead8be2aac",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 720,
                "y": 256
              }
            },
            {
              "id": "de2d8a2d-7908-48a2-9e35-7763a45886e4",
              "type": "basic.constant",
              "data": {
                "name": "N",
                "value": "22",
                "local": false
              },
              "position": {
                "x": 352,
                "y": 56
              }
            },
            {
              "id": "2330955f-5ce6-4d1c-8ee4-0a09a0349389",
              "type": "basic.code",
              "data": {
                "code": "//-- Number of bits of the prescaler\n//parameter N = 22;\n\n//-- divisor register\nreg [N-1:0] divcounter;\n\n//-- N bit counter\nalways @(posedge clk_in)\n  divcounter <= divcounter + 1;\n\n//-- Use the most significant bit as output\nassign clk_out = divcounter[N-1];",
                "params": [
                  {
                    "name": "N"
                  }
                ],
                "ports": {
                  "in": [
                    {
                      "name": "clk_in"
                    }
                  ],
                  "out": [
                    {
                      "name": "clk_out"
                    }
                  ]
                }
              },
              "position": {
                "x": 176,
                "y": 176
              },
              "size": {
                "width": 448,
                "height": 224
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "2330955f-5ce6-4d1c-8ee4-0a09a0349389",
                "port": "clk_out"
              },
              "target": {
                "block": "7e07d449-6475-4839-b43e-8aead8be2aac",
                "port": "in"
              }
            },
            {
              "source": {
                "block": "e19c6f2f-5747-4ed1-87c8-748575f0cc10",
                "port": "out"
              },
              "target": {
                "block": "2330955f-5ce6-4d1c-8ee4-0a09a0349389",
                "port": "clk_in"
              }
            },
            {
              "source": {
                "block": "de2d8a2d-7908-48a2-9e35-7763a45886e4",
                "port": "constant-out"
              },
              "target": {
                "block": "2330955f-5ce6-4d1c-8ee4-0a09a0349389",
                "port": "N"
              }
            }
          ]
        }
      }
    },
    "24496a3459008104b5ea76b1d9ae1f2cca902ed6": {
      "package": {
        "name": "NOR",
        "version": "1.0.0",
        "description": "NOR logic gate",
        "author": "Carlos Diaz",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%22-252%20400.9%2090%2040%22%3E%3Cpath%20d=%22M-252%20409.9h26v2h-26zM-252%20429.9h27v2h-27zM-177.3%20419.9h15.3v2h-15.3z%22/%3E%3Cpath%20d=%22M-181.4%20426.2c-2.9%200-5.3-2.4-5.3-5.3s2.4-5.3%205.3-5.3%205.3%202.4%205.3%205.3-2.4%205.3-5.3%205.3zm0-8.6c-1.8%200-3.3%201.5-3.3%203.3%200%201.8%201.5%203.3%203.3%203.3s3.3-1.5%203.3-3.3c0-1.8-1.5-3.3-3.3-3.3z%22/%3E%3Cpath%20d=%22M-185.3%20422.6l-.3-2.1.4-1.6c-10.3-17.8-26-18-30.6-18H-233l2%202.4s5.7%207%205.7%2017.6c0%2010.6-5.7%2017.6-5.7%2017.6l-2%202.4h17.2c2.4%200%207.7%200%2013.6-2.4%205.7-2.3%2012-6.9%2017-15.7l-.1-.2zm-18.2%2013.1c-5.4%202.2-9.8%202.2-12.3%202.2H-227c1.9-3.1%204.8-9%204.8-17s-2.9-13.9-4.8-17h11.3c4.7%200%2018.3-.1%2028%2017-4.8%208.4-10.6%2012.7-15.8%2014.8z%22/%3E%3C/svg%3E"
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "18c2ebc7-5152-439c-9b3f-851c59bac834",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 80
              }
            },
            {
              "id": "664caf9e-5f40-4df4-800a-b626af702e62",
              "type": "basic.output",
              "data": {
                "name": ""
              },
              "position": {
                "x": 752,
                "y": 144
              }
            },
            {
              "id": "97b51945-d716-4b6c-9db9-970d08541249",
              "type": "basic.input",
              "data": {
                "name": ""
              },
              "position": {
                "x": 64,
                "y": 208
              }
            },
            {
              "id": "00925b04-5004-4307-a737-fa4e97c8b6ab",
              "type": "basic.code",
              "data": {
                "code": "// NOR logic gate\n\nassign c = ~(a | b);",
                "params": [],
                "ports": {
                  "in": [
                    {
                      "name": "a"
                    },
                    {
                      "name": "b"
                    }
                  ],
                  "out": [
                    {
                      "name": "c"
                    }
                  ]
                }
              },
              "position": {
                "x": 256,
                "y": 48
              },
              "size": {
                "width": 384,
                "height": 256
              }
            }
          ],
          "wires": [
            {
              "source": {
                "block": "18c2ebc7-5152-439c-9b3f-851c59bac834",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "a"
              }
            },
            {
              "source": {
                "block": "97b51945-d716-4b6c-9db9-970d08541249",
                "port": "out"
              },
              "target": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "b"
              }
            },
            {
              "source": {
                "block": "00925b04-5004-4307-a737-fa4e97c8b6ab",
                "port": "c"
              },
              "target": {
                "block": "664caf9e-5f40-4df4-800a-b626af702e62",
                "port": "in"
              }
            }
          ]
        }
      }
    },
    "5f16128c7663e7000ae1ed91dce54fa121050cd9": {
      "package": {
        "name": "8_bit_or",
        "version": "",
        "description": "",
        "author": "Andrew Hett",
        "image": ""
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "08a84b3f-1f40-47f8-bfe9-42d5076ee854",
              "type": "basic.input",
              "data": {
                "name": "bit1",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": false,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 152
              }
            },
            {
              "id": "d6809ced-7be5-4c95-aad0-2956065685ad",
              "type": "basic.input",
              "data": {
                "name": "bit2",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 192
              }
            },
            {
              "id": "ae2df21b-88ae-429b-ab7c-45a4aafd940d",
              "type": "basic.input",
              "data": {
                "name": "bit3",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 232
              }
            },
            {
              "id": "8cb094c7-ee62-4322-bd47-84d3344d026f",
              "type": "basic.input",
              "data": {
                "name": "bit4",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 272
              }
            },
            {
              "id": "c5959df0-0392-454a-8e63-55cbcf9f3308",
              "type": "basic.output",
              "data": {
                "name": "out",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true
              },
              "position": {
                "x": 776,
                "y": 312
              }
            },
            {
              "id": "d93abc14-5898-4612-974e-f8263f29c2a1",
              "type": "basic.input",
              "data": {
                "name": "bit5",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 344
              }
            },
            {
              "id": "50a666c1-adbc-4ec5-9f11-c36f9e937464",
              "type": "basic.input",
              "data": {
                "name": "bit6",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 384
              }
            },
            {
              "id": "5e7526f0-d99a-4a19-862a-4558ea6f7268",
              "type": "basic.input",
              "data": {
                "name": "bit7",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 424
              }
            },
            {
              "id": "6aab3758-eddc-46e5-95ba-0886bef5a348",
              "type": "basic.input",
              "data": {
                "name": "bit8",
                "pins": [
                  {
                    "index": "0",
                    "name": "",
                    "value": ""
                  }
                ],
                "virtual": true,
                "clock": false
              },
              "position": {
                "x": 192,
                "y": 464
              }
            },
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
          "wires": [
            {
              "source": {
                "block": "08a84b3f-1f40-47f8-bfe9-42d5076ee854",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in1"
              }
            },
            {
              "source": {
                "block": "d6809ced-7be5-4c95-aad0-2956065685ad",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in2"
              }
            },
            {
              "source": {
                "block": "ae2df21b-88ae-429b-ab7c-45a4aafd940d",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in3"
              }
            },
            {
              "source": {
                "block": "8cb094c7-ee62-4322-bd47-84d3344d026f",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in4"
              }
            },
            {
              "source": {
                "block": "d93abc14-5898-4612-974e-f8263f29c2a1",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in5"
              }
            },
            {
              "source": {
                "block": "50a666c1-adbc-4ec5-9f11-c36f9e937464",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in6"
              }
            },
            {
              "source": {
                "block": "5e7526f0-d99a-4a19-862a-4558ea6f7268",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in7"
              }
            },
            {
              "source": {
                "block": "6aab3758-eddc-46e5-95ba-0886bef5a348",
                "port": "out"
              },
              "target": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "in8"
              }
            },
            {
              "source": {
                "block": "56d220a2-c382-4573-ad95-a4d169acffe2",
                "port": "out"
              },
              "target": {
                "block": "c5959df0-0392-454a-8e63-55cbcf9f3308",
                "port": "in"
              }
            }
          ]
        }
      }
    }
  }
}