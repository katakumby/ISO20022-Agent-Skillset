---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.1 Name <Nm>"]
file_pages: [66]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.1 Name <Nm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 66 to 66.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Currency <Ccy> [0..1] CodeSet C1 93
       PendingStandingOrder <PdgStgOrdr> [1..1]  93
         TotalAmount <TtlAmt> [1..1] Amount 94
         CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 94
         Currency <Ccy> [0..1] CodeSet C1 94
     ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 94
Constraints
• BilateralBalanceRule
If MultilateralBalance is not present, then at least one occurrence of CurrentBilateralLimit/
BilateralBalance must be present.
If MultilateralBalance is present, then any occurrence of CurrentBilateralLimit/BilateralBalance is
optional.
On Condition
    /MultilateralBalance[1] is absent
Following Must be True
    /CurrentBilateralLimit[1] Must be present
 And    /CurrentBilateralLimit[1]/BilateralBalance[1] Must be present
3.4.2.1.2.1.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max70Text" on page 890
3.4.2.1.2.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the nature, or use, of the cash account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 786 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 786
Or}   Proprietary <Prtry> [1..1] Text 786
3.4.2.1.2.1.3  Currency <Ccy>
Presence: [0..1]
Definition: Specifies the currency of the cash account.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 66 February 2025
```

