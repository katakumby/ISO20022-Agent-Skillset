---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.9 SettledQuantity <SttldQty>", "2.4.1.2.9.2 OriginalAndCurrentFace <OrgnlAndCurFace>", "2.4.1.2.9.2.2 AmortisedValue <AmtsdVal>"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.9.2.2 AmortisedValue <AmtsdVal>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
2.4.1.2.9.2.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
AmortisedValue <AmtsdVal> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 195 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 195
Or   ToAmount <ToAmt> [1..1] ± 195
Or   FromToAmount <FrToAmt> [1..1]  196
     FromAmount <FrAmt> [1..1] ± 196
     ToAmount <ToAmt> [1..1] ± 196
Or   EqualAmount <EQAmt> [1..1] Amount 196
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 197
2.4.1.2.10  IntendedSettlementDate <IntnddSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are intended to be moved.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  48
{Or     FromDate <FrDt> [1..1] Date 48
Or     ToDate <ToDt> [1..1] Date 48
Or     FromToDate <FrToDt> [1..1] ± 48
Or     EqualDate <EQDt> [1..1] Date 48
Or}     NotEqualDate <NEQDt> [1..1] Date 48
Or}   DateTime <DtTm> [1..1]  49
{Or     FromDateTime <FrDtTm> [1..1] DateTime 49
Or     ToDateTime <ToDtTm> [1..1] DateTime 49
Or     FromToDateTime <FrToDtTm> [1..1] ± 49
Or     EqualDateTime <EQDtTm> [1..1] DateTime 49
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 49
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 47 September 2025
```

