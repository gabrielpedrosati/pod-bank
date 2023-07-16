# credit_card_balance.csv

Descrição:

- Monthly balance snapshots of previous credit cards that the applicant has with Home Credit.

- This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credit cards * # of months where we have some history observable for the previous credit card) rows.

| Row                        | description                                                                                                                                       | special                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| SK_ID_PREV                 | ID of previous credit in Home credit related to loan in our sample. (One loan in our sample can have 0,1,2 or more previous loans in Home Credit) | hashed                                |
| SK_ID_CURR                 | ID of loan in our sample                                                                                                                          | hashed                                |
| MONTHS_BALANCE             | Month of balance relative to application date (-1 means the freshest balance date)                                                                | time only relative to the application |
| AMT_BALANCE                | Balance during the month of previous credit                                                                                                       |                                       |
| AMT_CREDIT_LIMIT_ACTUAL    | Credit card limit during the month of the previous credit                                                                                         |                                       |
| AMT_DRAWINGS_ATM_CURRENT   | Amount drawing at ATM during the month of the previous credit                                                                                     |                                       |
| AMT_DRAWINGS_CURRENT       | Amount drawing during the month of the previous credit                                                                                            |                                       |
| AMT_DRAWINGS_OTHER_CURRENT | Amount of other drawings during the month of the previous credit                                                                                  |                                       |
| AMT_DRAWINGS_POS_CURRENT   | Amount drawing or buying goods during the month of the previous credit                                                                            |                                       |
| AMT_INST_MIN_REGULARITY    | Minimal installment for this month of the previous credit                                                                                         |                                       |
| AMT_PAYMENT_CURRENT        | How much did the client pay during the month on the previous credit                                                                               |                                       |
| AMT_PAYMENT_TOTAL_CURRENT  | How much did the client pay during the month in total on the previous credit                                                                      |                                       |
| AMT_RECEIVABLE_PRINCIPAL   | Amount receivable for principal on the previous credit                                                                                            |                                       |
| AMT_RECIVABLE              | Amount receivable on the previous credit                                                                                                          |                                       |
| AMT_TOTAL_RECEIVABLE       | Total amount receivable on the previous credit                                                                                                    |                                       |
| CNT_DRAWINGS_ATM_CURRENT   | Number of drawings at ATM during this month on the previous credit                                                                                |                                       |
| CNT_DRAWINGS_CURRENT       | Number of drawings during this month on the previous credit                                                                                       |                                       |
| CNT_DRAWINGS_OTHER_CURRENT | Number of other drawings during this month on the previous credit                                                                                 |                                       |
| CNT_DRAWINGS_POS_CURRENT   | Number of drawings for goods during this month on the previous credit                                                                             |                                       |
| CNT_INSTALMENT_MATURE_CUM  | Number of paid installments on the previous credit                                                                                                |                                       |
| NAME_CONTRACT_STATUS       | Contract status (active signed,...) on the previous credit                                                                                        |                                       |
| SK_DPD                     | DPD (Days past due) during the month on the previous credit                                                                                       |                                       |
| SK_DPD_DEF                 | DPD (Days past due) during the month with tolerance (debts with low loan amounts are ignored) of the previous credit                              |                                       |
