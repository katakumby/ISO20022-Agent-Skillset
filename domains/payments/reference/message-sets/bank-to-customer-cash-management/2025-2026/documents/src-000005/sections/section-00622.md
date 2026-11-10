---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.8 TransactionInterest4", "6.1.15.8.2 Record <Rcrd>", "6.1.15.8.2.4 Rate <Rate>", "6.1.15.8.2.4.1 Type <Tp>"]
file_pages: [855]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.8.2.4.1 Type <Tp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 855 to 855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 855

```text
Rate <Rate> contains the following Rate4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 855
   ValidityRange <VldtyRg> [0..1] ± 855
6.1.15.8.2.4.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of interest rate.
Type <Tp> contains one of the following elements (see "RateType4Choice" on page 881 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Percentage <Pctg> [1..1] Rate 881
Or}   Other <Othr> [1..1] Text 881
6.1.15.8.2.4.2  ValidityRange <VldtyRg>
Presence: [0..1]
Definition: An amount range where the interest rate is applicable.
ValidityRange <VldtyRg> contains the following elements (see
"ActiveOrHistoricCurrencyAndAmountRange2" on page 813 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 814
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 814
   Currency <Ccy> [1..1] CodeSet C1 814
6.1.15.8.2.5  FromToDate <FrToDt>
Presence: [0..1]
Definition: Range of time between a start date and an end date for the calculation of the interest.
FromToDate <FrToDt> contains the following elements (see "DateTimePeriod1" on page 828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
6.1.15.8.2.6  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the interest.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
855 March 2026
```

