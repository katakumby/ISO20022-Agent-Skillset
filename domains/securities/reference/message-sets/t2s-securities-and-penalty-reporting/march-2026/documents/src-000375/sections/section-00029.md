---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.9 CashAccount <CshAcct>", "3.4.1.2.9.2 ContainText <CTTxt>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.9.2 ContainText <CTTxt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
3.4.1.2.9.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 557
3.4.1.2.9.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 557
3.4.1.2.10  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  42
{Or     FromDate <FrDt> [1..1] Date 43
Or     ToDate <ToDt> [1..1] Date 43
Or     FromToDate <FrToDt> [1..1] ± 43
Or     EqualDate <EQDt> [1..1] Date 43
Or}     NotEqualDate <NEQDt> [1..1] Date 43
Or}   DateTime <DtTm> [1..1]  43
{Or     FromDateTime <FrDtTm> [1..1] DateTime 44
Or     ToDateTime <ToDtTm> [1..1] DateTime 44
Or     FromToDateTime <FrToDtTm> [1..1] ± 44
Or     EqualDateTime <EQDtTm> [1..1] DateTime 44
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 44
3.4.1.2.10.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 42 March 2026
```

