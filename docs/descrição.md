### Resumo do Desafio Técnico

O desafio exige a criação de uma Prova de Conceito (POC) de automação para consulta e extração de documentos fiscais municipais.

**Fluxo Principal:**

* **Entrada:** Ler os dados a partir da planilha de amostra fornecida (`janabril2026_amostra_5x5.xlsx`).

* **Processamento (Para cada linha):**
* Identificar o município e consultar a Inscrição Municipal (CCM) da empresa.

* Baixar o comprovante de Cadastro Municipal (em formato PDF, XML ou print da tela).

* Baixar o documento da Nota Fiscal (em formato PDF ou XML).

* Adaptar a extração para as regras de cada município, utilizando APIs oficiais ou automação de navegador (com tratamento para captchas, timeouts e layouts distintos).

* **Saída:**
* Salvar os documentos baixados em uma estrutura de pastas organizada por `[Município]/[CNPJ]`.

* Atualizar a planilha original com o número do CCM, o status de sucesso ou falha, mensagens de erro detalhadas e os caminhos dos arquivos salvos.

**Entregáveis Esperados:**

* Código-fonte organizado e legível, entregue via link público do GitHub ou pasta compactada.

* Documentação técnica explicando as decisões tomadas e como os desafios foram resolvidos.

* **Atenção:** Embora não haja um prazo definido, a velocidade na entrega da solução será considerada na avaliação do teste.
