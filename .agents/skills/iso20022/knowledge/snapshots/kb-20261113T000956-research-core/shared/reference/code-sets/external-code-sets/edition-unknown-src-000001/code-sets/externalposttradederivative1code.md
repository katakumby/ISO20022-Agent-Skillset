---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPostTradeDerivative1Code"]
code_set: "ExternalPostTradeDerivative1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPostTradeDerivative1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPostTradeDerivative1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Information related to the post trade of derivatives.
*`ILQD`-Flag for transactions executed under the deferral for instruments for which there is not a liquid market.
*`LRGS`-Flag for transactions large in scale relative to normal market size, executed under a permitted post-trade deferral.
*`SIZE`-Flag for transactions executed under the post-trade size specific to the instrument deferral
.
*`DEFF`-Flag for transactions in ETCs, ETNs, SFPs and emission allowances, which benefit from a deferral.

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
| 1 | ILQD |
| 2 | LRGS |
| 3 | SIZE |
| 4 | DEFF |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
