---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>"]
file_pages: [22, 23, 24, 25, 26, 27, 28, 29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2 BillingReportOrError <BllgRptOrErr>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 22 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
3.4.2 BillingReportOrError <BllgRptOrErr>
Presence: [1..1]
Definition: Report on billing data or operational error.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 22 December 2025
```

## File page 23

```text
BillingReportOrError <BllgRptOrErr> contains one of the following BillingReportOrError6Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BillingReport <BllgRpt> [1..1]  30
     RegulatoryData <RgltryData> [1..1]  37
       Invoicer <Invcr> [1..1] ± 37
       Invoicee <Invcee> [1..1] ± 38
       InvoiceLegalStatement <InvcLglStmt> [0..1] Text 39
       PaymentMethod <PmtMtd> [0..1]  40
{Or         Code <Cd> [1..1] CodeSet 40
Or}         Proprietary <Prtry> [1..1] Text 40
     Service <Svc> [0..1]  40
       SystemIdentification <SysId> [1..1] ± 40
       SystemCurrency <SysCcy> [0..1] CodeSet C1 41
     InvoiceDate <InvcDt> [1..1] Date 41
     BillingIdentification <BllgId> [1..1] Text 41
     BillingPeriod <BllgPrd> [1..1] ± 41
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 41
     PartyIdentification <PtyId> [0..1] ± 42
     AccountInvoiceTotals <AcctInvcTtls> [0..*]  42
       AccountIdentification <AcctId> [1..1]  45
{Or         SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 46
Or}         CashAccountIdentification <CshAcctId> [1..1] ± 46
       InvoiceTotals <InvcTtls> [1..1]  46
         Tax <Tax> [0..*]  47
           Rate <Rate> [1..1] Rate 48
           Description <Desc> [0..1] Text 48
           TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 48
           TaxExemption <TaxXmptn> [0..*]  49
             ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 49
             Reason <Rsn> [0..1] Text 49
           Amount <Amt> [1..1] Amount C1, C4 49
           ChargesAndFees <ChrgsAndFees> [0..*]  50
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 23 December 2025
```

## File page 24

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Type <Tp> [0..1] Text 50
             Description <Desc> [0..1] Text 50
             Rate <Rate> [0..1] Rate 50
             Amount <Amt> [0..1] Amount C1, C4 50
         Adjustment <Adjstmnt> [0..1]  51
           Direction <Drctn> [1..1] CodeSet 51
           Amount <Amt> [1..1] Amount C1, C4 51
         TotalInvoiceAmount <TtlInvcAmt> [1..1]  52
           Amount <Amt> [1..1] Amount C1, C4 52
           ForeignExchange <FX> [0..1] ± 52
         PaymentDueDate <PmtDueDt> [1..1] Date 53
         CashAccount <CshAcct> [0..1] ± 53
       ServiceCategoryTotals <SvcCtgyTtls> [1..*]  53
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 24 December 2025
```

## File page 25

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 61
Or}           Proprietary <Prtry> [1..1] Text 61
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 25 December 2025
```

## File page 26

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
           TotalInvoiceAmount <TtlInvcAmt> [1..1]  74
             Amount <Amt> [1..1] Amount C1, C4 74
             ForeignExchange <FX> [0..1] ± 74
     InvoiceTotals <InvcTtls> [0..1]  75
       Tax <Tax> [0..*]  76
         Rate <Rate> [1..1] Rate 77
         Description <Desc> [0..1] Text 77
         TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 77
         TaxExemption <TaxXmptn> [0..*]  78
           ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 78
           Reason <Rsn> [0..1] Text 78
         Amount <Amt> [1..1] Amount C1, C4 78
         ChargesAndFees <ChrgsAndFees> [0..*]  79
           Type <Tp> [0..1] Text 79
           Description <Desc> [0..1] Text 79
           Rate <Rate> [0..1] Rate 79
           Amount <Amt> [0..1] Amount C1, C4 79
       Adjustment <Adjstmnt> [0..1]  80
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 26 December 2025
```

## File page 27

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Direction <Drctn> [1..1] CodeSet 80
         Amount <Amt> [1..1] Amount C1, C4 80
       TotalInvoiceAmount <TtlInvcAmt> [1..1]  81
         Amount <Amt> [1..1] Amount C1, C4 81
         ForeignExchange <FX> [0..1] ± 81
       PaymentDueDate <PmtDueDt> [1..1] Date 82
       CashAccount <CshAcct> [0..1] ± 82
     ServiceCategoryTotals <SvcCtgyTtls> [0..*]  82
       AccountIdentification <AcctId> [0..1]  85
{Or         SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 85
Or}         CashAccountIdentification <CshAcctId> [1..1] ± 85
       ParentAccountIdentification <PrntAcctId> [0..1]  86
{Or         SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 86
Or}         CashAccountIdentification <CshAcctId> [1..1] ± 86
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 27 December 2025
```

## File page 28

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ServiceCategory <SvcCtgy> [1..1]  91
{Or         Code <Cd> [1..1] CodeSet 91
Or}         Proprietary <Prtry> [1..1] Text 91
       ServiceItemTotals <SvcItmTtls> [0..*]  91
         ItemType <ItmTp> [1..1] Text 92
         Description <Desc> [0..1] Text 92
         Quantity <Qty> [1..1] Quantity 92
         UnitPrice <UnitPric> [0..1] Amount C1, C4 93
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 28 December 2025
```

## File page 29

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Rate <Rate> [1..1] Rate 100
           Description <Desc> [0..1] Text 100
           TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 100
           TaxExemption <TaxXmptn> [0..*]  101
             ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 101
             Reason <Rsn> [0..1] Text 101
           Amount <Amt> [1..1] Amount C1, C4 101
           ChargesAndFees <ChrgsAndFees> [0..*]  102
             Type <Tp> [0..1] Text 102
             Description <Desc> [0..1] Text 102
             Rate <Rate> [0..1] Rate 102
             Amount <Amt> [0..1] Amount C1, C4 102
         TotalInvoiceAmount <TtlInvcAmt> [1..1]  103
           Amount <Amt> [1..1] Amount C1, C4 103
           ForeignExchange <FX> [0..1] ± 103
Or   CancellationReport <CxlRpt> [1..1]  104
     RegulatoryData <RgltryData> [0..1]  104
       Invoicer <Invcr> [1..1] ± 105
       Invoicee <Invcee> [1..1] ± 106
       InvoiceLegalStatement <InvcLglStmt> [0..1] Text 107
       PaymentMethod <PmtMtd> [0..1]  108
{Or         Code <Cd> [1..1] CodeSet 108
Or}         Proprietary <Prtry> [1..1] Text 108
     Service <Svc> [0..1]  108
       SystemIdentification <SysId> [1..1] ± 108
       SystemCurrency <SysCcy> [0..1] CodeSet C1 109
     InvoiceDate <InvcDt> [1..1] Date 109
     BillingIdentification <BllgId> [1..1] Text 109
     BillingPeriod <BllgPrd> [1..1] ± 109
     CancellationReason <CxlRsn> [1..1]  109
{Or       Code <Cd> [1..1] Text 110
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 29 December 2025
```

