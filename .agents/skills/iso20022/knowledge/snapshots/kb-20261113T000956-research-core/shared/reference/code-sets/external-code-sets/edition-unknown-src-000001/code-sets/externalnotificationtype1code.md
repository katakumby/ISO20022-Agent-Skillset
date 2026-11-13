---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalNotificationType1Code"]
code_set: "ExternalNotificationType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalNotificationType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalNotificationType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the notification type, as published in an external notification type code set.
External code sets can be downloaded from www.iso20022.org.
*`CUHO`-Notification of a currency holiday.
*`ATAC`-Notification of new or amended terms and conditions for an account.
*`SUSP`-Notification of a process suspension due to an incident.
*`COUP`-Notification of new or amended contact details.
*`OTHR`-Other notification type.
*`INFO`-Sharing of information.
*`ADDR`-Notification of a change of address.
*`TERM`-Notification of termination of a service, such as an account closure.
*`SSIS`-Notification of a change to Standing Settlement Instructions (SSIs).
*`MERG`-Notification of a merger and any associated changes.
*`SYST`-Request for access to a system.
*`OPEN`-Notification of a change to opening hours.
*`INCH`-Notification of any pertinent industry or market changes.

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
| 1 | CUHO |
| 2 | ATAC |
| 3 | SUSP |
| 4 | COUP |
| 5 | OTHR |
| 6 | INFO |
| 7 | ADDR |
| 8 | TERM |
| 9 | SSIS |
| 10 | MERG |
| 11 | SYST |
| 12 | OPEN |
| 13 | INCH |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
