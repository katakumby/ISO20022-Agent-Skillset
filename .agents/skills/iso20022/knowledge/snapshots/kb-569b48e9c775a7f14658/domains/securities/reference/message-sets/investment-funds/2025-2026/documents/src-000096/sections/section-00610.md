---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [839]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# Continuation at file page 839

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 839 to 839.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 839

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalAmountNetDrawdown <TtlAmtNetDrwdwn> [0..1] Amount C1 931
     AdditionalFundsDesignated <AddtlFndsDsgntd> [0..1] Indicator 932
     PensionCommencementLumpSumRemaining
<PnsnCmcmntLumpSumRmng>
[0..1] Amount C1 932
     PensionCommencementLumpSumDate
<PnsnCmcmntLumpSumDt>
[0..1] Date 932
     MultiplePensionCommencementLumpSums
<MltplPnsnCmcmntLumpSums>
[0..1] Indicator 932
     LifetimeAllowance <LftmAllwnc> [0..1] Rate 933
     RecipientOfDrawdownIndicator <RcptOfDrwdwnInd> [0..1] Indicator 933
     BeneficiaryDetails <BnfcryDtls> [0..1]  933
       BeneficiaryType <BnfcryTp> [0..1]  933
{Or         Code <Cd> [1..1] CodeSet 933
Or}         Proprietary <Prtry> [1..1] ± 934
       DeathUnderLimit <DthUdrLmt> [0..1] Indicator 934
       DateOfDeath <DtOfDth> [0..1] Date 934
       DateDesignatedToBeneficiary <DtDsgntdToBnfcry> [0..1] Date 934
       AdditionalInformation <AddtlInf> [0..*] ± 934
     CappedLimits <CapdLmts> [0..1]  935
       StartDate <StartDt> [0..1] Date 935
       IncomeLimitCurrentPeriod <IncmLmtCurPrd> [0..1] Amount C1 935
       IncomeCurrentPeriod <IncmCurPrd> [0..1] Amount C1 935
       IncomeLimitNextPeriod <IncmLmtNxtPrd> [0..1] Amount C1 936
       AdditionalInformation <AddtlInf> [0..*] ± 936
     FlexibleDrawdownTriggeredDate
<FlxblDrwdwnTrggrdDt>
[0..1] Date 936
     TrancheDate <TrchDt> [0..1] Date 936
     AdditionalInformation <AddtlInf> [0..*] ± 937
   OtherDrawdownInformation <OthrDrwdwnInf> [0..1]  937
     EmploymentDetails <MplymntDtls> [0..1]  937
       TaxCode <TaxCd> [0..1] ± 938
       OtherTaxCodeIndicator <OthrTaxCdInd> [0..1] Indicator 938
       CumulativeTaxIndicator <CmltvTaxInd> [0..1] Indicator 938
       PreviousPay <PrvsPay> [0..1] Amount C1, C10 939
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 839 May 2026
```

