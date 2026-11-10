---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.7 PartyIdentification <PtyId>"]
file_pages: [42, 43, 44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.7 PartyIdentification <PtyId>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 42 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 123
   LEI <LEI> [0..1] IdentifierSet 123
3.4.2.1.7  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the billed party.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification136" on page 123
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 123
   LEI <LEI> [0..1] IdentifierSet 123
3.4.2.1.8  AccountInvoiceTotals <AcctInvcTtls>
Presence: [0..*]
Definition: Specifies totals related to the invoice per account.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 42 December 2025
```

## File page 43

```text
AccountInvoiceTotals <AcctInvcTtls> contains the following InvoiceTotals8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1]  45
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 46
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 46
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 43 December 2025
```

## File page 44

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       Code <Cd> [1..1] CodeSet 61
Or}       Proprietary <Prtry> [1..1] Text 61
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 44 December 2025
```

