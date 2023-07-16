# Bureau Balance

Descrição:

- Monthly balances of previous credits in Credit Bureau.

- This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample * # of relative previous credits * # of months where we have some history observable for the previous credits) rows.

| Row            | description                                                                                                                                                                                                                                      | special                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| SK_BUREAU_ID   | Recoded ID of Credit Bureau credit (unique coding for each application) - use this to join to CREDIT_BUREAU table                                                                                                                                | hashed                                |
| MONTHS_BALANCE | Month of balance relative to application date (-1 means the freshest balance date)                                                                                                                                                               | time only relative to the application |
| STATUS         | Status of Credit Bureau loan during the month (active, closed, DPD0-30,… [C means closed, X means status unknown, 0 means no DPD, 1 means maximal did during month between 1-30, 2 means DPD 31-60,… 5 means DPD 120+ or sold or written off ] ) |                                       |
