---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.9 InvoiceTotals <InvcTtls>", "3.4.2.1.9.4 PaymentDueDate <PmtDueDt>"]
file_pages: [82, 83, 84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.9.4 PaymentDueDate <PmtDueDt>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 82 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms24" on
page 115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 115
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 116
   ExchangeRate <XchgRate> [1..1] Rate 116
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 116
3.4.2.1.9.4  PaymentDueDate <PmtDueDt>
Presence: [1..1]
Definition: Due date for the payment of the invoice.
Datatype: "ISODate" on page 148
3.4.2.1.9.5  CashAccount <CshAcct>
Presence: [0..1]
Definition: Cash account from which the fees are paid.
CashAccount <CshAcct> contains one of the following elements (see "AccountIdentification4Choice"
on page 114 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C4 114
Or}   Other <Othr> [1..1] ± 114
3.4.2.1.10  ServiceCategoryTotals <SvcCtgyTtls>
Presence: [0..*]
Definition: Specifies totals related to the service category.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 82 December 2025
```

## File page 83

```text
ServiceCategoryTotals <SvcCtgyTtls> contains the following ServiceCategoryTotals8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1]  85
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 85
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 85
   ParentAccountIdentification <PrntAcctId> [0..1]  86
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 86
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 86
   BilledCustomerIdentification <BlldCstmrId> [0..1] ± 86
   Tax <Tax> [0..*]  87
     Rate <Rate> [1..1] Rate 87
     Description <Desc> [0..1] Text 87
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 87
     TaxExemption <TaxXmptn> [0..*]  88
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 88
       Reason <Rsn> [0..1] Text 88
     Amount <Amt> [1..1] Amount C1, C4 89
     ChargesAndFees <ChrgsAndFees> [0..*]  89
       Type <Tp> [0..1] Text 89
       Description <Desc> [0..1] Text 89
       Rate <Rate> [0..1] Rate 90
       Amount <Amt> [0..1] Amount C1, C4 90
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  90
     Amount <Amt> [1..1] Amount C1, C4 90
     ForeignExchange <FX> [0..1] ± 91
   ServiceCategory <SvcCtgy> [1..1]  91
{Or     Code <Cd> [1..1] CodeSet 91
Or}     Proprietary <Prtry> [1..1] Text 91
   ServiceItemTotals <SvcItmTtls> [0..*]  91
     ItemType <ItmTp> [1..1] Text 92
     Description <Desc> [0..1] Text 92
     Quantity <Qty> [1..1] Quantity 92
     UnitPrice <UnitPric> [0..1] Amount C1, C4 93
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 83 December 2025
```

## File page 84

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Tax <Tax> [0..*]  93
       Rate <Rate> [1..1] Rate 94
       Description <Desc> [0..1] Text 94
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 94
       TaxExemption <TaxXmptn> [0..*]  94
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 94
         Reason <Rsn> [0..1] Text 95
       Amount <Amt> [1..1] Amount C1, C4 95
       ChargesAndFees <ChrgsAndFees> [0..*]  95
         Type <Tp> [0..1] Text 96
         Description <Desc> [0..1] Text 96
         Rate <Rate> [0..1] Rate 96
         Amount <Amt> [0..1] Amount C1, C4 96
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  96
       Amount <Amt> [1..1] Amount C1, C4 97
       ForeignExchange <FX> [0..1] ± 97
   ServiceItemCorrection <SvcItmCrrctn> [0..*]  97
     ItemType <ItmTp> [1..1] Text 98
     Description <Desc> [0..1] Text 98
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 99
     Quantity <Qty> [1..1] Quantity 99
     UnitPrice <UnitPric> [0..1] Amount C1, C4 99
     Tax <Tax> [0..*]  99
       Rate <Rate> [1..1] Rate 100
       Description <Desc> [0..1] Text 100
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 100
       TaxExemption <TaxXmptn> [0..*]  101
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 101
         Reason <Rsn> [0..1] Text 101
       Amount <Amt> [1..1] Amount C1, C4 101
       ChargesAndFees <ChrgsAndFees> [0..*]  102
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 84 December 2025
```

