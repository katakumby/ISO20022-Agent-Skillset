---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.5 PartyIdentification33Choice", "12.1.14.5.1 AnyBIC <AnyBIC>"]
file_pages: [448]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.5.1 AnyBIC <AnyBIC>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 448 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 448

```text
12.1.14.5.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Impacted by:   'C4 AnyBIC  '
Datatype: AnyBICIdentifier on page 488
Constraints
• AnyBIC
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
12.1.14.5.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see GenericIdentification29 on
page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 396
   Issuer <Issr> [1..1] Text 397
   SchemeName <SchmeNm> [0..1] Text 397
12.1.14.5.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
NameAndAddress <NmAndAdr> contains the following NameAndAddress6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 449
   Address <Adr> [1..1] ± 449
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 448
```

