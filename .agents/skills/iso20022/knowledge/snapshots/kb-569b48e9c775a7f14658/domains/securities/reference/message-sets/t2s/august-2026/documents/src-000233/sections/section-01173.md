---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.2.2.19 ClassificationType <ClssfctnTp>", "28.4.2.2.2.19.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>"]
file_pages: [1688, 1689]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.2.19.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1688 to 1689.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1688

```text
Definition: Information allowing the classification of a financial instrument, for example, with its ISO CFI
(Classification of Financial Instrument) or product type.
ClassificationType <ClssfctnTp> contains the following ClassificationType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 1688
   FinancialInstrumentProductTypeCode
<FinInstrmPdctTpCd>
[0..1] CodeSet 1688
   AlternateClassification <AltrnClssfctn> [0..*] ± 1688
28.4.2.2.2.19.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 3321
28.4.2.2.2.19.2  FinancialInstrumentProductTypeCode <FinInstrmPdctTpCd>
Presence: [0..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstrumentProductType1Code" on page 3242
28.4.2.2.2.19.3  AlternateClassification <AltrnClssfctn>
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
28.4.2.2.2.20  Issuance <Issnc>
Presence: [0..1]
Definition: Details regarding the issuance of an asset.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1688 August 2026
```

## File page 1689

```text
Issuance <Issnc> contains the following Issuance5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuePlace <IssePlc> [0..1] IdentifierSet 1690
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C4 1690
   IssueDate <IsseDt> [0..1] Date 1690
   AnnouncementDate <AnncmntDt> [0..1] DateTime 1690
   ISINValidFrom <ISINVldFr> [0..1] Date 1690
   IssuerOrganisation <IssrOrg> [0..1]  1690
     Name <Nm> [1..1] Text 1691
     Identification <Id> [0..1]  1691
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1691
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 1692
     Purpose <Purp> [0..1] Text 1692
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 1692
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 1692
     RegistrationDate <RegnDt> [0..1] Date 1693
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 1693
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 1693
     PostalAddress <PstlAdr> [1..5] ± C10 1693
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 1693
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 1694
   IssueNominalAmount <IsseNmnlAmt> [0..1] ± 1694
   FullIssuedAmount <FullIssdAmt> [0..1] Amount C1, C5 1694
   IssueSize <IsseSz> [0..1] Quantity 1695
   IssuePrice <IssePric> [0..1] ± 1695
   IssuanceDistribution <IssncDstrbtn> [0..1]  1695
{Or     Code <Cd> [1..1] CodeSet 1696
Or}     Proprietary <Prtry> [1..1] ± 1696
   GoverningLaw <GovngLaw> [0..*]  1696
     Identification <Id> [0..1] Text 1696
     Country <Ctry> [0..1] CodeSet C4 1696
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1689 August 2026
```

