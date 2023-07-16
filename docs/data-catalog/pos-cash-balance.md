# pos_cash_balance.csv

Descrição:

- Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit.

- This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credits * # of months in which we have some history observable for the previous credits) rows.

| Row                   | description                                                                                                                                                                                                                                                    | special                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| SK_ID_PREV            | ID of previous credit in Home Credit related to loan in our sample. (One loan in our sample can have 0,1,2 or more previous loans in Home Credit)                                                                                                              |                                       |
| SK_ID_CURR            | ID of loan in our sample                                                                                                                                                                                                                                       |                                       |
| MONTHS_BALANCE        | Month of balance relative to application date (-1 means the information to the freshest monthly snapshot, 0 means the information at application - often it will be the same as -1 as many banks are not updating the information to Credit Bureau regularly ) | time only relative to the application |
| CNT_INSTALMENT        | Term of previous credit (can change over time)                                                                                                                                                                                                                 |                                       |
| CNT_INSTALMENT_FUTURE | Installments left to pay on the previous credit                                                                                                                                                                                                                |                                       |
| SK_DPD                | DPD (days past due) during the month of previous credit                                                                                                                                                                                                        |                                       |
| SK_DPD_DEF            | DPD during the month with tolerance (debts with low loan amounts are ignored) of the previous credit                                                                                                                                                           |                                       |
