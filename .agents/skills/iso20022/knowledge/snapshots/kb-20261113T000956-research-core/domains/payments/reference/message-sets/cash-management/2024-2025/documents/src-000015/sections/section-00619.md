---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.7 ImpliedCurrencyAmountRange1Choice", "37.1.4.7.4 EqualAmount <EQAmt>"]
file_pages: [796]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.7.4 EqualAmount <EQAmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 796 to 796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 796

```text
37.1.4.7.4  EqualAmount <EQAmt>
Presence: [1..1]
Definition: Exact value an amount must match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 848
37.1.4.7.5  NotEqualAmount <NEQAmt>
Presence: [1..1]
Definition: Value that an amount must not match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 848
37.1.5 Balance
37.1.5.1  CashBalance13
Definition: Balance details for a cash account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount 796
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 797
   Type <Tp> [0..1]  797
{Or     Code <Cd> [1..1] CodeSet 797
Or}     Proprietary <Prtry> [1..1] Text 797
   Status <Sts> [0..1] CodeSet 797
   ValueDate <ValDt> [0..1] ± 797
   ProcessingDate <PrcgDt> [0..1] ± 798
   NumberOfPayments <NbOfPmts> [0..1] Quantity 798
   RestrictionType <RstrctnTp> [0..1]  798
     Type <Tp> [1..1] ± 798
     Description <Desc> [0..1] Text 799
     ProcessingType <PrcgTp> [0..1]  799
{Or       Code <Cd> [1..1] CodeSet 799
Or}       Proprietary <Prtry> [1..1] Text 800
37.1.5.1.1  Amount <Amt>
Presence: [1..1]
Definition: Currency and amount of money of the cash balance.
Datatype: "ImpliedCurrencyAndAmount" on page 848
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 796 February 2025
```

