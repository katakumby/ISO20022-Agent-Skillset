---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalDeviceOperatingSystemType1Code"]
code_set: "ExternalDeviceOperatingSystemType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalDeviceOperatingSystemType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalDeviceOperatingSystemType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Type of operating system deployed on device, as published separately in an external device operating system type code set.

External code sets can be downloaded from www.iso20022.org.
*`IOSS`-iOS operating System.
*`DROI`-Android operating system.
*`WIND`-Windows operating system.
*`TIZN`-Tizen operating system.
*`BLCK`-Blackberry operating system.

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
| 1 | IOSS |
| 2 | DROI |
| 3 | WIND |
| 4 | TIZN |
| 5 | BLCK |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
