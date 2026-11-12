---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>"]
file_pages: [310, 311]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8 SecurityIdentification <SctyId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 310 to 311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
15.4.5.8  SecurityIdentification <SctyId>
Presence: [1..1]
Definition: Identification of the security.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 310 May 2026
```

## File page 311

```text
SecurityIdentification <SctyId> contains the following SecurityIdentification47 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  C12,
C13,
C21,
C22,
C27
312
     OtherIdentification <OthrId> [0..*]  313
       Identification <Id> [1..1] Text 313
       Suffix <Sfx> [0..1] Text 313
       Type <Tp> [1..1] ± 313
     Description <Desc> [0..1] Text 314
     ISIN <ISIN> [0..1] IdentifierSet 314
   Name <Nm> [1..1] Text 314
   ShortName <ShrtNm> [0..1] Text 314
   ClassType <ClssTp> [0..1] Text 314
   UmbrellaName <UmbrllNm> [0..1] Text 314
   NewUmbrella <NewUmbrll> [0..1] Indicator 314
   ClassificationType <ClssfctnTp> [0..1] ± 315
   BaseCurrency <BaseCcy> [0..1] CodeSet C1 315
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C6 315
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C6 315
   ProductType <PdctTp> [0..1]  316
{Or     Code <Cd> [1..1] CodeSet 316
Or}     Proprietary <Prtry> [1..1] ± 316
   Issuer <Issr> [0..1] ± 317
   IssuerProductGovernanceProcess
<IssrPdctGovncPrc>
[0..1] ± 317
   ProductCategory <PdctCtgy> [0..1] Text 317
   ProductCategoryGermany <PdctCtgyDE> [0..1] Text 318
   NotionalOrUnitBased <NtnlOrUnitBased> [0..1]  318
{Or     Code <Cd> [1..1] CodeSet 318
Or}     Proprietary <Prtry> [1..1] ± 318
   QuotationType <QtnTp> [0..1] ± 319
   LeveragedOrContingentLiability
<LvrgdOrCntngntLblty>
[0..1] Indicator 319
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 311 May 2026
```

