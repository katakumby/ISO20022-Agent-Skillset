---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.13 Miscellaneous"]
file_pages: [438]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.13 Miscellaneous

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 438 to 438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 438

```text
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
12.1.13 Miscellaneous
12.1.13.1  Statement86
Definition: Provides statement details such as the account owner identification (ie, the clearing member
identification) and optionaly the non clearing member identification, the clearing account or the list of
trade legs.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementIdentification <StmtId> [1..1] Text 438
   StatementDateAndTime <StmtDtAndTm> [1..1] ± 438
   UpdateType <UpdTp> [1..1] CodeSet 439
   Frequency <Frqcy> [1..1] CodeSet 439
   ReportNumber <RptNb> [0..1] Text 439
   ActivityIndicator <ActvtyInd> [1..1] Indicator 439
Constraints
• ReportNumberRule
(Rule)
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
12.1.13.1.1  StatementIdentification <StmtId>
Presence: [1..1]
Definition: Identification that is common to all pages of a statement.
Datatype: Max35Text on page 493
12.1.13.1.2  StatementDateAndTime <StmtDtAndTm>
Presence: [1..1]
Definition: Date of the statement.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 438
```

