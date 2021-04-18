# Kommunikation

## Informationen

### I1 Container Überfälligkeit

**von Flo:**

+ I1
+ Land (wenn kein Land angegeben ist sind es alle Länder)

**an Chris:**

+ I1
+ Land (wenn kein Land angegeben ist sind es alle Länder)
+ (Status: OPEN)

**von Chris:**

* Land (oder Länder)
* ContainderID
* Öffnungs-Datum
* Status: OPEN

```json
{
  "container": {
    "status": "OPEN",
    "country": {
      "china" : {
        "container_id" : 1,
        "open_date" : "2021-01-30"
      },
      "russia" : {
        "container_id" : 2,
        "open_date" : "2021-01-24"
      },
      "usa" : {
        "container_id" : 3,
        "open_date" : "2021-01-19"
      },
      ...
    }
  }
}
```

**an Flo:**

```json
{
  "container": {
    "china": {
      "container_id": 1,
      "open_date": "2021-01-30",
      "overdue": true
    },
    "russia": {
      "container_id": 2,
      "open_date": "2021-01-24",
      "overdue": true
    },
    "usa": {
      "container_id": 3,
      "open_date": "2021-01-19",
      "overdue": true
    },
    ...
  }
}
```



### I2 Container Gewicht Auslastung

**von Flo:**

+ I2
+ Land (wenn kein Land angegeben ist sind es alle Länder)

**an Chris:**

+ I2
+ Land (wenn kein Land angegeben ist sind es alle Länder)
+ (Status: OPEN)

**von Chris:**

+ Land/Länder
+ ContainerID
+ Aktuelles Gewicht
+ Maximales Gewicht
+ Status: OPEN

```json
{
  "container": {
    "status": "OPEN",
    "country": {
      "china": {
        "container_id": 1,
        "curr_weight_kg": 22,
        "max_weight_kg": 25
      },
      "russia": {
        "container_id": 2,
        "curr_weight_kg": 8,
        "max_weight_kg": 25
      },
      "usa": {
        "container_id": 3,
        "curr_weight_kg": 15,
        "max_weight_kg": 25
      },
      ...
    }
  }
}
```

**an Flo:**

```json
{
  "container": {
    "china": {
      "container_id": 1,
      "curr_weight_kg": 22,
      "max_weight_kg": 25,
      "utilization": 88.0
    },
    "russia": {
      "container_id": 2,
      "curr_weight_kg": 8,
      "max_weight_kg": 25,
      "utilization": 32.0
    },
    "usa": {
      "container_id": 3,
      "curr_weight_kg": 15,
      "max_weight_kg": 25,
      "utilization": 60.0
    },
    ...
  }
}
```



## Statistiken

### S1 Zeitraumabhängiger Anteil

**von Flo:**

+ S1
+ Land
+ Startdatum (des Zeitraums)
+ Enddatum (des Zeitraums)
+ Merkmalsart (wenn nichts angegeben dann alles)

**an Chris:**

+ S1
+ Land
+ Startdatum (des Zeitraums)
+ Enddatum (des Zeitraums)
+ Merkmalsart (wenn nichts angegeben dann alles)
+ (Status: CLOSED)

**von Chris:**

```json
{
  "container": {
    "status": "CLOSE",
    "start_time": "01-01-2021",
    "end_time": "01-02-2021",
    "type": "",
    "country": {
      "china": {
        "color": {
          "red": 2,
          "blue": 5,
          "green": 10
        },
        "brand": {
          "nike": 7,
          "adidas": 3,
          "hm": 7
        },
        "category": {
          "t-shirt": 6,
          "shoes": 9,
          "pants": 2
        },
        "weight": {
          "2kg": 4,
          "3kg": 7,
          "4kg": 6
        }
      }
    }
  }
}
```

**an Flo:**

```
{
  "container": {
    "china": {
      "color": {
        "red": {
          "abs": 2,
          "rel": 11.76470588235294
        },
        "blue": {
          "abs": 5,
          "rel": 29.411764705882355
        },
        "green": {
          "abs": 10,
          "rel": 58.82352941176471
        }
      },
      "brand": {
        "nike": {
          "abs": 7,
          "rel": 41.17647058823529
        },
        "adidas": {
          "abs": 3,
          "rel": 17.647058823529413
        },
        "hm": {
          "abs": 7,
          "rel": 41.17647058823529
        }
      },
      "category": {
        "t-shirt": {
          "abs": 6,
          "rel": 35.294117647058826
        },
        "shoes": {
          "abs": 9,
          "rel": 52.94117647058824
        },
        "pants": {
          "abs": 2,
          "rel": 11.76470588235294
        }
      },
      "weight": {
        "2kg": {
          "abs": 4,
          "rel": 23.52941176470588
        },
        "3kg": {
          "abs": 7,
          "rel": 41.17647058823529
        },
        "4kg": {
          "abs": 6,
          "rel": 35.294117647058826
        }
      }
    }
  }
}

```



## Prognosen

### P1 Erwartetes Lieferdatum

**von Flo:**

+ P1
+ Land
+ Startdatum

**an Chris (Anfrage 1):**

+ P1_1
+ Land
+ Startdatum (Startdatum von dem gerechnet werden soll)
+ (Enddatum (default: NOW))
+ (Status: CLOSE)

**von Chris (Antwort 1):**

+ Land
+ Startdatum (Startdatum von dem gerechnet werden soll)
+ Enddatum (default: NOW)
+ (Status: CLOSE)
+ Daten (pro Container `open_date` und `close_date`)

```json
{
  "container": {
    "status": "CLOSE",
    "country": "china",
    "min_date": "2019-01-01",
    "max_date": "now",
    "dates": {
      "1": {
        "open_date": "2019-01-01",
        "close_date": "2019-01-30"
      },
      "2": {
        "open_date": "2019-02-04",
        "close_date": "2019-03-02"
      },
      "3": {
        "open_date": "2019-05-10",
        "close_date": "2019-05-29"
      },
      ...
    }
  }
}
```

**an Chris (Anfrage 2):**

+ Land
+ Status: OPEN

**von Chris (Antwort 2):**

+ Land
+ Status: OPEN
+ `create_date` von Container

```json
{
  "container": {
    "status": "OPEN",
    "country": "china",
    "create_date": "2021-02-20"
  }
}
```

**an Flo:**

```json
{
  "container": {
    "country": "china",
    "create_date": "2021-02-20",
    "close_date_forecast": "2021-03-19",
    "accuracy": "20.0"
  }
}
```



### P2 Merkmalsentwicklung

**von Flo:**

+ P2
+ Land
+ Merkmalsart
+ Merkmal
+ Startdatum
+ Intervall [y ... year, m ... month, d ... day]

**an Chris:**

* P2
* Land
* Merkmalsart
* Merkmal
* Startdatum
* Intervall [y ... year, m ... month, d ... day]
* (Status: CLOSE)

**von Chris:**

+ Land
+ Merkmalsart
+ Merkmal
+ Startdatum
+ Intervall 
+ Intervall-Werte für jedes Merkmal pro Merkmalsart

```json
{
  "container": {
    "status": "CLOSE",
    "country": "china",
    "type": "color",
    "min_date": "2020-01-01",
    "intervall": "m",
    "colors": {
      "green": {
        "01-2015": 2,
        "02-2015": 4,
        "03-2015": 7,
        "04-2015": 15,
        "05-2015": 3,
        "06-2015": 7,
        "07-2015": 9,
        "08-2015": 24,
        "09-2015": 26,
        "10-2015": 15,
        "11-2015": 14,
        "12-2015": 6,
        ...
      }
    }
  }
}
```

**an Flo:**

```json
{
  "response": {
    "container": {
      "status": "CLOSE",
      "country": "china",
      "type": "color",
      "min_date": "2015-01-01",
      "intervall": "m",
      "colors": {
        "green": {
          "01-2015": 56,
          "02-2015": 47,
          "03-2015": 87,
          "04-2015": 101,
          "05-2015": 168,
          "06-2015": 216,
          "07-2015": 231,
          "08-2015": 174,
          "09-2015": 168,
          "10-2015": 98,
          "11-2015": 65,
          "12-2015": 60,
          "01-2016": 41,
          "02-2016": 49,
          "03-2016": 71,
          "04-2016": 92,
          "05-2016": 156,
          "06-2016": 189,
          "07-2016": 198,
          "08-2016": 145,
          "09-2016": 101,
          "10-2016": 86,
          "11-2016": 57,
          "12-2016": 39,
          "01-2017": 42,
          "02-2017": 53,
          "03-2017": 65,
          "04-2017": 86,
          "05-2017": 91,
          "06-2017": 130,
          "07-2017": 156,
          "08-2017": 148,
          "09-2017": 132,
          "10-2017": 98,
          "11-2017": 85,
          "12-2017": 70,
          "01-2018": 73,
          "02-2018": 81,
          "03-2018": 88,
          "04-2018": 107,
          "05-2018": 136,
          "06-2018": 187,
          "07-2018": 212,
          "08-2018": 199,
          "09-2018": 156,
          "10-2018": 121,
          "11-2018": 99,
          "12-2018": 87,
          "01-2019": 71,
          "02-2019": 81,
          "03-2019": 109,
          "04-2019": 122,
          "05-2019": 158,
          "06-2019": 191,
          "07-2019": 220,
          "08-2019": 225,
          "09-2019": 198,
          "10-2019": 156,
          "11-2019": 98,
          "12-2019": 89,
          "01-2020": 92,
          "02-2020": 81,
          "03-2020": 78,
          "04-2020": 54,
          "05-2020": 61,
          "06-2020": 98,
          "07-2020": 121,
          "08-2020": 118,
          "09-2020": 101,
          "10-2020": 81,
          "11-2020": 47,
          "12-2020": 31,
          "01-2021": 33,
          "02-2021": 48,
          "03-2021": 56
        }
      }
    }
  },
  "forecast": {
    "averages": {
      "2021-04-01": 62.56852041461447,
      "2021-05-01": 61.45902044047619,
      "2021-06-01": 57.98311844247758,
      "2021-07-01": 58.53300493612715,
      "2021-08-01": 58.37041131290482,
      "2021-09-01": 58.20826934403275,
      "2021-10-01": 58.04657777490051,
      "2021-11-01": 57.88533535438278,
      "2021-12-01": 57.724540834829604,
      "2022-01-01": 57.564192972056766,
      "2022-02-01": 57.404290525336165,
      "2022-03-01": 57.24483225738621,
      "2022-04-01": 57.08581693436222,
      "2022-05-01": 56.927243325846945,
      "2022-06-01": 56.76911020484096,
      "2022-07-01": 56.61141634775324,
      "2022-08-01": 56.45416053439165,
      "2022-09-01": 56.29734154795352,
      "2022-10-01": 56.14095817501623,
      "2022-11-01": 55.985009205527824,
      "2022-12-01": 55.82949343279763,
      "2023-01-01": 55.674409653486954,
      "2023-02-01": 55.519756667599715,
      "2023-03-01": 55.36553327847323
    },
    "deviations": {
      "2021-04-01": 1.244566663293399,
      "2021-05-01": 1.4928260522946377,
      "2021-06-01": 1.7778112022605383,
      "2021-07-01": 2.0800663001161284,
      "2021-08-01": 2.3437552037822647,
      "2021-09-01": 2.602121947294819,
      "2021-10-01": 2.859199700829607,
      "2021-11-01": 3.117326966321149,
      "2021-12-01": 3.3780145370952916,
      "2022-01-01": 3.6423170730633143,
      "2022-02-01": 3.911015978893649,
      "2022-03-01": 4.184718614814619,
      "2022-04-01": 4.4639161788171355,
      "2022-05-01": 4.749019444108769,
      "2022-06-01": 5.040381850044018,
      "2022-07-01": 5.338314989722628,
      "2022-08-01": 5.643099328170442,
      "2022-09-01": 5.954991820172332,
      "2022-10-01": 6.274231450522057,
      "2022-11-01": 6.601043345035379,
      "2022-12-01": 6.935641875574607,
      "2023-01-01": 7.278233042578752,
      "2023-02-01": 7.629016329341905,
      "2023-03-01": 7.988186163842116
    },
    "confidence": {
      "2021-04-01": {
        "lower": 40.749633405076075,
        "upper": 96.07006050725278
      },
      "2021-05-01": {
        "lower": 28.02424092715016,
        "upper": 134.78371112073438
      },
      "2021-06-01": {
        "lower": 18.773044830459295,
        "upper": 179.08879751139068
      },
      "2021-07-01": {
        "lower": 13.930958782206398,
        "upper": 245.93516644588436
      },
      "2021-08-01": {
        "lower": 10.994565413316995,
        "upper": 309.88991276643685
      },
      "2021-09-01": {
        "lower": 8.932179861189267,
        "upper": 379.325391190269
      },
      "2021-10-01": {
        "lower": 7.405490895392146,
        "upper": 454.9874193315247
      },
      "2021-11-01": {
        "lower": 6.234087863218255,
        "upper": 537.4823266221345
      },
      "2021-12-01": {
        "lower": 5.311326008751717,
        "upper": 627.3617189194221
      },
      "2022-01-01": {
        "lower": 4.569537540234092,
        "upper": 725.1579144165286
      },
      "2022-02-01": {
        "lower": 3.963492934339336,
        "upper": 831.401146742924
      },
      "2022-03-01": {
        "lower": 3.4617269204500736,
        "upper": 946.6289211946942
      },
      "2022-04-01": {
        "lower": 3.0416427213779467,
        "upper": 1071.391610907936
      },
      "2022-05-01": {
        "lower": 2.6865862300160304,
        "upper": 1206.2561016926106
      },
      "2022-06-01": {
        "lower": 2.384015343534558,
        "upper": 1351.808360709345
      },
      "2022-07-01": {
        "lower": 2.124310492801159,
        "upper": 1508.6553833628525
      },
      "2022-08-01": {
        "lower": 1.8999769778473359,
        "upper": 1677.4267682200016
      },
      "2022-09-01": {
        "lower": 1.7050954801584617,
        "upper": 1858.7760640080924
      },
      "2022-10-01": {
        "lower": 1.5349346701497828,
        "upper": 2053.3819752089908
      },
      "2022-11-01": {
        "lower": 1.3856725286557325,
        "upper": 2261.9494800721054
      },
      "2022-12-01": {
        "lower": 1.2541922870579025,
        "upper": 2485.210895591239
      },
      "2023-01-01": {
        "lower": 1.13793063841908,
        "upper": 2723.926912250637
      },
      "2023-02-01": {
        "lower": 1.0347632337491055,
        "upper": 2978.887613991966
      },
      "2023-03-01": {
        "lower": 0.9429172079611063,
        "upper": 3250.9134941316784
      }
    }
  }
}
```

