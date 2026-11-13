---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.17 AdditionalInformation <AddtlInf>"]
file_pages: [317]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.17 AdditionalInformation <AddtlInf>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 317 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 317

```text
5.4.9.17  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information.
AdditionalInformation <AddtlInf> contains the following CorporateActionNarrative32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationToComplyWith <InfToCmplyWth> [0..*] Text 317
   DeliveryDetails <DlvryDtls> [0..*] Text 317
   ForeignExchangeInstructionsAdditionalInformation
<FXInstrsAddtlInf>
[0..*] Text 317
   InstructionAdditionalInformation <InstrAddtlInf> [0..*] Text 317
5.4.9.17.1  InformationToComplyWith <InfToCmplyWth>
Presence: [0..*]
Definition: Provides information conditions to the account owner that are to be complied with, for
example, not open to US/Canadian residents, Qualified Institutional Buyers (QIB) or Sophisticated
Investor Letter (SIL) to be provided.
Datatype: "Max350Text" on page 1250
5.4.9.17.2  DeliveryDetails <DlvryDtls>
Presence: [0..*]
Definition: Provides additional information on the delivery details of the outturned (derived) securities.
This narrative is only to be used in case the securities are not eligible at the agent/custodian, and may
not be used for settlement instructions.
Datatype: "Max350Text" on page 1250
5.4.9.17.3  ForeignExchangeInstructionsAdditionalInformation <FXInstrsAddtlInf>
Presence: [0..*]
Definition: Provides additional details pertaining to foreign exchange instructions.
Datatype: "Max350Text" on page 1250
5.4.9.17.4  InstructionAdditionalInformation <InstrAddtlInf>
Presence: [0..*]
Definition: Provides additional details pertaining to the corporate action instruction.
Datatype: "Max350Text" on page 1250
5.4.10 ProtectInstruction <PrtctInstr>
Presence: [0..1]
Definition: Provides detailed information on protect and cover protect instructions.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 317 February 2026
```

