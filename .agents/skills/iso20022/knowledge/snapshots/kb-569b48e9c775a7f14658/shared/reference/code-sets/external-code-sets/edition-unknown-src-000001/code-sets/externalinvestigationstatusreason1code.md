---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalInvestigationStatusReason1Code"]
code_set: "ExternalInvestigationStatusReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalInvestigationStatusReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalInvestigationStatusReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the reason for the investigation status, as published in an external investigation status reason code set.
External code sets can be downloaded from www.iso20022.org.
*`AGNT`-Request message has been directed at an incorrect agent or party.
*`DU01`-Request message is duplicate, duplicate request message is rejected.
*`NARR`-See ResponseData element for additional information.
*`FTNA`-Request message forwarded to another agent or party, these may be indicated in NextResponder element.
*`CAPR`-Investigation closed as per the request message.
*`CACR`-Investigation closed as cancellation request for underlying transaction has been sent.
*`ADAC`-Awaiting debit authorisation from customer.
*`ARPL`-Awaiting reply from customer.
*`NOAS`-No reply from customer.
*`INPO`-Collation of response data is still ongoing.
*`NOOR`-Underlying transaction never received.
*`ARJT`-Underlying transaction already rejected.
*`ARDT`-Investigation request not accepted as the transaction has already been returned.
*`RR04`-Regulatory Reason.
*`LEGL`-Reported when the request cannot be accepted because of regulatory rules.
*`ESCA`-Special follow-up is taking place.
*`INIT`-Incorrect investigation type used in request message.
*`PARE`-Response message partially addresses the request, a further response message will follow.
*`NOAD`-No additional information in relation to the request can be provided.
*`G004`-Indicates that the credit claim non receipt investigation is pending as the cover creditor is waiting for the credit of the cover.
*`CMPI`-Is related to a Correction Made as Per Inquiry procedure for investigation status Closed (CLSD).

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
| 1 | AGNT |
| 2 | DU01 |
| 3 | NARR |
| 4 | FTNA |
| 5 | CAPR |
| 6 | CACR |
| 7 | ADAC |
| 8 | ARPL |
| 9 | NOAS |
| 10 | INPO |
| 11 | NOOR |
| 12 | ARJT |
| 13 | ARDT |
| 14 | RR04 |
| 15 | LEGL |
| 16 | ESCA |
| 17 | INIT |
| 18 | PARE |
| 19 | NOAD |
| 20 | G004 |
| 21 | CMPI |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
