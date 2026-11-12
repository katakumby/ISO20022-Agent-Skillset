---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.6 TaxRemittance <TaxRmt>"]
file_pages: [111, 112]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.6 TaxRemittance <TaxRmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 111 to 112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 111

```text
Invoicee <Invcee> contains the following elements (see "PartyIdentification272" on page 554 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 555
   PostalAddress <PstlAdr> [0..1] ± 556
   Identification <Id> [0..1]  556
{Or     OrganisationIdentification <OrgId> [1..1]  557
       AnyBIC <AnyBIC> [0..1] IdentifierSet C3 558
       LEI <LEI> [0..1] IdentifierSet 558
       Other <Othr> [0..*]  558
         Identification <Id> [1..1] Text 559
         SchemeName <SchmeNm> [0..1]  559
{Or           Code <Cd> [1..1] CodeSet 559
Or}           Proprietary <Prtry> [1..1] Text 559
         Issuer <Issr> [0..1] Text 559
Or}     PrivateIdentification <PrvtId> [1..1]  559
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  560
         BirthDate <BirthDt> [1..1] Date 560
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 560
         CityOfBirth <CityOfBirth> [1..1] Text 561
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C18 561
       Other <Othr> [0..*]  561
         Identification <Id> [1..1] Text 561
         SchemeName <SchmeNm> [0..1]  561
{Or           Code <Cd> [1..1] CodeSet 562
Or}           Proprietary <Prtry> [1..1] Text 562
         Issuer <Issr> [0..1] Text 562
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C18 562
   ContactDetails <CtctDtls> [0..1] ± 562
2.4.2.19.26.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 111 March 2026
```

## File page 112

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 113
   Debtor <Dbtr> [0..1] ± 113
   UltimateDebtor <UltmtDbtr> [0..1] ± 113
   AdministrationZone <AdmstnZone> [0..1] Text 114
   ReferenceNumber <RefNb> [0..1] Text 114
   Method <Mtd> [0..1] Text 114
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C19 114
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C19 115
   Date <Dt> [0..1] Date 115
   SequenceNumber <SeqNb> [0..1] Quantity 115
   Record <Rcrd> [0..*]  115
     Type <Tp> [0..1] Text 116
     Category <Ctgy> [0..1] Text 116
     CategoryDetails <CtgyDtls> [0..1] Text 116
     DebtorStatus <DbtrSts> [0..1] Text 117
     CertificateIdentification <CertId> [0..1] Text 117
     FormsCode <FrmsCd> [0..1] Text 117
     Period <Prd> [0..1]  117
       Year <Yr> [0..1] Year 117
       Type <Tp> [0..1] CodeSet 117
       FromToDate <FrToDt> [0..1] ± 118
     TaxAmount <TaxAmt> [0..1]  119
       Rate <Rate> [0..1] Rate 119
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C19 119
       TotalAmount <TtlAmt> [0..1] Amount C2, C19 119
       Details <Dtls> [0..*]  120
         Period <Prd> [0..1]  120
           Year <Yr> [0..1] Year 120
           Type <Tp> [0..1] CodeSet 121
           FromToDate <FrToDt> [0..1] ± 121
         Amount <Amt> [1..1] Amount C2, C19 122
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 112 March 2026
```

