---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.7 Party Identification", "8.1.7.1 PartyIdentification120Choice", "8.1.7.1.2 ProprietaryIdentification <PrtryId>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.7.1.2 ProprietaryIdentification <PrtryId>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 76
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
8.1.7.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 64 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 64
   Issuer <Issr> [1..1] Text 64
   SchemeName <SchmeNm> [0..1] Text 64
8.1.7.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 70 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 70
   Address <Adr> [0..1] ± 70
8.1.7.2  PartyIdentification136
Definition: Identification of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 69
   LEI <LEI> [0..1] IdentifierSet 69
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 68 December 2024
```

