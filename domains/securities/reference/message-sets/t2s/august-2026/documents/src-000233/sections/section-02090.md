---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.3 Amount", "82.1.3.5 AmountAndDirection5", "82.1.3.5.2 CreditDebit <CdtDbt>"]
file_pages: [2842]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.3.5.2 CreditDebit <CdtDbt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2842 to 2842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2842

```text
Note: The decimal separator is a dot.
82.1.3.5.2  CreditDebit <CdtDbt>
Presence: [0..1]
Definition: Indicates if the amount is a debited or a credited.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
82.1.4 Amount Range
82.1.4.1  ImpliedCurrencyAmountRange1Choice
Definition: Choice between ranges of values in which an amount is considered valid or a specified
amount value which has to be matched or unmatched to be valid.
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
82.1.4.1.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 2845
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 2845
   Included <Incl> [1..1] Indicator 2845
82.1.4.1.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2842 August 2026
```

