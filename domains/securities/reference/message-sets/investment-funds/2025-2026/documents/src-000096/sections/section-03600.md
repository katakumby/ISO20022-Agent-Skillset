---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.3 Treasury <Trsr>"]
file_pages: [4850]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.3 Treasury <Trsr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4850 to 4850.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4850

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.23.3  Treasury <Trsr>
Presence: [0..1]
Definition: Information about the profile for treasury trading.
Treasury <Trsr> contains the following TreasuryProfile1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 4850
   TraderType <TradrTp> [1..1]  4850
{Or     Code <Cd> [1..1] CodeSet 4850
Or}     Proprietary <Prtry> [1..1] ± 4851
   Rate <Rate> [1..1] Rate 4851
66.1.28.23.3.1  Date <Dt>
Presence: [1..1]
Definition: Execution date of treasury bond trade.
Datatype: "ISODate" on page 5388
66.1.28.23.3.2  TraderType <TradrTp>
Presence: [1..1]
Definition: Type of party that performs trading operations, for example, investor or custodian.
TraderType <TradrTp> contains one of the following PartyRole5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4850
Or}   Proprietary <Prtry> [1..1] ± 4851
66.1.28.23.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Role expressed as a code.
Datatype: "PartyRole1Code" on page 5336
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4850 May 2026
```

