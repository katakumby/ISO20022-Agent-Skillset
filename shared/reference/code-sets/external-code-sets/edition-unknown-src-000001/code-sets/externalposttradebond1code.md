---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPostTradeBond1Code"]
code_set: "ExternalPostTradeBond1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPostTradeBond1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPostTradeBond1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Information related to the post trade of bonds.
*`FULG`-Full details flag G for Individual transactions in sovereign bonds which have previously benefited from aggregated publication.
*`FULO`-Full details flag O for transactions in a sovereign bond which has previously benefitted from the omission of the publication of the volume.
*`LIF4`-Flag for transactions in bonds benefiting from a deferral applicable to transactions of a large size in a financial instrument for which there is not a liquid market.
*`LLF3`-Flag for transactions in bonds benefiting from a deferral applicable to transactions of a large size in a financial instrument for which there is a liquid market.
*`MTCH`-Flag for matched principal transactions.
*`MIF2`-Flag for transactions in bonds benefiting from a deferral applicable to transactions of a medium size in a financial instrument for which there is not a liquid market.
*`NEGO`-Flag for transactions which are negotiated privately but reported under the rules of a trading venue.
*`MLF1`-Flag for transactions in bonds benefiting from a deferral applicable to transactions of a medium size in a financial instrument for which there is a liquid market.
*`NPFT`-Flag for non-price forming transactions.
*`TPAC`-Flag for package transactions, which are not exchange for physicals.
*`PORT`-Flag for transactions in five or more different financial instruments where those transactions are traded at the same time by the same client.

It is used against a single lot price and that is not a ‘package transaction'.
*`VIF5`-Flag for transactions in bonds benefiting from a deferral applicable to transactions of a very large size in a financial instrument for which there is not a liquid market.
*`VLF5`-Flag for transactions in bonds benefiting from a deferral applicable to transactions of a very large size in a financial instrument for which there is a liquid market
*`OMIS`-Flag for transactions in a sovereign bond which benefits from the omission of the publication of the volume.

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
| 1 | FULG |
| 2 | FULO |
| 3 | LIF4 |
| 4 | LLF3 |
| 5 | MTCH |
| 6 | MIF2 |
| 7 | NEGO |
| 8 | MLF1 |
| 9 | NPFT |
| 10 | TPAC |
| 11 | PORT |
| 12 | VIF5 |
| 13 | VLF5 |
| 14 | OMIS |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
