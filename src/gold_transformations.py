# Processamento Gold

cartao_credito_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/financeiro/')
cartao_credito_dataframe.createOrReplaceTempView('credit_card')
cartao_credito = spark.sql("""
            SELECT
                Id_Cliente,
                Limite_Disponivel
                Valor_Saque_Caixa_Eletronico,
                Valor_Saque_Total,
                Valor_Saque_Total_ATEND_TRANSF,
                Saque_Total_Caixa_Eletronico_POS,
                Valor_Fatura,
                Valor_Pagamento_Minimo_Fatura,
                Valor_Fatura_Paga,
                Valor_Fatura_Pendente,
                Valor_Fatura_Pendente_Juros,
                Data_Geracao_Dados,
                CURRENT_TIMESTAMP AS TS_Carregamento_Dados
              FROM credit_card;
                """)
cartao_credito.write.partitionBy('Data_Geracao_Dados').mode('append').parquet('s3://datalake-igti-edc-421412/gold/cartao_credito/')

informacoes_pessoais_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/informacoes_pessoais/')
educacao_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/educacao/')
imoveis_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/imoveis/')
informacoes_pessoais_dataframe.createOrReplaceTempView('informacoes')
educacao_dataframe.createOrReplaceTempView('educacao')
imoveis_dataframe.createOrReplaceTempView('imoveis')



emprego_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/emprego/')
emprego_dataframe.createOrReplaceTempView('emprego')

informacoes_pessoais = spark.sql("""
    SELECT
        i.Id_Cliente,
        i.Sexo,
        CASE
           WHEN i.Possui_Carro = 'Y' THEN True
           ELSE False
        END,
        CASE
           WHEN i.Possui_Propriedade = 'Y' THEN True
           ELSE False
        END,
        i.Numero_de_dependentes,
        cc.Valor_Renda,
        cc.Tipo_Renda,
        e.Nivel_Educacao,
        i.Estado_Civil,
        im.Situacao_Habitacional,
        i.Idade,
        CASE
            WHEN em.Data_Inicio_Emprego IS NOT NULL THEN True
            ELSE False
        END AS Trabalha,
        em.Funcao AS Ramo_Empresarial,
        i.Contagem_de_membros_da_familia,
        em.Area_Atuacao,
        i.Data_Geracao_Dados,
        CURRENT_TIMESTAMP AS TS_Carregamento_Dado
    FROM informacoes i
    JOIN credit_card cc
        ON cc.Id_Cliente = i.Id_Cliente
    JOIN educacao e
        ON e.Id_Cliente = i.Id_Cliente
    JOIN imoveis im
        ON im.Id_Cliente = i.Id_Cliente
    JOIN emprego em
        ON em.Id_Cliente = i.Id_Cliente;
""")

informacoes_pessoais.write.partitionBy('Data_Geracao_Dados').mode('append').parquet('s3://datalake-igti-edc-421412/gold/informacoes_pessoais/')

financeiro_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/financeiro/')
financeiro_dataframe.createOrReplaceTempView('financeiro')
historico_credito_dataframe = spark.read.parquet('s3://datalake-igti-edc-421412/silver/financeiro/')
historico_credito_dataframe.createOrReplaceTempView('historico_credito')
bronze_application_train_dataframe = spark.read.csv('s3://datalake-igti-edc-421412/bronze/credito/application_train.csv',
                                                   sep=',',
                                                   header=True,
                                                   inferSchema=True)
bronze_application_train_dataframe.createOrReplaceTempView('bronze_application_train')

emprestimo = spark.sql("""
    SELECT
        f.Id_Cliente,
        f.Emprestimo_Pago,
        f.Tipo_Contrato,
        f.Valor_emprestimo_concedido,
        f.Valor_Anuidade_emprestimo,
        f.Valor_bens,
        f.Acompanhantes_Cliente,
        f.Dia_Semana_Solicitacao_Emprestimo,
        f.Hora_Solicitacao_Emprestimo,
        bat.FLAG_DOCUMENT_2 + bat.FLAG_DOCUMENT_3 + bat.FLAG_DOCUMENT_4 + bat.FLAG_DOCUMENT_5 + bat.FLAG_DOCUMENT_6 + bat.FLAG_DOCUMENT_7 + bat.FLAG_DOCUMENT_8 + bat.FLAG_DOCUMENT_9 + bat.FLAG_DOCUMENT_10 + bat.FLAG_DOCUMENT_11 + bat.FLAG_DOCUMENT_12 + bat.FLAG_DOCUMENT_13 + bat.FLAG_DOCUMENT_14 + bat.FLAG_DOCUMENT_15 + bat.FLAG_DOCUMENT_16 + bat.FLAG_DOCUMENT_17 + bat.FLAG_DOCUMENT_18 + bat.FLAG_DOCUMENT_19 + bat.FLAG_DOCUMENT_20 + bat.FLAG_DOCUMENT_21 AS Qtd_Total_Documentos_Entregues,
        f.Data_Geracao_Dados,
        CURRENT_TIMESTAMP AS TS_Carregamento_Dado
    FROM financeiro f
    JOIN bronze_application_train bat
       ON bat.SK_ID_CURR = f.Id_Cliente
""")

emprestimo.write.partitionBy('Data_Geracao_Dados').mode('append').parquet('s3://datalake-igti-edc-421412/gold/emprestimo/')