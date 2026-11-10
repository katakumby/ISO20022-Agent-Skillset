---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.4 Message Building Blocks", "6.4.1 ReportParameters <RptParams>", "6.4.1.6 ReportNumber <RptNb>"]
file_pages: [239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6.4.1.6 ReportNumber <RptNb>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 239 to 239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 239

```text
CodeName Name Definition
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
ONDE OnDemand Event takes place on demand.
6.4.1.6  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
Datatype: Exact5NumericText on page 492
6.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a report) and continuation indicator to indicate that the
report is to continue or that the message is the last page of the report.
Pagination <Pgntn> contains the following elements (see Pagination on page 440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 440
   LastPageIndicator <LastPgInd> [1..1] Indicator 440
6.4.3 ClearingMember <ClrMmb>
Presence: [1..1]
Definition: Provides the identification of the account owner, that is the clearing member (individual
clearing member or general clearing member).
ClearingMember <ClrMmb> contains one of the following elements (see PartyIdentification35Choice
on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 452
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 452
6.4.4 ReportSummary <RptSummry>
Presence: [0..1]
Definition: Provides details on the valuation of the collateral on deposit.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 239
```

