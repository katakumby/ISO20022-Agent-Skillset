---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.14 Party Identification", "17.1.14.1 PartyIdentification136", "17.1.14.1.1 Identification <Id>"]
file_pages: [418]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.14.1.1 Identification <Id>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 418 to 418.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 418

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 418
   LEI <LEI> [0..1] IdentifierSet 418
17.1.14.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 418 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 418
Or   ProprietaryIdentification <PrtryId> [1..1] ± 419
Or}   NameAndAddress <NmAndAdr> [1..1] ± 419
17.1.14.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 494
17.1.14.2  PartyIdentification120Choice
Definition: Choice between different formats for the identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 418
Or   ProprietaryIdentification <PrtryId> [1..1] ± 419
Or}   NameAndAddress <NmAndAdr> [1..1] ± 419
17.1.14.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 493
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
418 March 2024
```

