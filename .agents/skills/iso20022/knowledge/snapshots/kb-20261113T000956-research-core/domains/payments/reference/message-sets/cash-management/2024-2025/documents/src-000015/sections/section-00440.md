---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["22 camt.024.001.08 ModifyStandingOrderV08", "22.4 Message Building Blocks", "22.4.3 NewStandingOrderValueSet <NewStgOrdrValSet>", "22.4.3.1 Amount <Amt>"]
file_pages: [597]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.024.001.08"]
---

# 22.4.3.1 Amount <Amt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 597 to 597.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 597

```text
NewStandingOrderValueSet <NewStgOrdrValSet> contains the following StandingOrder10
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] ± 597
   Creditor <Cdtr> [0..1] ± 598
   CreditorAccount <CdtrAcct> [0..1] ± C8, C7 598
   Debtor <Dbtr> [0..1] ± 599
   DebtorAccount <DbtrAcct> [0..1] ± C8, C7 599
   ExecutionType <ExctnTp> [0..1]  600
{Or     Time <Tm> [1..1] Time 600
Or}     Event <Evt> [1..1]  600
{Or       Code <Cd> [1..1] CodeSet 601
Or}       Proprietary <Prtry> [1..1] Text 601
   Frequency <Frqcy> [0..1] CodeSet 601
   ValidityPeriod <VldtyPrd> [0..1]  601
{Or     FromDate <FrDt> [1..1] Date 602
Or     ToDate <ToDt> [1..1] Date 602
Or}     FromToDate <FrToDt> [1..1] ± 602
   ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 602
Constraints
• ModifyStandingOrderValueSetRule
At least one element must be present.
22.4.3.1  Amount <Amt>
Presence: [0..1]
Definition: Amount of money and currency to be transferred when a payment instruction is created as a
result of a standing order.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 597 February 2025
```

