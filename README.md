# Algorithmus

Author: Lisa Wachter   
Version: 02.02.2021



## Anwendungsfälle

### Informationen

- [x] I1 Container Überfälligkeit
- [x] I2 Container Gewicht Auslastung

### Statistiken

- [x] S1

### Prognosen

- [x] P1 Erwartetes Lieferdatum
- [x] P2 Merkmalsentwicklung



Die genaue Beschreibung der Kommunikation ist [hier](kommunikation.md) zu finden.



## Routen

Wir mit `Flask` erstellt auf Port `5000`.

Alle Routes sind `POST` Routes.

Die Parameter müssen alle *genau* so heißen wie angegeben!



### Infromationen

```
localhost:5000/informations
```

`localhost` muss dann natürch mit der IP des Servers ausgetauscht werden.

**Parameter für I1 und I2**

`case` (I1 oder I2), `country`

### Statistiken

```
localhost:5000/statistics
```

`localhost` muss dann natürch mit der IP des Servers ausgetauscht werden.

**Parameter für S1**

`case` (S1), `countr`, `min`, `max`, `type`

### Prognosen

```
localhost:5000/predictions
```

`localhost` muss dann natürch mit der IP des Servers ausgetauscht werden.

**Parameter für P1**

`case` (P1), `country`

**Parameter für P2**

`case` (P2), `country`, `feature_type`, `feature`







## Links

https://www.datacamp.com/courses/foundations-of-predictive-analytics-in-python-part-1

https://www.programmer-books.com/wp-content/uploads/2019/05/Learning-Predictive-Analytics-with-Python.pdf

https://www.youtube.com/watch?v=e8Yw4alG16Q (main)

https://towardsdatascience.com/programmatic-identification-of-support-resistance-trend-lines-with-python-d797a4a90530

https://www.bounteous.com/insights/2020/09/15/forecasting-time-series-model-using-python-part-one/s