---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.4 Amount Range", "82.1.4.1 ImpliedCurrencyAmountRange1Choice", "82.1.4.1.5 NotEqualAmount <NEQAmt>"]
file_pages: [2844]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.4.1.5 NotEqualAmount <NEQAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2844 to 2844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2844

```text
82.1.4.1.5  NotEqualAmount <NEQAmt>
Presence: [1..1]
Definition: Value that an amount must not match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 3210
82.1.4.2  ActiveCurrencyAndAmountRange3
Definition: Range of amount values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 2844
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2844
   Currency <Ccy> [1..1] CodeSet C1 2844
82.1.4.2.1  Amount <Amt>
Presence: [1..1]
Definition: Specified amount or amount range.
Amount <Amt> contains one of the following elements (see "ImpliedCurrencyAmountRange1Choice"
on page 2842 for details)
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
82.1.4.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the amount is a credited or debited amount.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
82.1.4.2.3  Currency <Ccy>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2844 August 2026
```

