---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalChannel1Code"]
code_set: "ExternalChannel1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalChannel1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalChannel1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external submission or presentation channel code in the format of a character string with a maximum length of 4 characters. The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`COUR`-Delivery by courier.
*`EMAL`-Transmission by e-mail.
*`FAXI`-Transmission by fax.
*`MESS`-Delivery by messenger.
*`POST`-Delivery by postal service.
*`REGM`-Delivery by registered mail services.
*`SEMA`-Transfer via secure e-mail.
*`SWFA`-Transmission by SWIFTNet FileAct.
*`SWIA`-Transmission by SWIFTNet InterAct.
*`SWMT`-Transmission by SWIFT (FIN).
*`SWMX`-Transmission by SWIFTNet.
*`TELE`-Transmission by telecommunications service.
*`WEBM`-Available via Web upload/download

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
| 1 | COUR |
| 2 | EMAL |
| 3 | FAXI |
| 4 | MESS |
| 5 | POST |
| 6 | REGM |
| 7 | SEMA |
| 8 | SWFA |
| 9 | SWIA |
| 10 | SWMT |
| 11 | SWMX |
| 12 | TELE |
| 13 | WEBM |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
