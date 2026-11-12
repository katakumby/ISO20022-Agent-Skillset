---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.19 ClassificationType <ClssfctnTp>"]
file_pages: [260, 261]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.19 ClassificationType <ClssfctnTp>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 260 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
13.1.6.2.19  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Information allowing the classification of a financial instrument, for example, with its ISO CFI
(Classification of Financial Instrument) or product type.
ClassificationType <ClssfctnTp> contains the following ClassificationType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 260
   FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 260
   AlternateClassification <AltrnClssfctn> [0..*] ± 260
13.1.6.2.19.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 530
13.1.6.2.19.2  FinancialInstrumentProductTypeCode <FinInstrmPdctTpCd>
Presence: [0..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstrumentProductType1Code" on page 514
13.1.6.2.19.3  AlternateClassification <AltrnClssfctn>
Presence: [0..*]
Definition: Proprietary classification of financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see
"GenericIdentification36" on page 479 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 480
13.1.6.2.20  Issuance <Issnc>
Presence: [0..1]
Definition: Details regarding the issuance of an asset.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 260 March 2024
```

## File page 261

```text
Issuance <Issnc> contains the following Issuance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 262
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 262
   IssueDate <IsseDt> [0..1] Date 262
   AnnouncementDate <AnncmntDt> [0..1] DateTime 262
   ISINValidFrom <ISINVldFr> [0..1] Date 262
   IssuerOrganisation <IssrOrg> [0..1]  262
     Name <Nm> [1..1] Text 263
     Identification <Id> [0..1]  263
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 263
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 264
     Purpose <Purp> [0..1] Text 264
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 264
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 264
     RegistrationDate <RegnDt> [0..1] Date 265
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 265
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 265
     PostalAddress <PstlAdr> [1..5] ± C10 265
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 265
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 266
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 266
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 266
   IssueSize <IsseSz> [0..1] Quantity 267
   IssuePrice <IssePric> [0..1] ± 267
   IssuanceDistribution <IssncDstrbtn> [0..1]  267
{Or     Code <Cd> [1..1] CodeSet 268
Or}     Proprietary <Prtry> [1..1] ± 268
   GoverningLaw <GovngLaw> [0..*]  268
     Identification <Id> [0..1] Text 268
     Country <Ctry> [0..1] CodeSet C4 268
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 261 March 2024
```

