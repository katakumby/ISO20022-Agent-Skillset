---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.9 SettledQuantity <SttldQty>", "73.4.1.2.9.2 OriginalAndCurrentFace <OrgnlAndCurFace>", "73.4.1.2.9.2.2 AmortisedValue <AmtsdVal>"]
file_pages: [2602]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.9.2.2 AmortisedValue <AmtsdVal>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2602 to 2602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2602

```text
73.4.1.2.9.2.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
AmortisedValue <AmtsdVal> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 2842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 2842
Or   ToAmount <ToAmt> [1..1] ± 2842
Or   FromToAmount <FrToAmt> [1..1]  2843
     FromAmount <FrAmt> [1..1] ± 2843
     ToAmount <ToAmt> [1..1] ± 2843
Or   EqualAmount <EQAmt> [1..1] Amount 2843
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 2844
73.4.1.2.10  IntendedSettlementDate <IntnddSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are intended to be moved.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2603
{Or     FromDate <FrDt> [1..1] Date 2603
Or     ToDate <ToDt> [1..1] Date 2603
Or     FromToDate <FrToDt> [1..1] ± 2603
Or     EqualDate <EQDt> [1..1] Date 2603
Or}     NotEqualDate <NEQDt> [1..1] Date 2603
Or}   DateTime <DtTm> [1..1]  2604
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2604
Or     ToDateTime <ToDtTm> [1..1] DateTime 2604
Or     FromToDateTime <FrToDtTm> [1..1] ± 2604
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2604
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2604
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2602 August 2026
```

