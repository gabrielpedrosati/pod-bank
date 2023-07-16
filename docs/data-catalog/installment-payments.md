# Installments Payments

Descrição:

- Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample.

- There is a) one row for every payment that was made plus b) one row each for missed payment.

- One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample.

| Row                    | description                                                                                                                                                                                | special                               |
|:----------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:-------------------------------------:|
| SK_ID_PREV             | ID of previous credit in Home credit related to loan in our sample. (One loan in our sample can have 0,1,2 or more previous loans in Home Credit)                                          | hashed                                |
| SK_ID_CURR             | ID of loan in our sample                                                                                                                                                                   | hashed                                |
| NUM_INSTALMENT_VERSION | Version of installment calendar (0 is for credit card) of previous credit. Change of installment version from month to month signifies that some parameter of payment calendar has changed |                                       |
| NUM_INSTALMENT_NUMBER  | On which installment we observe payment                                                                                                                                                    |                                       |
| DAYS_INSTALMENT        | When the installment of previous credit was supposed to be paid (relative to application date of current loan)                                                                             | time only relative to the application |
| DAYS_ENTRY_PAYMENT     | When was the installments of previous credit paid actually (relative to application date of current loan)                                                                                  | time only relative to the application |
| AMT_INSTALMENT         | What was the prescribed installment amount of previous credit on this installment                                                                                                          |                                       |
| AMT_PAYMENT            | What the client actually paid on previous credit on this installment                                                                                                                       |                                       |
