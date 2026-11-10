---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>"]
file_pages: [4184, 4185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8 LegInformation <LegInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4184 to 4185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4184

```text
PartiallySettled <PrtlySttld> contains the following elements (see "PartiallySettledStatus10" on
page 5185 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5185
{Or     Code <Cd> [1..1] CodeSet 5185
Or}     Proprietary <Prtry> [1..1] ± 5186
   AdditionalInformation <AddtlInf> [0..1] Text 5186
56.4.3.3.8  LegInformation <LegInf>
Presence: [0..*]
Definition: Information about a switch leg that is rejected or repaired.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4184 May 2026
```

## File page 4185

```text
LegInformation <LegInf> contains the following SwitchLegReferences3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LegIdentification <LegId> [1..1]  4186
{Or     RedemptionLegIdentification <RedLegId> [1..1] Text 4187
Or}     SubscriptionLegIdentification <SbcptLegId> [1..1] Text 4187
   LegRejectionReason <LegRjctnRsn> [0..1] Text 4187
   RepairedFee <RprdFee> [0..10]  C6, C12 4187
     Type <Tp> [0..1]  4188
{Or       Code <Cd> [1..1] CodeSet 4188
Or}       Proprietary <Prtry> [1..1] ± 4190
     RepairedStandardAmount <RprdStdAmt> [0..1] Amount C1, C8 4190
     RepairedStandardRate <RprdStdRate> [0..1] Rate 4190
     RepairedDiscountAmount <RprdDscntAmt> [0..1] Amount C1, C8 4190
     RepairedDiscountRate <RprdDscntRate> [0..1] Rate 4191
     RepairedRequestedAmount <RprdReqdAmt> [0..1] Amount C1, C8 4191
     RepairedRequestedRate <RprdReqdRate> [0..1] Rate 4191
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 4192
     NewCommercialAgreementReferenceIndicator
<NewComrclAgrmtRefInd>
[0..1] Indicator 4192
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C16 4192
     AccountIdentification <AcctId> [1..1] Text 4193
     AccountName <AcctNm> [0..1] Text 4193
     AccountDesignation <AcctDsgnt> [0..1] Text 4193
     OwnerIdentification <OwnrId> [0..*] ± 4193
     AccountServicer <AcctSvcr> [0..1] ± 4193
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4194
     SubAccountDetails <SubAcctDtls> [0..1] ± 4194
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4194
   FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C13 4195
     Identification <Id> [1..1]  4197
{Or       ISIN <ISIN> [1..1] IdentifierSet 4197
Or       SEDOL <SEDOL> [1..1] IdentifierSet 4198
Or       CUSIP <CUSIP> [1..1] IdentifierSet 4198
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4185 May 2026
```

