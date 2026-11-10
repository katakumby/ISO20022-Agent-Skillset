---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.2 Pagination <Pgntn>"]
file_pages: [326]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.2 Pagination <Pgntn>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 326 to 326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 326

```text
ReportDateAndTime <RptDtAndTm> contains one of the following elements (see
DateAndDateTime2Choice on page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
11.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a report) and continuation indicator to indicate that the
report is to continue or that the message is the last page of the report.
Pagination <Pgntn> contains the following elements (see Pagination1 on page 439 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 440
   LastPageIndicator <LastPgInd> [1..1] Indicator 440
11.4.3 ClearingMember <ClrMmb>
Presence: [0..1]
Definition: Provides the identification of the clearing member (individual clearing member or general
clearing member).
ClearingMember <ClrMmb> contains one of the following elements (see PartyIdentification253Choice
on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
11.4.4 ClearingSegment <ClrSgmt>
Presence: [0..1]
Definition: Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, Clearing Member Firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 326
```

