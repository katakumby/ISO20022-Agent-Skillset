---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.66 SafekeepingPlaceFormat41Choice", "16.1.15.66.5 Proprietary <Prtry>"]
file_pages: [998]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.66.5 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 998 to 998.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 998

```text
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 1244
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
16.1.15.66.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification78" on page 881 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 881
   Identification <Id> [0..1] Text 881
16.1.15.67  DefaultProcessingOrStandingInstruction2Choice
Definition: Choice between default processing or standing instruction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DefaultOptionIndicator <DfltOptnInd> [1..1] Indicator 998
Or}   StandingInstructionIndicator <StgInstrInd> [1..1] Indicator 998
16.1.15.67.1  DefaultOptionIndicator <DfltOptnInd>
Presence: [1..1]
Definition: Indicates whether the option, for example, currency option, will be selected by default if no
instruction is provided by the account owner.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
16.1.15.67.2  StandingInstructionIndicator <StgInstrInd>
Presence: [1..1]
Definition: Indicates whether an account owner has placed a standing order to select this corporate
action option.
The standing instruction may or may not be overridden, depending on account or event terms.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 998 February 2026
```

