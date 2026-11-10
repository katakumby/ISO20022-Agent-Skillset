---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.12 Interest <Intrst>", "2.4.2.12.3 FromToDate <FrToDt>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.12.3 FromToDate <FrToDt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
Definition: An amount range where the interest rate is applicable.
ValidityRange <VldtyRg> contains the following elements (see
"ActiveOrHistoricCurrencyAndAmountRange2" on page 813 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 814
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 814
   Currency <Ccy> [1..1] CodeSet C1 814
2.4.2.12.3  FromToDate <FrToDt>
Presence: [0..1]
Definition: Range of time between a start date and an end date for the calculation of the interest.
FromToDate <FrToDt> contains the following elements (see "DateTimePeriod1" on page 828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
2.4.2.12.4  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the interest.
Datatype: "Max35Text" on page 916
2.4.2.12.5  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax applied to charges.
Tax <Tax> contains the following TaxCharges2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 51
   Rate <Rate> [0..1] Rate 52
   Amount <Amt> [0..1] Amount C2, C6 52
2.4.2.12.5.1  Identification <Id>
Presence: [0..1]
Definition: Unique reference to unambiguously identify the nature of the tax levied, such as Value
Added Tax (VAT).
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
51 March 2026
```

