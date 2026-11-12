---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.6 TaxRemittance <TaxRmt>"]
file_pages: [1128, 1129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.6 TaxRemittance <TaxRmt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1128 to 1129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1128

```text
Invoicee <Invcee> contains the following elements (see "PartyIdentification272" on page 1193 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1194
   PostalAddress <PstlAdr> [0..1] ± 1195
   Identification <Id> [0..1]  1195
{Or     OrganisationIdentification <OrgId> [1..1]  1196
       AnyBIC <AnyBIC> [0..1] IdentifierSet C4 1197
       LEI <LEI> [0..1] IdentifierSet 1197
       Other <Othr> [0..*]  1197
         Identification <Id> [1..1] Text 1198
         SchemeName <SchmeNm> [0..1]  1198
{Or           Code <Cd> [1..1] CodeSet 1198
Or}           Proprietary <Prtry> [1..1] Text 1198
         Issuer <Issr> [0..1] Text 1198
Or}     PrivateIdentification <PrvtId> [1..1]  1198
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  1199
         BirthDate <BirthDt> [1..1] Date 1199
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1199
         CityOfBirth <CityOfBirth> [1..1] Text 1200
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C10 1200
       Other <Othr> [0..*]  1200
         Identification <Id> [1..1] Text 1200
         SchemeName <SchmeNm> [0..1]  1200
{Or           Code <Cd> [1..1] CodeSet 1201
Or}           Proprietary <Prtry> [1..1] Text 1201
         Issuer <Issr> [0..1] Text 1201
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C10 1201
   ContactDetails <CtctDtls> [0..1] ± 1201
9.4.3.11.11.2.6  TaxRemittance <TaxRmt>
Presence: [0..1]
Definition: Provides remittance information about a payment made for tax-related purposes.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1128 March 2026
```

## File page 1129

```text
TaxRemittance <TaxRmt> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 1130
   Debtor <Dbtr> [0..1] ± 1130
   UltimateDebtor <UltmtDbtr> [0..1] ± 1130
   AdministrationZone <AdmstnZone> [0..1] Text 1131
   ReferenceNumber <RefNb> [0..1] Text 1131
   Method <Mtd> [0..1] Text 1131
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C8 1131
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C8 1132
   Date <Dt> [0..1] Date 1132
   SequenceNumber <SeqNb> [0..1] Quantity 1132
   Record <Rcrd> [0..*]  1132
     Type <Tp> [0..1] Text 1133
     Category <Ctgy> [0..1] Text 1133
     CategoryDetails <CtgyDtls> [0..1] Text 1133
     DebtorStatus <DbtrSts> [0..1] Text 1134
     CertificateIdentification <CertId> [0..1] Text 1134
     FormsCode <FrmsCd> [0..1] Text 1134
     Period <Prd> [0..1]  1134
       Year <Yr> [0..1] Year 1134
       Type <Tp> [0..1] CodeSet 1134
       FromToDate <FrToDt> [0..1] ± 1135
     TaxAmount <TaxAmt> [0..1]  1136
       Rate <Rate> [0..1] Rate 1136
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 1136
       TotalAmount <TtlAmt> [0..1] Amount C2, C8 1136
       Details <Dtls> [0..*]  1137
         Period <Prd> [0..1]  1137
           Year <Yr> [0..1] Year 1137
           Type <Tp> [0..1] CodeSet 1138
           FromToDate <FrToDt> [0..1] ± 1138
         Amount <Amt> [1..1] Amount C2, C8 1139
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1129 March 2026
```

