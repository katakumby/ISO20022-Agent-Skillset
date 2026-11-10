---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.24 WorkingCapital <WorkgCptl>"]
file_pages: [4613]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.24 WorkingCapital <WorkgCptl>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4613 to 4613.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4613

```text
EquityValue <EqtyVal> contains the following elements (see "DateAndAmount1" on page 4343 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 4343
   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.24.7.24  WorkingCapital <WorkgCptl>
Presence: [0..1]
Definition: Resource or value owned or used by a third-party company and the date on which the
working capital amount was registered.
WorkingCapital <WorkgCptl> contains the following elements (see "DateAndAmount1" on page 4343
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1] Date 4343
   Amount <Amt> [1..1] Amount C1, C13 4344
66.1.24.7.25  CompanyLink <CpnyLk>
Presence: [0..1]
Definition: Account owner's connection with the trading party or broker.
CompanyLink <CpnyLk> contains one of the following elements (see "CompanyLink1Choice" on
page 4916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4916
Or}   Proprietary <Prtry> [1..1] ± 4917
66.1.24.7.26  ElectronicMailingServiceReference <ElctrncMlngSvcRef>
Presence: [0..1]
Definition: Reference to be specified when a letter, for example, an order confirmation, is sent by an
automated mailing system.
Datatype: "Max350Text" on page 5403
66.1.24.7.27  PrimaryCommunicationAddress <PmryComAdr>
Presence: [0..*]
Definition: Communication device number or electronic address used for communication.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4613 May 2026
```

