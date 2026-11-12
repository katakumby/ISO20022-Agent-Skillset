---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.19 ClassificationType <ClssfctnTp>"]
file_pages: [414, 415]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.19 ClassificationType <ClssfctnTp>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 414 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 414

```text
13.1.6.4.19  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Information allowing the classification of a financial instrument, for example, with its ISO CFI
(Classification of Financial Instrument) or product type.
ClassificationType <ClssfctnTp> contains the following ClassificationType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 414
   FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 414
   AlternateClassification <AltrnClssfctn> [0..*] ± 414
13.1.6.4.19.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 530
13.1.6.4.19.2  FinancialInstrumentProductTypeCode <FinInstrmPdctTpCd>
Presence: [0..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstrumentProductType1Code" on page 514
13.1.6.4.19.3  AlternateClassification <AltrnClssfctn>
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
13.1.6.4.20  Issuance <Issnc>
Presence: [0..1]
Definition: Details regarding the issuance of an asset.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 414 March 2024
```

## File page 415

```text
Issuance <Issnc> contains the following Issuance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 416
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 416
   IssueDate <IsseDt> [0..1] Date 416
   AnnouncementDate <AnncmntDt> [0..1] DateTime 416
   ISINValidFrom <ISINVldFr> [0..1] Date 416
   IssuerOrganisation <IssrOrg> [0..1]  416
     Name <Nm> [1..1] Text 417
     Identification <Id> [0..1]  417
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 417
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 418
     Purpose <Purp> [0..1] Text 418
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 418
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 418
     RegistrationDate <RegnDt> [0..1] Date 419
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 419
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 419
     PostalAddress <PstlAdr> [1..5] ± C10 419
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 419
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 420
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 420
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 420
   IssueSize <IsseSz> [0..1] Quantity 421
   IssuePrice <IssePric> [0..1] ± 421
   IssuanceDistribution <IssncDstrbtn> [0..1]  421
{Or     Code <Cd> [1..1] CodeSet 422
Or}     Proprietary <Prtry> [1..1] ± 422
   GoverningLaw <GovngLaw> [0..*]  422
     Identification <Id> [0..1] Text 422
     Country <Ctry> [0..1] CodeSet C4 422
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 415 March 2024
```

