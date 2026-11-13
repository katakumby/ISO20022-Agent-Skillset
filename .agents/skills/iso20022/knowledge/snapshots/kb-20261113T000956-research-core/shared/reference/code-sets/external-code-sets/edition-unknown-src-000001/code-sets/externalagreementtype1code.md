---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalAgreementType1Code"]
code_set: "ExternalAgreementType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalAgreementType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalAgreementType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the name of the identification scheme, as published in an external agreement type code set.
External code sets can be downloaded from www.iso20022.org.
*`AUSL`-Australian Masters Securities Lending Agreement (AMSLA).
*`BIAG`-Bilateral agreement.
*`CARA`-Investment Industry Regulatory Organization of Canada (IIROC) Repurchase/Reverse Repurchase Transaction Agreement.
*`CDEA`-FIA-ISDA Cleared Derivatives Execution Agreement.
*`CHMA`-Swiss Master Agreement.
*`CHRA`-Swiss Master Repurchase Agreement.
*`CMOP`-Contrato Marco de Operaciones Financieras.
*`CNBR`-China Bond Repurchase Master Agreement.
*`CSDA`-CSD bilateral agreement.
*`DEMA`-German Master Agreement.
*`DERD`-Deutscher Rahmenvertrag für Wertpapierdarlehen.
*`DERP`-Deutscher Rahmenvertrag für Wertpapierpensionsgeschäfte .
*`DERV`-Deutscher Rahmenvertrag für Finanztermingeschäfte (DRV).
*`EFMA`-EFET Master Agreement.
*`ESRA`-Contrato Marco de compraventa y Reporto de valores.
*`EUMA`-European Master Agreement.
*`FMAT`-FBF Master Agreement related to transactions on forward financial instruments.
*`FPCA`-FOA Professional Client Agreement.
*`FRFB`-Convention-Cadre Relative aux Operations de Pensions Livrees.
*`GESL`-Gilt Edged Stock Lending Agreement (GESLA).
*`GMRA`-Global Master Repurchase Agreement.
*`GMSL`-Global Master Securities Lending Agreement.
*`IDMA`-Islamic Derivative Master Agreement.
*`ISDA`-International Swaps and Derivatives Association Agreement.
*`JPBL`-Japanese Master Agreement on Lending Transaction of Bonds.
*`JPBR`-Japanese Master Agreement on the Transaction with Repurchase Agreement of the Bonds.
*`JPSL`-Japanese Master Agreement on the Borrowing and Lending Transactions of Share Certificates.
*`KRRA`-Korea Financial Investment Association (KOFIA) Standard Repurchase Agreement.
*`KRSL`-Korean Securities Lending Agreement (KOSLA).
*`MEFI`-Master Equity and Fixed Interest Stock Lending Agreement (MEFISLA).
*`MRAA`-Master Repurchase Agreement.
*`MSLA`-Master Securities Loan Agreement.
*`OSLA`-Overseas Securities Lending Agreement.
*`OTHR`-Other type of master agreement.

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
| 1 | AUSL |
| 2 | BIAG |
| 3 | CARA |
| 4 | CDEA |
| 5 | CHMA |
| 6 | CHRA |
| 7 | CMOP |
| 8 | CNBR |
| 9 | CSDA |
| 10 | DEMA |
| 11 | DERD |
| 12 | DERP |
| 13 | DERV |
| 14 | EFMA |
| 15 | ESRA |
| 16 | EUMA |
| 17 | FMAT |
| 18 | FPCA |
| 19 | FRFB |
| 20 | GESL |
| 21 | GMRA |
| 22 | GMSL |
| 23 | IDMA |
| 24 | ISDA |
| 25 | JPBL |
| 26 | JPBR |
| 27 | JPSL |
| 28 | KRRA |
| 29 | KRSL |
| 30 | MEFI |
| 31 | MRAA |
| 32 | MSLA |
| 33 | OSLA |
| 34 | OTHR |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
