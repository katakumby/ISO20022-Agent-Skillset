---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.13 BeneficiaryDetails <BnfcryDtls>", "34.4.4.21.13.1 BeneficiaryType <BnfcryTp>", "34.4.4.21.13.1.2 Proprietary <Prtry>"]
file_pages: [934]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.13.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 934 to 934.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 934

```text
Datatype: "BeneficiaryType1Code" on page 5277
CodeName Name Definition
DEPE Dependent Beneficiary is a dependent.
NOMI Nominee Beneficiary is a nominee.
SUCC Successor Beneficiary is a successor.
34.4.4.21.13.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of beneficiary expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
34.4.4.21.13.2  DeathUnderLimit <DthUdrLmt>
Presence: [0..1]
Definition: Indicates whether the original pension holder was under the age limit when deceased.
Typically, in the UK this limit is seventy-five.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
34.4.4.21.13.3  DateOfDeath <DtOfDth>
Presence: [0..1]
Definition: Date of death of the original pension holder.
Datatype: "ISODate" on page 5388
34.4.4.21.13.4  DateDesignatedToBeneficiary <DtDsgntdToBnfcry>
Presence: [0..1]
Definition: Date on which the new beneficiary was designated.
Datatype: "ISODate" on page 5388
34.4.4.21.13.5  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the recipient of the drawdown.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 934 May 2026
```

