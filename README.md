# Algorithmus

Author: Lisa Wachter   
Version: 02.02.2021



## Anwendungsfälle

### Informationen

#### I1 Container überfällig

**von Flo:**

+ I1
+ Land (wenn kein Land angegeben ist sind es alle Länder)

**an Chris:**

+ Land (wenn kein Land angegeben ist sind es alle Länder)
+ (Status: OPEN)

**von Chris:**

* Land (oder Länder)
* ContainderID
* Öffnungs-Datum
* Status: OPEN

```
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
		}
	}
}
```



#### I2

**von Flo:**

+ 



### Statistiken





### Prognosen











## Links

https://www.datacamp.com/courses/foundations-of-predictive-analytics-in-python-part-1

https://www.programmer-books.com/wp-content/uploads/2019/05/Learning-Predictive-Analytics-with-Python.pdf