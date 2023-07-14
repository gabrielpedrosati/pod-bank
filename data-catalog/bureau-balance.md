# Bureau Balance



| Row            | description                                                                                                                                                                                                                                      | special                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| SK_BUREAU_ID   | Recoded ID of Credit Bureau credit (unique coding for each application) - use this to join to CREDIT_BUREAU table                                                                                                                                | hashed                                |
| MONTHS_BALANCE | Month of balance relative to application date (-1 means the freshest balance date)                                                                                                                                                               | time only relative to the application |
| STATUS         | Status of Credit Bureau loan during the month (active, closed, DPD0-30,… [C means closed, X means status unknown, 0 means no DPD, 1 means maximal did during month between 1-30, 2 means DPD 31-60,… 5 means DPD 120+ or sold or written off ] ) |                                       |
