---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.19 ClassificationType <ClssfctnTp>"]
file_pages: [764, 765]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.19 ClassificationType <ClssfctnTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 764 to 765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 764

```text
27.4.2.3.19  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Information allowing the classification of a financial instrument, for example, with its ISO CFI
(Classification of Financial Instrument) or product type.
ClassificationType <ClssfctnTp> contains the following ClassificationType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 764
   FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 764
   AlternateClassification <AltrnClssfctn> [0..*] ± 764
27.4.2.3.19.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 3321
27.4.2.3.19.2  FinancialInstrumentProductTypeCode <FinInstrmPdctTpCd>
Presence: [0..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstrumentProductType1Code" on page 3242
27.4.2.3.19.3  AlternateClassification <AltrnClssfctn>
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
27.4.2.3.20  Issuance <Issnc>
Presence: [0..1]
Definition: Details regarding the issuance of an asset.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 764 August 2026
```

## File page 765

```text
Issuance <Issnc> contains the following Issuance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 766
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 766
   IssueDate <IsseDt> [0..1] Date 766
   AnnouncementDate <AnncmntDt> [0..1] DateTime 766
   ISINValidFrom <ISINVldFr> [0..1] Date 766
   IssuerOrganisation <IssrOrg> [0..1]  766
     Name <Nm> [1..1] Text 767
     Identification <Id> [0..1]  767
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 767
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 768
     Purpose <Purp> [0..1] Text 768
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 768
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 768
     RegistrationDate <RegnDt> [0..1] Date 769
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 769
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 769
     PostalAddress <PstlAdr> [1..5] ± C10 769
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 769
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 770
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 770
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 770
   IssueSize <IsseSz> [0..1] Quantity 771
   IssuePrice <IssePric> [0..1] ± 771
   IssuanceDistribution <IssncDstrbtn> [0..1]  771
{Or     Code <Cd> [1..1] CodeSet 772
Or}     Proprietary <Prtry> [1..1] ± 772
   GoverningLaw <GovngLaw> [0..*]  772
     Identification <Id> [0..1] Text 772
     Country <Ctry> [0..1] CodeSet C4 772
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 765 August 2026
```

