---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.11 DefaultProcessingOrStandingInstruction <DfltPrcgOrStgInstr>"]
file_pages: [435]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.11 DefaultProcessingOrStandingInstruction <DfltPrcgOrStgInstr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 435 to 435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.4.13.11  DefaultProcessingOrStandingInstruction <DfltPrcgOrStgInstr>
Presence: [1..1]
Definition: Indicates whether the corporate action movement is a default processing or a standing
instruction.
DefaultProcessingOrStandingInstruction <DfltPrcgOrStgInstr> contains one of the following
elements (see "DefaultProcessingOrStandingInstruction2Choice" on page 998 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DefaultOptionIndicator <DfltOptnInd> [1..1] Indicator 998
Or}   StandingInstructionIndicator <StgInstrInd> [1..1] Indicator 998
7.4.13.12  ChargesAppliedIndicator <ChrgsApldInd>
Presence: [0..1]
Definition: Indicates whether redemption charges apply.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
7.4.13.13  CertificationBreakdownIndicator <CertfctnBrkdwnInd>
Presence: [0..1]
Definition: Indicates whether certification/breakdown is required from the account owner.
Yes: certification required
No: no certification required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
7.4.13.14  WithdrawalAllowedIndicator <WdrwlAllwdInd>
Presence: [0..1]
Definition: Indicates whether withdrawal of instruction is allowed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
7.4.13.15  ChangeAllowedIndicator <ChngAllwdInd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 435 February 2026
```

