---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.2.2.19 ClassificationType <ClssfctnTp>", "28.4.2.1.2.2.19.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>"]
file_pages: [1312, 1313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.2.19.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1312 to 1313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1312

```text
Definition: Information allowing the classification of a financial instrument, for example, with its ISO CFI
(Classification of Financial Instrument) or product type.
ClassificationType <ClssfctnTp> contains the following ClassificationType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1312
   FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1312
   AlternateClassification <AltrnClssfctn> [0..*] ± 1312
28.4.2.1.2.2.19.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 3321
28.4.2.1.2.2.19.2  FinancialInstrumentProductTypeCode <FinInstrmPdctTpCd>
Presence: [0..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstrumentProductType1Code" on page 3242
28.4.2.1.2.2.19.3  AlternateClassification <AltrnClssfctn>
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
28.4.2.1.2.2.20  Issuance <Issnc>
Presence: [0..1]
Definition: Details regarding the issuance of an asset.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1312 August 2026
```

## File page 1313

```text
Issuance <Issnc> contains the following Issuance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 1314
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1314
   IssueDate <IsseDt> [0..1] Date 1314
   AnnouncementDate <AnncmntDt> [0..1] DateTime 1314
   ISINValidFrom <ISINVldFr> [0..1] Date 1314
   IssuerOrganisation <IssrOrg> [0..1]  1314
     Name <Nm> [1..1] Text 1315
     Identification <Id> [0..1]  1315
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1315
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1316
     Purpose <Purp> [0..1] Text 1316
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1316
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1316
     RegistrationDate <RegnDt> [0..1] Date 1317
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1317
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1317
     PostalAddress <PstlAdr> [1..5] ± C10 1317
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1317
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1318
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1318
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1318
   IssueSize <IsseSz> [0..1] Quantity 1319
   IssuePrice <IssePric> [0..1] ± 1319
   IssuanceDistribution <IssncDstrbtn> [0..1]  1319
{Or     Code <Cd> [1..1] CodeSet 1320
Or}     Proprietary <Prtry> [1..1] ± 1320
   GoverningLaw <GovngLaw> [0..*]  1320
     Identification <Id> [0..1] Text 1320
     Country <Ctry> [0..1] CodeSet C4 1320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1313 August 2026
```

