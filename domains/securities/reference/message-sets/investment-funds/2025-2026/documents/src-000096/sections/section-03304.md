---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.7 GenericIdentification82"]
file_pages: [4541]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.7 GenericIdentification82

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4541 to 4541.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4541

```text
Definition: Entity that issues the proprietary identification.
Datatype: "Max35Text" on page 5403
66.1.23.7  GenericIdentification82
Definition: Information related to the identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4541
   Type <Tp> [1..1]  4541
{Or     Code <Cd> [1..1] CodeSet 4541
Or}     Proprietary <Prtry> [1..1] ± 4542
   Issuer <Issr> [0..1] Text 4543
   IssueDate <IsseDt> [0..1] Date 4543
   ExpiryDate <XpryDt> [0..1] Date 4543
   State <Stat> [0..1] Text 4543
   IssuerCountry <IssrCtry> [0..1] CodeSet C12 4543
66.1.23.7.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Datatype: "Max35Text" on page 5403
66.1.23.7.2  Type <Tp>
Presence: [1..1]
Definition: Type of identification.
Type <Tp> contains one of the following OtherIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4541
Or}   Proprietary <Prtry> [1..1] ± 4542
66.1.23.7.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification expressed as a code.
Datatype: "PartyIdentificationType7Code" on page 5336
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4541 May 2026
```

