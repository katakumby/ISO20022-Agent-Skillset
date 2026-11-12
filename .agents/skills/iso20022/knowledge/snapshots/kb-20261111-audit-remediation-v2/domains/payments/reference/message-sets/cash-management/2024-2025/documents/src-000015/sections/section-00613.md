---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.2 ActiveCurrencyAndAmountRange3"]
file_pages: [790]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.2 ActiveCurrencyAndAmountRange3

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 790 to 790.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 790

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
37.1.4.2  ActiveCurrencyAndAmountRange3
Definition: Range of amount values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 790
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 790
   Currency <Ccy> [1..1] CodeSet C1 790
37.1.4.2.1  Amount <Amt>
Presence: [1..1]
Definition: Specified amount or amount range.
Amount <Amt> contains one of the following elements (see "ImpliedCurrencyAmountRange1Choice"
on page 794 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 794
Or   ToAmount <ToAmt> [1..1] ± 795
Or   FromToAmount <FrToAmt> [1..1]  795
     FromAmount <FrAmt> [1..1] ± 795
     ToAmount <ToAmt> [1..1] ± 795
Or   EqualAmount <EQAmt> [1..1] Amount 796
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 796
37.1.4.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the amount is a credited or debited amount.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
37.1.4.2.3  Currency <Ccy>
Presence: [1..1]
Definition: Medium of exchange of value, used to qualify an amount.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 790 February 2025
```

