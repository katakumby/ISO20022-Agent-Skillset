---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.19 ClassificationType <ClssfctnTp>", "28.4.2.1.1.2.19.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>"]
file_pages: [1124, 1125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.19.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1124 to 1125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1124

```text
Definition: Information allowing the classification of a financial instrument, for example, with its ISO CFI
(Classification of Financial Instrument) or product type.
ClassificationType <ClssfctnTp> contains the following ClassificationType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1124
   FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1124
   AlternateClassification <AltrnClssfctn> [0..*] ± 1124
28.4.2.1.1.2.19.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 3321
28.4.2.1.1.2.19.2  FinancialInstrumentProductTypeCode <FinInstrmPdctTpCd>
Presence: [0..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstrumentProductType1Code" on page 3242
28.4.2.1.1.2.19.3  AlternateClassification <AltrnClssfctn>
Presence: [0..*]
Definition: Proprietary classification of financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see
"GenericIdentification36" on page 2964 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2965
   Issuer <Issr> [1..1] Text 2965
   SchemeName <SchmeNm> [0..1] Text 2965
28.4.2.1.1.2.20  Issuance <Issnc>
Presence: [0..1]
Definition: Details regarding the issuance of an asset.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1124 August 2026
```

## File page 1125

```text
Issuance <Issnc> contains the following Issuance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 1126
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1126
   IssueDate <IsseDt> [0..1] Date 1126
   AnnouncementDate <AnncmntDt> [0..1] DateTime 1126
   ISINValidFrom <ISINVldFr> [0..1] Date 1126
   IssuerOrganisation <IssrOrg> [0..1]  1126
     Name <Nm> [1..1] Text 1127
     Identification <Id> [0..1]  1127
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1127
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1128
     Purpose <Purp> [0..1] Text 1128
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1128
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1128
     RegistrationDate <RegnDt> [0..1] Date 1129
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1129
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1129
     PostalAddress <PstlAdr> [1..5] ± C10 1129
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1129
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1130
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1130
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1130
   IssueSize <IsseSz> [0..1] Quantity 1131
   IssuePrice <IssePric> [0..1] ± 1131
   IssuanceDistribution <IssncDstrbtn> [0..1]  1131
{Or     Code <Cd> [1..1] CodeSet 1132
Or}     Proprietary <Prtry> [1..1] ± 1132
   GoverningLaw <GovngLaw> [0..*]  1132
     Identification <Id> [0..1] Text 1132
     Country <Ctry> [0..1] CodeSet C4 1132
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1125 August 2026
```

