---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalSystemEventType1Code"]
code_set: "ExternalSystemEventType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalSystemEventType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalSystemEventType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the type an event generated within a system, as published in an system event type code list.
External code sets can be downloaded from www.iso20022.org.
*`CRCO`-Event is the cutoff for the cash reservation window.
*`CUSC`-Event is the cutoff for customer payments.
*`ESTF`-Event is the cut off for the standing facilities.
*`EUCO`-Event is the cutoff time for the Euro1 system, that is, the deadline for processing Euro1 transactions.
*`EUSU`-Event is the opening of the Euro 1 system operation.
*`FIRE`-Event is the report after all operations have ceased in the system.
*`IBKC`-Event is the cutoff for interbank payments.
*`LTDC`-Event is the cutoff for the settlement of the cash multilateral balances resulting from the daylight cycle of the securities settlement system.
*`LTGC`-Event is the cutoff for the daytime cycle of the securities settlement system.
*`LTNC`-Event is the cutoff for the settlement of the cash multilateral balances resulting from the overnight cycle of the securities settlement system.
*`LVCC`-Event is the cutoff time after which low value payments can no longer be cancelled.
*`LVCO`-Event is the cutoff time for low value payments processed by the system.
*`LVRT`-Event is the time at which the members will be provided with the report corresponding to the processing of low value payments.
*`LWSU`-Event is the start of the limit warning period.
*`NPCT`-Event is the cutoff time for the receipt of new commercial payments.
*`PCOT`-Event is the cutoff time for the processing of payments.
*`RECC`-Event is the cutoff for the settlement of the multilateral balances stemming from the retail clearing system.
*`REOP`-Event is the expected resume time for a TARGET component.
*`SSSC`-Event is the cutoff for the securities settlement system cash reservation window.
*`STDY`-Event is the start of the operating day.
*`STSU`-Event is the start of the Step 1 system operation.
*`SYSC`-Event is the cutoff for the system.

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
| 1 | CRCO |
| 2 | CUSC |
| 3 | ESTF |
| 4 | EUCO |
| 5 | EUSU |
| 6 | FIRE |
| 7 | IBKC |
| 8 | LTDC |
| 9 | LTGC |
| 10 | LTNC |
| 11 | LVCC |
| 12 | LVCO |
| 13 | LVRT |
| 14 | LWSU |
| 15 | NPCT |
| 16 | PCOT |
| 17 | RECC |
| 18 | REOP |
| 19 | SSSC |
| 20 | STDY |
| 21 | STSU |
| 22 | SYSC |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
