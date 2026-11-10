---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.8 SettlementQuantity <SttlmQty>", "73.4.1.2.8.2 OriginalAndCurrentFace <OrgnlAndCurFace>", "73.4.1.2.8.2.2 AmortisedValue <AmtsdVal>"]
file_pages: [2594]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.8.2.2 AmortisedValue <AmtsdVal>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2594 to 2594.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2594

```text
73.4.1.2.8.2.2  AmortisedValue <AmtsdVal>
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
73.4.1.2.9  SettledQuantity <SttldQty>
Presence: [0..1]
Definition: Quantity of financial instrument effectively settled.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2594 August 2026
```

