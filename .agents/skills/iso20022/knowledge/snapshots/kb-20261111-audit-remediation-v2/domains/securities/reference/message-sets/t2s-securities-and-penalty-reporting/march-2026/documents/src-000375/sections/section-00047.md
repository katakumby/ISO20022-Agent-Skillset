---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.12 SettledQuantity <SttldQty>", "3.4.1.2.12.2 OriginalAndCurrentFace <OrgnlAndCurFace>", "3.4.1.2.12.2.2 AmortisedValue <AmtsdVal>"]
file_pages: [60]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.12.2.2 AmortisedValue <AmtsdVal>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 60 to 60.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
3.4.1.2.12.2.2  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
AmortisedValue <AmtsdVal> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 253 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 253
Or   ToAmount <ToAmt> [1..1] ± 254
Or   FromToAmount <FrToAmt> [1..1]  254
     FromAmount <FrAmt> [1..1] ± 254
     ToAmount <ToAmt> [1..1] ± 254
Or   EqualAmount <EQAmt> [1..1] Amount 255
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 255
3.4.1.2.13  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities.
SettlementAmount <SttlmAmt> contains the following elements (see
"ActiveCurrencyAndAmountRange3" on page 255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 255
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 255
   Currency <Ccy> [1..1] CodeSet C1 256
3.4.1.2.14  SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Total amount of money paid or received in exchange for the securities.
SettledAmount <SttldAmt> contains the following elements (see "ActiveCurrencyAndAmountRange3"
on page 255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 255
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 255
   Currency <Ccy> [1..1] CodeSet C1 256
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 60 March 2026
```

