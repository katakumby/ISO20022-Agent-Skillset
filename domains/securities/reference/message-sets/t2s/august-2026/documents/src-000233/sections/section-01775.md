---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.9 CashAccount <CshAcct>", "71.4.1.2.9.2 ContainText <CTTxt>"]
file_pages: [2438]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.9.2 ContainText <CTTxt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2438 to 2438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2438

```text
71.4.1.2.9.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 3328
71.4.1.2.9.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 3328
71.4.1.2.10  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2438
{Or     FromDate <FrDt> [1..1] Date 2439
Or     ToDate <ToDt> [1..1] Date 2439
Or     FromToDate <FrToDt> [1..1] ± 2439
Or     EqualDate <EQDt> [1..1] Date 2439
Or}     NotEqualDate <NEQDt> [1..1] Date 2439
Or}   DateTime <DtTm> [1..1]  2439
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2440
Or     ToDateTime <ToDtTm> [1..1] DateTime 2440
Or     FromToDateTime <FrToDtTm> [1..1] ± 2440
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2440
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2440
71.4.1.2.10.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2438 August 2026
```

