---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.24 SimpleIdentificationInformation"]
file_pages: [4555]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.24 SimpleIdentificationInformation

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4555 to 4555.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4555

```text
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 5403
66.1.23.24  SimpleIdentificationInformation
Definition: Information related to an identification, eg, party identification or account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4555
66.1.23.24.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, eg, account
identifier.
Datatype: "Max35Text" on page 5403
66.1.24 Investment Account
66.1.24.1  AccountUsageType2Choice
Definition: Choice of formats for the specification of the type of account usage.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4555
Or}   Proprietary <Prtry> [1..1] ± 4555
66.1.24.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of account usage expressed as a code.
Datatype: "AccountUsageType2Code" on page 5275
CodeName Name Definition
INVE Investor Investor.
ISSP IssuingParticipant Issuing participant.
SETP SettlementParticipant Settlement participant.
TRDP TradingParticipant Trading participant.
66.1.24.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of account usage expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4555 May 2026
```

