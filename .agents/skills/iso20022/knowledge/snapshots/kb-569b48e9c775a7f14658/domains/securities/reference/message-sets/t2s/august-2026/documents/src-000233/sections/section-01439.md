---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["34 reda.014.001.02 PartyCreationRequestV02", "34.4 Message Building Blocks", "34.4.2 Party <Pty>", "34.4.2.6 Type <Tp>", "34.4.2.6.1 Code <Cd>"]
file_pages: [2050]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 34.4.2.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2050 to 2050.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2050

```text
Type <Tp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2050
Or}   Proprietary <Prtry> [1..1] Text 2050
34.4.2.6.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 3246
34.4.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 3328
34.4.2.7  TechnicalAddress <TechAdr>
Presence: [0..*]
Definition: Unique technical address to unambiguously identify a party for receiving messages from the
executing system.
TechnicalAddress <TechAdr> contains one of the following TechnicalIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 2050
Or}   TechnicalAddress <TechAdr> [1..1] Text 2050
34.4.2.7.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 3320
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
34.4.2.7.2  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Technical address of the party is defined in a free text format.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.014.001.02 PartyCreationRequestV02
Target2-Securities 2050 August 2026
```

