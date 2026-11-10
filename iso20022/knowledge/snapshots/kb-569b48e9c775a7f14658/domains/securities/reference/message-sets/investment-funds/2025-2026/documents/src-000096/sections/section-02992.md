---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>", "56.4.3.3.8.3 RepairedFee <RprdFee>", "56.4.3.3.8.3.8 CommercialAgreementReference <ComrclAgrmtRef>"]
file_pages: [4192]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8.3.8 CommercialAgreementReference <ComrclAgrmtRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4192 to 4192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4192

```text
Definition: Modified value of the requested fee (charge/commission) rate applied on the order (the
requested fee (charge/commission) rate in the original individual order that has been repaired so that
the order can be accepted).
Datatype: "PercentageRate" on page 5401
56.4.3.3.8.3.8  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
56.4.3.3.8.3.9  NewCommercialAgreementReferenceIndicator <NewComrclAgrmtRefInd>
Presence: [0..1]
Definition: Indicates if the CommercialAgreementReference is a new reference or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
56.4.3.3.8.4  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account identification of the switch leg that is rejected or repaired.
Impacted by: C16 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4193
   AccountName <AcctNm> [0..1] Text 4193
   AccountDesignation <AcctDsgnt> [0..1] Text 4193
   OwnerIdentification <OwnrId> [0..*] ± 4193
   AccountServicer <AcctSvcr> [0..1] ± 4193
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4194
   SubAccountDetails <SubAcctDtls> [0..1] ± 4194
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4194
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4192 May 2026
```

