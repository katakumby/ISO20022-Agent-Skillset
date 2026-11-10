---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "3.4.2.1.8.2 InvoiceTotals <InvcTtls>", "3.4.2.1.8.2.4 PaymentDueDate <PmtDueDt>"]
file_pages: [53, 54, 55]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.8.2.4 PaymentDueDate <PmtDueDt>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 53 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

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
3.4.2.1.8.2.4  PaymentDueDate <PmtDueDt>
Presence: [1..1]
Definition: Due date for the payment of the invoice.
Datatype: "ISODate" on page 148
3.4.2.1.8.2.5  CashAccount <CshAcct>
Presence: [0..1]
Definition: Cash account from which the fees are paid.
CashAccount <CshAcct> contains one of the following elements (see "AccountIdentification4Choice"
on page 114 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C4 114
Or}   Other <Othr> [1..1] ± 114
3.4.2.1.8.3  ServiceCategoryTotals <SvcCtgyTtls>
Presence: [1..*]
Definition: Specifies totals related to the service category.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 53 December 2025
```

## File page 54

```text
ServiceCategoryTotals <SvcCtgyTtls> contains the following ServiceCategoryTotals7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BilledCustomerIdentification <BlldCstmrId> [0..1] ± 56
   Tax <Tax> [0..*]  56
     Rate <Rate> [1..1] Rate 56
     Description <Desc> [0..1] Text 57
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 57
     TaxExemption <TaxXmptn> [0..*]  57
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 57
       Reason <Rsn> [0..1] Text 58
     Amount <Amt> [1..1] Amount C1, C4 58
     ChargesAndFees <ChrgsAndFees> [0..*]  58
       Type <Tp> [0..1] Text 59
       Description <Desc> [0..1] Text 59
       Rate <Rate> [0..1] Rate 59
       Amount <Amt> [0..1] Amount C1, C4 59
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  59
     Amount <Amt> [1..1] Amount C1, C4 60
     ForeignExchange <FX> [0..1] ± 60
   ServiceCategory <SvcCtgy> [1..1]  60
{Or     Code <Cd> [1..1] CodeSet 61
Or}     Proprietary <Prtry> [1..1] Text 61
   ServiceItemTotals <SvcItmTtls> [0..*]  61
     ItemType <ItmTp> [1..1] Text 62
     Description <Desc> [0..1] Text 62
     Quantity <Qty> [1..1] Quantity 63
     BalanceCurrency <BalCcy> [0..1] CodeSet C1 63
     UnitPrice <UnitPric> [0..1] Amount C1, C4 63
     Tax <Tax> [0..*]  63
       Rate <Rate> [1..1] Rate 64
       Description <Desc> [0..1] Text 64
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 64
       TaxExemption <TaxXmptn> [0..*]  65
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 54 December 2025
```

## File page 55

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 65
         Reason <Rsn> [0..1] Text 65
       Amount <Amt> [1..1] Amount C1, C4 65
       ChargesAndFees <ChrgsAndFees> [0..*]  66
         Type <Tp> [0..1] Text 66
         Description <Desc> [0..1] Text 66
         Rate <Rate> [0..1] Rate 66
         Amount <Amt> [0..1] Amount C1, C4 66
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  67
       Amount <Amt> [1..1] Amount C1, C4 67
       ForeignExchange <FX> [0..1] ± 67
   ServiceItemCorrection <SvcItmCrrctn> [0..*]  68
     ItemType <ItmTp> [1..1] Text 69
     Description <Desc> [0..1] Text 69
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 70
     Quantity <Qty> [1..1] Quantity 70
     BalanceCurrency <BalCcy> [0..1] CodeSet C1 70
     UnitPrice <UnitPric> [0..1] Amount C1, C4 70
     Tax <Tax> [0..*]  71
       Rate <Rate> [1..1] Rate 71
       Description <Desc> [0..1] Text 71
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 71
       TaxExemption <TaxXmptn> [0..*]  72
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 72
         Reason <Rsn> [0..1] Text 72
       Amount <Amt> [1..1] Amount C1, C4 72
       ChargesAndFees <ChrgsAndFees> [0..*]  73
         Type <Tp> [0..1] Text 73
         Description <Desc> [0..1] Text 73
         Rate <Rate> [0..1] Rate 73
         Amount <Amt> [0..1] Amount C1, C4 73
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 55 December 2025
```

