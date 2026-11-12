---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalIncoterms1Code"]
code_set: "ExternalIncoterms1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalIncoterms1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalIncoterms1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the incoterms, as published in an external incoterms code list.
External code sets can be downloaded from www.iso20022.org.
*`CFR`-Cost and Freight (sea and inland waterway transport) - Incoterms 2010
*`CIF`-Cost, Insurance and Freight (sea and inland waterway transport) - Incoterms 2010
*`CIP`-Carriage and Insurance Paid To (any mode of transport, including multimodal) - Incoterms 2010
*`CPT`-Carriage Paid To (any mode of transport, including multimodal) - Incoterms 2010
*`DAP`-Delivered at Place (any mode of transport, including multimodal) - Incoterms 2010
*`DAT`-Delivered at Terminal (any mode of transport, including multimodal) - Incoterms 2010
*`DDP`-Delivered Duty Paid (any mode of transport, including multimodal) - Incoterms 2010
*`EXW`-Ex Works (any mode of transport, including multimodal) - Incoterms 2010
*`FAS`-Free Alongside Ship (sea and inland waterway transport) - Incoterms 2010
*`FCA`-Free Carrier (any mode of transport, including multimodal) - Incoterms 2010
*`FOB`-Free On Board (sea and inland waterway transport) - Incoterms 2010

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
| 1 | CFR |
| 2 | CIF |
| 3 | CIP |
| 4 | CPT |
| 5 | DAP |
| 6 | DAT |
| 7 | DDP |
| 8 | EXW |
| 9 | FAS |
| 10 | FCA |
| 11 | FOB |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
