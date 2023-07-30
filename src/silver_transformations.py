from pyspark.sql.functions import lit, current_timestamp, date_format, col, to_timestamp, to_date
from datetime import datetime

file_date = '2023-07-10'

application_train = spark.read.csv('s3://datalake-igti-edc-421412/bronze/credito/application_train.csv',
                                   sep=',',
                                   header=True,
                                   encoding='utf-8',
                                   inferSchema=True)

informacoes_pessoais = application_train.select(
    col("SK_ID_CURR").alias("Id_Cliente"),
    (col("DAYS_BIRTH") / 365 * -1).cast("int").alias("Idade"),
    col("CODE_GENDER").alias("Sexo"),
    col("NAME_FAMILY_STATUS").alias("Estado_Civil"),
    col("CNT_CHILDREN").alias("Numero_de_dependentes"),
    col("CNT_FAM_MEMBERS").alias("Contagem_de_membros_da_familia"),
    col("FLAG_OWN_CAR").alias("Possui_Carro"),
    col("FLAG_OWN_REALTY").alias("Possui_Propriedade"),
    to_timestamp(date_format(current_timestamp(), "yyyy-MM-dd HH:mm:ss")).alias("TS_Carregamento_Dado")
).orderBy("Id_Cliente")

informacoes_pessoais = informacoes_pessoais.withColumn('Data_Geracao_Dados', to_date(lit(file_date), 'yyyy-MM-dd'))

informacoes_pessoais.write.mode('append').partitionBy("Data_Geracao_Dados").parquet('s3://datalake-igti-edc-421412/silver/informacoes_pessoais/')



# dados financeiros
previous_application = spark.read.csv('s3://datalake-igti-edc-421412/bronze/credito/previous_application.csv',sep=',',header=True, encoding='utf-8', inferSchema=True)
credit_card_balance = spark.read.csv('s3://datalake-igti-edc-421412/bronze/credito/credit_card_balance.csv',sep=',',header=True, encoding='utf-8', inferSchema=True)
dados_financerios = application_train.alias("pt").join(
    previous_application.alias("pa"),on="SK_ID_CURR",how="left").join(
        credit_card_balance.alias("ccb"),on="SK_ID_CURR",how="left"
    ).select(
    col("pt.SK_ID_CURR").alias("Id_Cliente"),
    col("pt.AMT_INCOME_TOTAL").alias("Valor_Renda"),
    col("ccb.AMT_DRAWINGS_POS_CURRENT").alias("Saque_Total_Caixa_Eletronico_POS"),
    col("ccb.AMT_CREDIT_LIMIT_ACTUAL").alias("Limite_Disponivel"),
    col("pt.NAME_INCOME_TYPE").alias("Tipo_Renda"),
    (col("pt.DAYS_EMPLOYED") * -1).alias("Dias_Empregado"),
    col("ccb.AMT_DRAWINGS_CURRENT").alias("Valor_Saque_Total"),
    col("ccb.AMT_DRAWINGS_ATM_CURRENT").alias("Valor_Saque_Caixa_Eletronico"),
    col("pa.NAME_CONTRACT_TYPE").alias("Tipo_Contrato"),
    col("ccb.AMT_DRAWINGS_OTHER_CURRENT").alias("Valor_Saque_Total_ATEND_TRANSF"),
    col("pa.NAME_CONTRACT_STATUS").alias("Status_Contrato"),
    col("pa.AMT_APPLICATION").alias("Valor_emprestimo_solicitado"),
    col("pa.AMT_CREDIT").alias("Valor_emprestimo_concedido"),
    col("pa.AMT_DOWN_PAYMENT").alias("Valor_entrada"),
    col("pa.AMT_ANNUITY").alias("Valor_Anuidade_emprestimo"),
    col("ccb.AMT_BALANCE").alias("Valor_Fatura"),
    col("pa.AMT_GOODS_PRICE").alias("Valor_bens"),
    col("ccb.AMT_INST_MIN_REGULARITY").alias("Valor_Pagamento_Minimo_Fatura"),
    col("ccb.AMT_PAYMENT_CURRENT").alias("Valor_Fatura_Paga"),
    col("pa.RATE_DOWN_PAYMENT").alias("Taxa_Entrada"),
    col("ccb.AMT_RECEIVABLE_PRINCIPAL").alias("Valor_Fatura_Pendente"),
    col("ccb.AMT_RECIVABLE").alias("Valor_Fatura_Pendente_Juros"),
    col("ccb.NAME_CONTRACT_STATUS").alias("Status_Cartao_Credito"),
    col("pt.TARGET").alias("Emprestimo_Pago"),
    col("pt.NAME_TYPE_SUITE").alias("Acompanhantes_Cliente"),
    col("pt.WEEKDAY_APPR_PROCESS_START").alias("Dia_Semana_Solicitacao_Emprestimo"),
    col("pt.HOUR_APPR_PROCESS_START").alias("Hora_Solicitacao_Emprestimo"),
    to_timestamp(date_format(current_timestamp(), "yyyy-MM-dd HH:mm:ss")).alias("TS_Carregamento_Dado")
)
dados_financerios = dados_financerios.withColumn('Data_Geracao_Dados', to_date(lit(file_date), 'yyyy-MM-dd'))    
dados_financerios.write.mode('append').partitionBy("Data_Geracao_Dados").parquet('s3://datalake-igti-edc-421412/silver/financeiro/')


# Histórico de Crédito
#Lendo as tabelas
#Criando a tabela de Histórico de Crédito
bureau = spark.read.csv('s3://datalake-igti-edc-421412/bronze/credito/bureau.csv',sep=',',header=True, encoding='utf-8', inferSchema=True)
pos_cash_balance = spark.read.csv('s3://datalake-igti-edc-421412/bronze/credito/POS_CASH_balance.csv', sep=',', header=True, encoding='utf-8', inferSchema=True)
#Criando a coluna de prestações que já foram pagas do empréstimo
pos_cash_balance = pos_cash_balance.withColumn('Qtdade_Prestacoes_Pagas', lit(pos_cash_balance.CNT_INSTALMENT - pos_cash_balance.CNT_INSTALMENT_FUTURE))

historico_de_credito = bureau.alias("br").join(
    other = pos_cash_balance.alias("pcb"),on="SK_ID_CURR",how="left").select(
    col("br.SK_ID_CURR").alias("Id_Cliente"),
    col("br.CREDIT_DAY_OVERDUE").alias("Dias_Atraso_Credito"),
    col("br.CREDIT_ACTIVE").alias("Status_Credito"),
    col("br.AMT_CREDIT_SUM").alias("Valor_Total_Credito"),
    col("br.AMT_CREDIT_SUM_LIMIT").alias("Valor_Total_Divida_Atual"),
    col("br.AMT_CREDIT_SUM_OVERDUE").alias("Valor_Total_Credito_Vencido"),
    col("br.CREDIT_TYPE").alias("Tipo_de_Credito"),
    col("pcb.CNT_INSTALMENT").alias("Qtdade_Prestacoes_Programadas"),
    col("pcb.CNT_INSTALMENT_FUTURE").alias("Qtdade_Prestacoes_Futuras"),
    col("pcb.Qtdade_Prestacoes_Pagas"),
    to_timestamp(date_format(current_timestamp(), "yyyy-MM-dd HH:mm:ss")).alias("TS_Carregamento_Dado")
)
    
historico_de_credito = historico_de_credito.withColumn('Data_Geracao_Dados', to_date(lit(file_date), 'yyyy-MM-dd'))
historico_de_credito.write.mode('append').partitionBy("Data_Geracao_Dados").parquet('s3://datalake-igti-edc-421412/silver/historico_credito/')


# Emprego
application_train.createOrReplaceTempView('application_train')
dataframe_emprego = spark.sql(f"""
          SELECT
          SK_ID_CURR AS Id_Cliente,
            CASE
              WHEN OCCUPATION_TYPE LIKE '%staff%' THEN LEFT(OCCUPATION_TYPE, POSITION(' staff' IN OCCUPATION_TYPE))
              ELSE OCCUPATION_TYPE
            END Funcao,
            CASE
              WHEN OCCUPATION_TYPE LIKE '%staff%' THEN True
              WHEN OCCUPATION_TYPE IS NULL THEN null
              ELSE False
            END Gerente,
          CASE
             WHEN ORGANIZATION_TYPE LIKE '%Type%' THEN LEFT(ORGANIZATION_TYPE, POSITION('Type' IN ORGANIZATION_TYPE) - 1)
            WHEN ORGANIZATION_TYPE LIKE '%type%' THEN LEFT(ORGANIZATION_TYPE, POSITION(':' IN ORGANIZATION_TYPE) - 1)
            ELSE ORGANIZATION_TYPE
          END AS Area_Atuacao,
          CASE
            WHEN ORGANIZATION_TYPE LIKE '%Type%' THEN RIGHT(ORGANIZATION_TYPE, 1)
            WHEN ORGANIZATION_TYPE LIKE '%type%' THEN RIGHT(ORGANIZATION_TYPE, 1)
            ELSE 'null'
          END AS Tipo_Area_Atuacao,
          CASE
              WHEN DAYS_EMPLOYED > 0 THEN 999
              ELSE DAYS_EMPLOYED
            END AS Dias_Empregado,
            CASE
              WHEN DAYS_EMPLOYED <= 0 THEN TO_DATE({file_date}) + DAYS_EMPLOYED
              ELSE null
            END Data_Inicio_Emprego,
            TO_DATE('{file_date}') AS Data_Geracao_Dado,
            current_timestamp AS TS_Carregamento_Dado
          FROM application_train
          """)

dataframe_emprego.write.partitionBy('Data_Geracao_Dado').mode('append').parquet('s3://datalake-igti-edc-421412/silver/emprego/')

dataframe_veiculo = spark.sql(f"""
          SELECT
            SK_ID_CURR AS Id_Cliente,
            CASE
              WHEN FLAG_OWN_CAR = 'Y' THEN True
              ELSE False
            END AS Possui_Carro,
            CAST(OWN_CAR_AGE AS INT) AS Qtd_Anos_Carro_Emprestimo,
            TO_DATE('{file_date}') AS Data_Geracao_Dado,
            CURRENT_TIMESTAMP AS TS_Carregamento_Dado
          FROM application_train;
          """)

dataframe_veiculo.write.partitionBy('Data_Geracao_Dado').mode('append').parquet('s3://datalake-igti-edc-421412/silver/veiculo/')

data_frame_ambiente_social = spark.sql(f"""
          SELECT
            SK_ID_CURR AS Id_Cliente,
            ROUND(REGION_POPULATION_RELATIVE,10) AS Populacao_Regiao_Cliente,
            REGION_RATING_CLIENT AS Classificacao_Regiao,
            REGION_RATING_CLIENT_W_CITY AS Classificacao_Regiao_Cidade,
            TO_DATE('{file_date}') AS Data_Geracao_Dado,
            CURRENT_TIMESTAMP AS TS_Carregamento_Dado
          FROM application_train;
          """)
data_frame_ambiente_social.write.partitionBy('Data_Geracao_Dado').mode('append').parquet('s3://datalake-igti-edc-421412/silver/ambiente_social/')

dataframe_educacao = spark.sql(f"""
          SELECT
            SK_ID_CURR AS Id_Cliente,
            NAME_EDUCATION_TYPE AS Nivel_Educacao,
            TO_DATE('{file_date}') AS Data_Geracao_Dado,
            CURRENT_TIMESTAMP AS TS_Carregamento_Dado
          FROM application_train;
          """)

dataframe_educacao.write.partitionBy('Data_Geracao_Dado').mode('append').parquet('s3://datalake-igti-edc-421412/silver/educacao/')

dataframe_imoveis = spark.sql(f"""
          SELECT
            SK_ID_CURR AS Id_Cliente,
            CASE
              WHEN FLAG_OWN_REALTY = 'Y' THEN True
              ELSE False
            END Possui_Imovel,
            NAME_HOUSING_TYPE AS Situacao_Habitacional,
            TO_DATE('{file_date}') AS Data_Geracao_Dado,
            CURRENT_TIMESTAMP AS TS_Carregamento_Dado
          FROM application_train;
          """)

dataframe_imoveis.write.partitionBy('Data_Geracao_Dado').mode('append').parquet('s3://datalake-igti-edc-421412/silver/imoveis/')

