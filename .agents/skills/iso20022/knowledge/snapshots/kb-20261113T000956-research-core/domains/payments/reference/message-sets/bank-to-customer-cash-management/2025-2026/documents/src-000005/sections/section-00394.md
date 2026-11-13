---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.14 Charges <Chrgs>"]
file_pages: [592]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.14 Charges <Chrgs>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 592 to 592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

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
4.4.2.14.14  Charges <Chrgs>
Presence: [0..1]
Definition: Provides information on the charges, pre-advised or included in the entry amount.
Usage: This component is used on entry level in case of batch or aggregate bookings.
Charges <Chrgs> contains the following Charges15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 592
   Record <Rcrd> [0..*]  593
     Amount <Amt> [1..1] Amount C2, C6 593
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 594
     ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 594
     Type <Tp> [0..1]  594
{Or       Code <Cd> [1..1] CodeSet 594
Or}       Proprietary <Prtry> [1..1] ± 595
     Rate <Rate> [0..1] Rate 595
     Bearer <Br> [0..1] CodeSet 595
     Agent <Agt> [0..1] ± 595
     Tax <Tax> [0..1]  596
       Identification <Id> [0..1] Text 596
       Rate <Rate> [0..1] Rate 596
       Amount <Amt> [0..1] Amount C2, C6 597
4.4.2.14.14.1  TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt>
Presence: [0..1]
Definition: Total of all charges and taxes applied to the entry.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
592 March 2026
```

