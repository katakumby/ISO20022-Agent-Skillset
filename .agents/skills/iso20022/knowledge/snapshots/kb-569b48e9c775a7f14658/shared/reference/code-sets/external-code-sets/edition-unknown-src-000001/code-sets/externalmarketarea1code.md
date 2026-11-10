---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalMarketArea1Code"]
code_set: "ExternalMarketArea1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalMarketArea1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalMarketArea1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external market code, to which the instruction, operation or report relates, in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code set published separately.
External code sets can be downloaded from www.iso20022.org.
*`ANYY`-Any market area.
*`CASH`-Bank to bank cash movements.
*`COLL`-Collections.
*`COMM`-Precious metals and other commodities such as palm oil.
*`COPA`-Payment in which one of the parties is not a financial institution.
*`DERI`-Futures contracts, options, forward contracts, swaps, etc...
*`DOCC`-Documentary credits.
*`FOEX`-Foreign exchange.
*`GUAR`-Guarantees.
*`LETT`-Letters of credit.
*`LOAN`-Loans and deposits.
*`MMKT`-Money markets.
*`NDLF`-FX forward trade for which only balance is settled.
*`OFFS`-Offshore settlement.
*`ONSH`-Onshore settlement.
*`OPTI`-FX Options, swap options, etc...
*`SECU`-Bonds, equities, futures...
*`TFIN`-Documentary credits, collections, guarantees, letters of credit.
*`TREA`-Cash management activities.

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
| 1 | ANYY |
| 2 | CASH |
| 3 | COLL |
| 4 | COMM |
| 5 | COPA |
| 6 | DERI |
| 7 | DOCC |
| 8 | FOEX |
| 9 | GUAR |
| 10 | LETT |
| 11 | LOAN |
| 12 | MMKT |
| 13 | NDLF |
| 14 | OFFS |
| 15 | ONSH |
| 16 | OPTI |
| 17 | SECU |
| 18 | TFIN |
| 19 | TREA |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
