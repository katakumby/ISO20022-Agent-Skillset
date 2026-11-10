---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalSystemPartyType1Code"]
code_set: "ExternalSystemPartyType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalSystemPartyType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalSystemPartyType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the system party type, as published in an external system party type code set.
External code sets can be downloaded from www.iso20022.org.
*`SYMG`-Party that defines the eligibility criteria of the system and is responsible for monitoring, controlling and, if necessary, operating the system. All authorizations are available to the system manager when interacting with the system.
*`SYOP`-Party that operates the system on behalf of the system manager (if different from the system manager) and is provided with specific authorizations by the system manager for this purpose.
*`STPU`-Party that owns an account in the system and can interact with the system or counterparties using all use cases available to standard participants.
*`STPR`-Party that owns an account in the system, but only supports a limited range of available use cases in interaction with counterparties.
*`NCBK`-As system participant, the national central bank is the principal monetary authority of a nation and performs several key functions, including issuing currency and regulating the supply of credit in the economy.
*`PMBK`-Commercial bank used to effect money settlements.
*`ANSY`-System in which payments and/or financial instruments are exchanged and/or cleared or recorded, while the ensuing monetary obligations are settled in another system, typically an RTGS system
*`CSDY`-Infrastructure that holds or controls the holding of physical or dematerialized financial instruments belonging to all, or a large portion of, the investors in a securities market. This effects the centralized transfer of ownership of such securities by entries on its books and records.
*`CSDP`-Legal entity or, as the case may be, an individual having a contractual relationship with the CSD for the processing of its securities settlement-related activities in T2S.
*`ECSD`-Infrastructure that holds or controls the holding of physical or dematerialized financial instruments belonging to all, or a large portion of, the investors in a securities market. This effects the centralized transfer of ownership of such securities by entries on its books and records. The infrastructure is external to the system executing the instruction.

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
| 1 | SYMG |
| 2 | SYOP |
| 3 | STPU |
| 4 | STPR |
| 5 | NCBK |
| 6 | PMBK |
| 7 | ANSY |
| 8 | CSDY |
| 9 | CSDP |
| 10 | ECSD |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
