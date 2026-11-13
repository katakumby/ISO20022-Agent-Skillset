---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.11 Party Identification", "13.1.11.3 PartyIdentification120Choice", "13.1.11.3.2 ProprietaryIdentification <PrtryId>"]
file_pages: [490]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.11.3.2 ProprietaryIdentification <PrtryId>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 490 to 490.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 490

```text
Datatype: "AnyBICDec2014Identifier" on page 530
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
13.1.11.3.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 479 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 480
13.1.11.3.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 495 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 495
   Address <Adr> [0..1] ± 496
13.1.11.4  SystemPartyIdentification8
Definition: Unique and unambiguous identification of a party within a system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 490
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 491
13.1.11.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification to unambiguously identify the party within the system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 490 March 2024
```

