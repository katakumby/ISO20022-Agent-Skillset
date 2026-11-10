---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.5 PartyIdentification126Choice", "66.1.30.5.2 ProprietaryIdentification <PrtryId>"]
file_pages: [4916]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.5.2 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4916 to 4916.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4916

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.30.5.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to the party using a proprietary identification
scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.30.6  CompanyLink1Choice
Definition: Choice of formats for the trading party or broker.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4916
Or}   Proprietary <Prtry> [1..1] ± 4917
66.1.30.6.1  Code <Cd>
Presence: [1..1]
Definition: Company link expressed as a code.
Datatype: "CompanyLink1Code" on page 5285
CodeName Name Definition
AGEN Agent Autonomous agent accredited by the
broker.
BROK Broker Employee, operator or agent of the
broker.
PART BrokeragePartner Brokerage partner or shareholder,
individual or entity who holds a direct or
an indirect control function and the
holder of a management or an
administration position.
MEMB MemberBroker Member broker of a financial
conglomerate (person is a board
member, director, officer and employee
of a member company of the
conglomerate).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4916 May 2026
```

