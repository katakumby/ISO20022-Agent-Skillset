---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.10 SettlementDate <SttlmDt>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.10 SettlementDate <SttlmDt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
2.4.6.10  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Provides the contractual settlement date.
SettlementDate <SttlmDt> contains one of the following DateFormat66Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 44
Or}   DateCode <DtCd> [1..1]  44
{Or     Code <Cd> [1..1] CodeSet 44
Or}     Proprietary <Prtry> [1..1] ± 44
2.4.6.10.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: ISODate on page 487
2.4.6.10.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date is expressed using a code.
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 44
Or}   Proprietary <Prtry> [1..1] ± 44
2.4.6.10.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
2.4.6.10.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 44
```

