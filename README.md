# Algorithmus

Author: Lisa Wachter   
Version: 02.02.2021



## Anwendungsfälle

### Informationen

#### I1 Container Überfälligkeit

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
			"overdue": True
		}, 
		"russia": {
			"container_id": 2, 
			"open_date": "2021-01-24", 
			"overdue": True
		},
		"usa": {
			"container_id": 3, 
			"open_date": "2021-01-19", 
			"overdue": True
		},
    ...
	}
}
```



#### I2 Container Gewicht Auslastung

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



### Statistiken





### Prognosen

#### P1 Erwartetes Lieferdatum

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
+ Enddatum
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

```
{
	"container": {
		"country": "china", 
		"create_date": "2021-02-20", 
		"close_date_forecast": "2021-03-19", 
		"accuracy": "20.0"
	}
}
```



#### P2

**von Flo:**

+ P2
+ Land (wenn kein Land angegeben ist sind es alle Länder)















## Links

https://www.datacamp.com/courses/foundations-of-predictive-analytics-in-python-part-1

https://www.programmer-books.com/wp-content/uploads/2019/05/Learning-Predictive-Analytics-with-Python.pdf