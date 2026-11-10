---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.6 Date Time"]
file_pages: [388]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.6 Date Time

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 388 to 388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 388

```text
12.1.6 Date Time
12.1.6.1  DateFormat65Choice
Definition: Choice between an ISODate or ISODateTime format or a date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 388
Or}   DateCode <DtCd> [1..1]  388
{Or     Code <Cd> [1..1] CodeSet 388
Or}     Proprietary <Prtry> [1..1] ± 389
12.1.6.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Date <Dt> contains one of the following elements (see DateAndDateTime2Choice on page 390 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
12.1.6.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Specifies the type of date.
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 388
Or}   Proprietary <Prtry> [1..1] ± 389
12.1.6.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 388
```

