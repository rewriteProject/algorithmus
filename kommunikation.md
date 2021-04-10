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
+ Merkmal (Wenn kein Merkmal angegeben ist sind es alle Merkmale)
+ Startdatum
+ Intervall [y ... year, m ... month, d ... day]

**an Chris:**

* P2
* Land
* Merkmalsart
* Merkmal (Wenn kein Merkmal angegeben ist sind es alle Merkmale)
* Startdatum
* Intervall [y ... year, m ... month, d ... day]
* (Status: CLOSE)

**von Chris:**

+ Land
+ Merkmalsart
+ Merkmal (Wenn kein Merkmal angegeben ist sind es alle Merkmale)
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
// TODO
```

