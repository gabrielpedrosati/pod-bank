| Taxa_inadimplência | Media_Emprestimo | Data_Geracao_Dado |
| ------------------ | ---------------- | ----------------- |
| 10                 | 650000           | 27-07-2023        |
|                    |                  |                   |
|                    |                  |                   |

Cartao Credito (Ao longo do tempo)

| Coluna                                                      | Descrição                                                                                                                                                         |     |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| SK_ID_CURR                                                  | ID do Cliente                                                                                                                                                     |     |
| Limite                                                      |                                                                                                                                                                   |     |
| Limite_Utilizado(AMT_DRAWINGS_POS_CURRENT)                  |                                                                                                                                                                   |     |
| Limite_Disponivel(AMT_CREDIT_LIMIT_ACTUAL)                  |                                                                                                                                                                   |     |
| Valor_Saque_Caixa_Eletronico( AMT_DRAWINGS_ATM_CURRENT)     |                                                                                                                                                                   |     |
| Saque_Total_Mes (AMT_DRAWINGS_CURRENT)                      | Inclui transações em caixas eletrônicos e compras                                                                                                                 |     |
| Saque_Total_ATEND_TRANSF (AMT_DRAWINGS_OTHER_CURRENT)       | Montante total sacado pelo cliente em outros canais além dos caixas eletrônicos, como balcões de atendimento ou transferências.                                   |     |
| Saque_Total_Caixa_Eletronico_POS (AMT_DRAWINGS_POS_CURRENT) | Montante total sacado pelo cliente em caixas eletrônicos, mas especificamente na modalidade "POS" (Point of Sale), ou seja, saques que ocorreram durante compras. |     |
| Fatura_Mes (AMT_BALANCE)                                    | Saldo atual do cartão de crédito do cliente para o mês em questão                                                                                                 |     |
| Valor_Minimo_Fatura_Mes (AMT_INST_MIN_REGULARITY)           | Valor mínimo da parcela que o cliente é obrigado a pagar em um mês específico.                                                                                    |     |
| Fatura_Paga_Mes(AMT_PAYMENT_CURRENT)                        | Montante total pago pelo cliente durante o mês específico.                                                                                                        |     |
| Fatura_Pendente (AMT_RECEIVABLE_PRINCIPAL)                  | Montante principal que o cliente ainda deve pagar no mês específico.                                                                                              |     |
| Fatura_Pendente_Juros(AMT_RECIVABLE)                        | Valor total que o cliente ainda deve pagar, incluindo o montante principal e juros acumulados.                                                                    |     |
|                                                             |                                                                                                                                                                   |     |

Cadastro / Informações Pessoais

| Nome                                                                         | Descrição | Idade |
| ---------------------------------------------------------------------------- | --------- | ----- |
| SK_ID_CURR                                                                   |           |       |
| Genero(CODE_GENDER) v                                                        |           |       |
| Possui_Carro(FLAG_OWN_CAR)                                                   |           |       |
| Possui_Propriedade(FLAG_OWN_REALTY)                                          |           |       |
| Quantidade_Filhos(CNT_CHILDREN)                                              |           |       |
| Renda_Total(AMT_INCOME_TOTAL) - puxar da temp view credit_card               |           |       |
| Tipo_Renda(NAME_INCOME_TYPE)- puxar da temp view credit_card                 |           |       |
| Nivel_Educacao(NAME_EDUCATION_TYPE) - - puxar da temp view educacao          |           |       |
| Estado_Civil(NAME_FAMILY_STATUS)                                             |           |       |
| Tipo_Habitacao(NAME_HOUSING_TYPE)- puxar da temp view imovel                 |           |       |
| Idade(DAYS_BIRTH)                                                            |           |       |
| Dias_Empregado(DAYS_EMPLOYED) (Se trabalha) - puxar da temp view credit_card |           |       |
| Cargo (OCCUPATION_TYPE)- puxar da temp view emprego                          |           |       |
| Quantidade_Membros_Familia(CNT_FAM_MEMBERS)                                  |           |       |
| Ramo_Empresarial (ORGANIZATION_TYPE)- puxar da temp view emprego             |           |       |
|                                                                              |           |       |

Emprestimo

| SK_ID_CURR                                                                      |                                                                    |     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --- |
| Pago(TARGET) - temp view financeiro                                             |                                                                    |     |
| Tipo_Contrato(NAME_CONTRACT_TYPE) - temp view financeiro                        |                                                                    |     |
| Valor_emprestimo_concedido(AMT_CREDIT)- temp view financeiro                    |                                                                    |     |
| Valor_Anuidade_emprestimo(AMT_ANNUITY)- temp view financeiro                    |                                                                    |     |
| Valor_bens(AMT_GOODS_PRICE)- temp view financeiro                               | Preço dos bens para os quais o empréstimo está sendo solicitado    |     |
| Acompanhantes_Cliente(NAME_TYPE_SUITE)- temp view financeiro                    | Tipo de conjunto de pessoas que aconpanham o cliente no empréstimo |     |
| Dia_Semana_Solicitacao(WEEKDAY_APPR_PROCESS_START)- temp view financeiro        | Dia da semana em que o pedido de empréstimo foi iniciado           |     |
| Hora_Solicitacao(HOUR_APPR_PROCESS_START)- temp view financeiro                 |                                                                    |     |
| Qtd_Documentos_Informados(FLAG_DOCUMENT) - - temp view bronze_application_train |                                                                    |     |
|                                                                                 |                                                                    |     |

Pedidos de Empréstimo

Histórico de Crédito / Bureau

Pagamentos e Atrasos (Inadimplencia)

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |
|     |     |     |
