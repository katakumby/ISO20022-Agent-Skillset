---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.12 FundDetails <FndDtls>"]
file_pages: [322, 323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.12 FundDetails <FndDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 322 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 322

```text
FundManagementCompany <FndMgmtCpny> contains the following elements (see
"ContactAttributes5" on page 5021 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5021
   PostalAddress <PstlAdr> [0..1] ± 5021
   PhoneNumber <PhneNb> [0..1] Text 5022
   FaxNumber <FaxNb> [0..1] Text 5022
   EmailAddress <EmailAdr> [0..1] Text 5022
   URLAddress <URLAdr> [0..1] Text 5022
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5022
   LEI <LEI> [0..1] IdentifierSet 5023
15.4.5.12  FundDetails <FndDtls>
Presence: [0..1]
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, for example, dividend option or valuation currency.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 322 May 2026
```

## File page 323

```text
FundDetails <FndDtls> contains the following elements (see "FinancialInstrument96" on page 4484 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PhysicalBearerSecurities <PhysBrScties> [0..1] Indicator 4485
   DematerialisedBearerSecurities <DmtrlsdBrScties> [0..1] Indicator 4486
   PhysicalRegisteredSecurities <PhysRegdScties> [0..1] Indicator 4486
   DematerialisedRegisteredSecurities
<DmtrlsdRegdScties>
[0..1] Indicator 4486
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4486
   DividendPolicy <DvddPlcy> [0..1] CodeSet 4486
   DividendFrequency <DvddFrqcy> [0..1] CodeSet 4487
   ReinvestmentFrequency <RinvstmtFrqcy> [0..1] CodeSet 4487
   FrontEndLoad <FrntEndLd> [0..1] Indicator 4488
   BackEndLoad <BckEndLd> [0..1] Indicator 4488
   SwitchFee <SwtchFee> [0..1] Indicator 4488
   EUSavingsDirective <EUSvgsDrctv> [0..1] CodeSet 4488
   LaunchDate <LnchDt> [0..1] Date 4489
   FundEndDate <FndEndDt> [0..1] Date 4489
   TerminationDate <TermntnDt> [0..1] Date 4489
   InitialOfferEndDate <InitlOfferEndDt> [0..1] Date 4489
   SuspensionStartDate <SspnsnStartDt> [0..1] Date 4489
   SuspensionEndDate <SspnsnEndDt> [0..1] Date 4489
   MaturityDate <MtrtyDt> [0..1] Date 4489
   MayBeTerminatedEarly <MayBeTermntdEarly> [0..1] CodeSet 4490
   ClosedEndFund <ClsdEndFnd> [0..1] Indicator 4490
   Equalisation <Equlstn> [0..1] Indicator 4490
   TaxEfficientProductEligible <TaxEffcntPdctElgbl> [0..1] Indicator 4490
   Authorised <Authrsd> [0..1] Indicator 4490
   RDRCompliant <RDRCmplnt> [0..1] Indicator 4491
   ManagementFeeSource <MgmtFeeSrc> [0..1] CodeSet 4491
   PerformanceFee <PrfrmncFee> [0..1] Indicator 4491
   AdditionalInformation <AddtlInf> [0..*] ± 4491
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 323 May 2026
```

