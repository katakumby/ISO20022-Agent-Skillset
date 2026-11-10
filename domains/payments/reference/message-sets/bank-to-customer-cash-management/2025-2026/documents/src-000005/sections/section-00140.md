---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.20 Tax <Tax>"]
file_pages: [213, 214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.20 Tax <Tax>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 213 to 214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 213

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 835
   OtherIdentification <OthrId> [0..*]  836
     Identification <Id> [1..1] Text 836
     Suffix <Sfx> [0..1] Text 836
     Type <Tp> [1..1] ± 836
   Description <Desc> [0..1] Text 836
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
2.4.2.15.18.2.20  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
213 March 2026
```

## File page 214

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 215
   Debtor <Dbtr> [0..1] ± 215
   UltimateDebtor <UltmtDbtr> [0..1] ± 215
   AdministrationZone <AdmstnZone> [0..1] Text 216
   ReferenceNumber <RefNb> [0..1] Text 216
   Method <Mtd> [0..1] Text 216
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 216
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 217
   Date <Dt> [0..1] Date 217
   SequenceNumber <SeqNb> [0..1] Quantity 217
   Record <Rcrd> [0..*]  217
     Type <Tp> [0..1] Text 218
     Category <Ctgy> [0..1] Text 218
     CategoryDetails <CtgyDtls> [0..1] Text 218
     DebtorStatus <DbtrSts> [0..1] Text 219
     CertificateIdentification <CertId> [0..1] Text 219
     FormsCode <FrmsCd> [0..1] Text 219
     Period <Prd> [0..1]  219
       Year <Yr> [0..1] Year 219
       Type <Tp> [0..1] CodeSet 219
       FromToDate <FrToDt> [0..1] ± 220
     TaxAmount <TaxAmt> [0..1]  221
       Rate <Rate> [0..1] Rate 221
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 221
       TotalAmount <TtlAmt> [0..1] Amount C2, C6 221
       Details <Dtls> [0..*]  222
         Period <Prd> [0..1]  222
           Year <Yr> [0..1] Year 222
           Type <Tp> [0..1] CodeSet 223
           FromToDate <FrToDt> [0..1] ± 223
         Amount <Amt> [1..1] Amount C2, C6 224
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
214 March 2026
```

