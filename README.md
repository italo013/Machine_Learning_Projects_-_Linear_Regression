# Modelo de Regressão Linear para Marketing

## Sobre o Projeto
Este projeto desenvolve um modelo de regressão linear para prever o retorno de vendas baseado em investimentos em publicidade online. A empresa está investindo mensalmente em plataformas como YouTube, Facebook e jornais (newspaper) para prospecção de leads. O objetivo é entender a relação entre as variáveis, identificar os fatores que mais impactam na geração de leads e criar um modelo de predição de valores para estimar o retorno de vendas.

## Estrutura do Projeto
O projeto está estruturado nas seguintes etapas:
1. **Análise Descritiva**
2. **Análise Exploratória**
3. **Modelagem**
4. **Cálculo de Predição**

## Tecnologias Utilizadas
O projeto utiliza as seguintes bibliotecas Python:
1. **Python:** A linguagem de programação principal usada para implementar a lógica do modelo e os testes estatísticos.
2. **Streamlit:** Uma biblioteca Python usada para criar a interface web interativa. Streamlit permite a criação rápida de aplicativos web.
3. **Pandas:** Utilizada para manipulação e análise de dados estruturados. É particularmente útil para lidar com os dados das tábuas de mortalidade e resultados dos testes.
4. **NumPy:** Biblioteca fundamental para computação científica em Python, usada para operações matemáticas eficientes em arrays e matrizes.
5. **Plotly:** Biblioteca de visualização de dados interativa, usada para criar gráficos dinâmicos e informativos dos resultados da otimização.
6. **scikit-optimize (skopt):** Uma biblioteca de otimização que fornece implementações de várias técnicas de otimização bayesiana.

## Conjunto de Dados
O conjunto de dados contém informações sobre:
- Investimento no YouTube
- Investimento no Facebook
- Investimento em jornais (newspaper)
- Valor das vendas

## Metodologia
1. **Análise Descritiva:** Exploração inicial dos dados para compreender as variáveis e identificar problemas potenciais.
2. **Análise Exploratória:**
    - Análise de correlação entre variáveis
    - Visualização da relação entre investimento e vendas
    - Cálculo do ROI (Retorno sobre Investimento) por plataforma
    - Identificação de outliers
3. **Modelagem:**
    - Divisão dos dados em conjuntos de treino e teste
    - Construção de um modelo de regressão linear múltipla
4. **Cálculo de Predição:**
    - Treinamento do modelo
    - Avaliação do modelo usando RMSE e R²
    - Interpretação dos coeficientes do modelo

## Resultados Principais
- O modelo apresentou bom desempenho, com RMSE de 1.89 no treino e 2.36 no teste.
- O R² de 0.91 no treino e 0.87 no teste indica que o modelo explica uma grande parte da variação nos dados.
- O Facebook mostrou o maior impacto positivo nas vendas, com um aumento esperado de 19.45% nas vendas para cada unidade de aumento no investimento.

## Conclusões
O modelo de regressão linear é eficaz em prever as vendas baseado nos investimentos em publicidade. Os resultados sugerem que o Facebook pode ser a plataforma mais eficaz para gerar vendas a partir do investimento em publicidade.