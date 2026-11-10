---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.1 Amount <Amt>"]
file_pages: [722]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.1 Amount <Amt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 722 to 722.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 722

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  731
       TotalAmount <TtlAmt> [1..1] Amount 732
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 732
       Currency <Ccy> [0..1] CodeSet C1 732
     SetStandingOrder <SetStgOrdr> [1..1]  732
       TotalAmount <TtlAmt> [1..1] Amount 733
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 733
       Currency <Ccy> [0..1] CodeSet C1 733
     PendingStandingOrder <PdgStgOrdr> [1..1]  733
       TotalAmount <TtlAmt> [1..1] Amount 734
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 734
       Currency <Ccy> [0..1] CodeSet C1 734
   ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 734
31.4.2.1.2.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money and currency to be transferred when a payment instruction is created as a
result of a standing order.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
31.4.2.1.2.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies if the account is debited or credited by the standing order.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
31.4.2.1.2.1.3  Currency <Ccy>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 722 February 2025
```

