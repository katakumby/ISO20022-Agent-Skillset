---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.4 Amount Range", "7.1.4.1 ImpliedCurrencyAmountRange1Choice", "7.1.4.1.4 EqualAmount <EQAmt>"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.4.1.4 EqualAmount <EQAmt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
7.1.4.1.4  EqualAmount <EQAmt>
Presence: [1..1]
Definition: Exact value an amount must match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.4.1.5  NotEqualAmount <NEQAmt>
Presence: [1..1]
Definition: Value that an amount must not match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.4.2  ActiveCurrencyAndAmountRange3
Definition: Range of amount values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 255
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 255
   Currency <Ccy> [1..1] CodeSet C1 256
7.1.4.2.1  Amount <Amt>
Presence: [1..1]
Definition: Specified amount or amount range.
Amount <Amt> contains one of the following elements (see "ImpliedCurrencyAmountRange1Choice"
on page 253 for details)
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
7.1.4.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the amount is a credited or debited amount.
Datatype: "CreditDebitCode" on page 501
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 255 March 2026
```

