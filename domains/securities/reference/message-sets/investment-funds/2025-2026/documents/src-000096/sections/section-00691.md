---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.11 LifetimeAllowance <LftmAllwnc>"]
file_pages: [933]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.11 LifetimeAllowance <LftmAllwnc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 933 to 933.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 933

```text
34.4.4.21.11  LifetimeAllowance <LftmAllwnc>
Presence: [0..1]
Definition: Percentage of the lifetime allowance (LTA) used.
Datatype: "PercentageRate" on page 5401
34.4.4.21.12  RecipientOfDrawdownIndicator <RcptOfDrwdwnInd>
Presence: [0..1]
Definition: Indicates a person other than the original pension holder is the receiver of the drawdown
payment.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
34.4.4.21.13  BeneficiaryDetails <BnfcryDtls>
Presence: [0..1]
Definition: Information about the recipient of the drawdown, when not the original pension holder.
BeneficiaryDetails <BnfcryDtls> contains the following BeneficiaryDrawdown2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BeneficiaryType <BnfcryTp> [0..1]  933
{Or     Code <Cd> [1..1] CodeSet 933
Or}     Proprietary <Prtry> [1..1] ± 934
   DeathUnderLimit <DthUdrLmt> [0..1] Indicator 934
   DateOfDeath <DtOfDth> [0..1] Date 934
   DateDesignatedToBeneficiary <DtDsgntdToBnfcry> [0..1] Date 934
   AdditionalInformation <AddtlInf> [0..*] ± 934
34.4.4.21.13.1  BeneficiaryType <BnfcryTp>
Presence: [0..1]
Definition: Type of beneficiary.
BeneficiaryType <BnfcryTp> contains one of the following BeneficiaryType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 933
Or}   Proprietary <Prtry> [1..1] ± 934
34.4.4.21.13.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of beneficiary expressed as a code.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 933 May 2026
```

