---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.14 Charges <Chrgs>"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.14 Charges <Chrgs>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
AmountDetails <AmtDtls> contains the following elements (see "AmountAndCurrencyExchange4" on
page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructedAmount <InstdAmt> [0..1] ± 802
   TransactionAmount <TxAmt> [0..1] ± 803
   CounterValueAmount <CntrValAmt> [0..1] ± 803
   AnnouncedPostingAmount <AnncdPstngAmt> [0..1] ± 804
   ProprietaryAmount <PrtryAmt> [0..*] ± 804
2.4.2.15.14  Charges <Chrgs>
Presence: [0..1]
Definition: Provides information on the charges, pre-advised or included in the entry amount.
Usage: This component is used on entry level in case of batch or aggregate bookings.
Charges <Chrgs> contains the following Charges15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 74
   Record <Rcrd> [0..*]  75
     Amount <Amt> [1..1] Amount C2, C6 75
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 76
     ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 76
     Type <Tp> [0..1]  76
{Or       Code <Cd> [1..1] CodeSet 76
Or}       Proprietary <Prtry> [1..1] ± 77
     Rate <Rate> [0..1] Rate 77
     Bearer <Br> [0..1] CodeSet 77
     Agent <Agt> [0..1] ± 77
     Tax <Tax> [0..1]  78
       Identification <Id> [0..1] Text 78
       Rate <Rate> [0..1] Rate 78
       Amount <Amt> [0..1] Amount C2, C6 79
2.4.2.15.14.1  TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt>
Presence: [0..1]
Definition: Total of all charges and taxes applied to the entry.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
74 March 2026
```

