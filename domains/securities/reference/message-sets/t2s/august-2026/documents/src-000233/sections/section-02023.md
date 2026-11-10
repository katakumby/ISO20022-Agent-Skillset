---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "80.4 Message Building Blocks", "80.4.1 Pagination <Pgntn>"]
file_pages: [2754]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 80.4.1 Pagination <Pgntn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2754 to 2754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2754

```text
80.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
80.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: Provides general information on the report.
Impacted by: C30 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following elements (see "Statement58" on
page 3019 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryReference <QryRef> [0..1] Text 3020
   ReportIdentification <RptId> [0..1] Text 3020
   HistoricData <HstrcData> [1..1] Indicator 3020
   ActivityIndicator <ActvtyInd> [1..1] Indicator 3020
   SubAccountIndicator <SubAcctInd> [1..1] Indicator 3021
Constraints
• ReportNumberRule
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
80.4.3 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2754 August 2026
```

