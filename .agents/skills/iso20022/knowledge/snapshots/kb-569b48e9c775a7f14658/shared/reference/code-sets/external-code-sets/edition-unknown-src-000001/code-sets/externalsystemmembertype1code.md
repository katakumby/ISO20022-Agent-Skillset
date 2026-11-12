---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalSystemMemberType1Code"]
code_set: "ExternalSystemMemberType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalSystemMemberType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalSystemMemberType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the nature of the membership of a party in a system, as published in an external system member type code set.
External code sets can be downloaded from www.iso20022.org.
*`DRCT`-Member has full rights in the system. In principle, this membership status entails financial responsibility for its own operations and sponsored members' operations submitted to the system.
*`IDRT`-Member has limited rights in the system specifications. In principle, this membership status entails no financial responsibility for its operations submitted to the system.
*`RMTE`-Member has access to the system from a remote location or through remote technical means.
*`EURO`-Member is entitled to access the Euro1 system of the Euro Banking Association (EBA).
*`STEP`-Member is entitled to access the Step1 system of the Euro Banking Association (EBA).

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
| 1 | DRCT |
| 2 | IDRT |
| 3 | RMTE |
| 4 | EURO |
| 5 | STEP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
