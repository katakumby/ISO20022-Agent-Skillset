---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalAuthorityIdentification1Code"]
code_set: "ExternalAuthorityIdentification1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalAuthorityIdentification1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalAuthorityIdentification1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external authority identification scheme name code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`AUAS`-Australian Securities and Investments Commission (ASIC)
*`ATFM`-Austrian Financial Market Authority (FMA)
*`BEFS`-Financial Services and Markets Authority (FSMA)
*`BENB`-National Bank of Belgium
*`BGFS`-Financial Supervision Commission (FSC)
*`CACS`-Canadian Securities Transition Office (CSTO)
*`CYAS`-Authority for the Supervision and Development of Cooperative Societies
*`CYCB`-Central Bank of Cyprus (CBC)
*`CYCY`-Cyprus Securities and Exchange Commission (CySEC)
*`CZCN`-Czech National Bank (CNB)
*`DEBA`-Federal Financial Supervisory Authority (BaFin)
*`DKFI`-Finanstilsynet.
*`EEEF`-Estonian Financial Supervision Authority (EFSA)
*`EUES`-European Securities and Markets Authority (ESMA)
*`ESBD`-Bank of Spain (BDE)
*`ESCN`-Comisión Nacional del Mercado de Valores (CNMV)
*`FIFS`-Finanssivalvonta (FSA)
*`FRAC`-Autorité de Contrôle Prudentiel et de Résolution (ACPR)
*`FRAM`-Autorité des Marchés Financiers (AMF)
*`GBFS`-Financial Services Authority (FSA)
*`GBFC`-Financial Conduct Authority (FCA)
*`GBPR`-Prudential Regulation Authority (PRA)
*`GIFS`-Gibraltar FSC (FSC)
*`USCF`-US Commodity Futures Trading Commission (CFTC)
*`GRBO`-Bank of Greece (BOG)
*`GRHC`-Hellenic Capital Market Commission (HCMC)
*`HRHA`-Croatian Financial Services Supervisory Agency (HANFA)
*`HUPS`-Hungarian Financial Supervisory Authority (PSZAF)
*`IECB`-Central Bank of Ireland (CBI)
*`ISFM`-Iceland Financial Supervisory Authority (FME)
*`ITBD`-BANCA D'ITALIA (BDI)
*`ITCO`-Commissione Nazionale per le Societa e la Borsa (CONSOB)
*`LIFM`-Financial Market Authority (FMA)
*`LTLS`-Bank of Lithuania (LSC)
*`LUCS`-Commission de Surveillance du Secteur Financier (CSSF)
*`LVFK`-Financial & Capital Market Commission (FKTK)
*`MTMF`-Malta Financial Services Authority (MFSA)
*`NLAF`-Netherlands Authority for the Financial Markets (AFM)
*`NLDN`-Nederlandse Bank (DNB)
*`NOFI`-Norwegian Financial Supervisory Authority (Finanstilsynet)
*`PLKN`-Polish Financial Supervisory Commission (KNF)
*`PTBP`-Banco de Portugal (BP)
*`PTCM`-Comissão do Mercado de Valores Mobiliários (CMVM)
*`ROAS`-Romanian Financial Supervisory Authority (ASF)
*`SEFI`-Finansinspektionen (FI)
*`SIAT`-Securities Market Agency (ATVP)
*`SKNB`-National Bank of Slovakia (NBS)

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | AUAS |
| 2 | ATFM |
| 3 | BEFS |
| 4 | BENB |
| 5 | BGFS |
| 6 | CACS |
| 7 | CYAS |
| 8 | CYCB |
| 9 | CYCY |
| 10 | CZCN |
| 11 | DEBA |
| 12 | DKFI |
| 13 | EEEF |
| 14 | EUES |
| 15 | ESBD |
| 16 | ESCN |
| 17 | FIFS |
| 18 | FRAC |
| 19 | FRAM |
| 20 | GBFS |
| 21 | GBFC |
| 22 | GBPR |
| 23 | GIFS |
| 24 | USCF |
| 25 | GRBO |
| 26 | GRHC |
| 27 | HRHA |
| 28 | HUPS |
| 29 | IECB |
| 30 | ISFM |
| 31 | ITBD |
| 32 | ITCO |
| 33 | LIFM |
| 34 | LTLS |
| 35 | LUCS |
| 36 | LVFK |
| 37 | MTMF |
| 38 | NLAF |
| 39 | NLDN |
| 40 | NOFI |
| 41 | PLKN |
| 42 | PTBP |
| 43 | PTCM |
| 44 | ROAS |
| 45 | SEFI |
| 46 | SIAT |
| 47 | SKNB |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
