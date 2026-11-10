---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 reda.014.001.02 PartyCreationRequestV02", "2.4 Message Building Blocks", "2.4.2 Party <Pty>", "2.4.2.6 Type <Tp>", "2.4.2.6.1 Code <Cd>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 2.4.2.6.1 Code <Cd>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
Type <Tp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 13
Or}   Proprietary <Prtry> [1..1] Text 13
2.4.2.6.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 182
2.4.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 188
2.4.2.7  TechnicalAddress <TechAdr>
Presence: [0..*]
Definition: Unique technical address to unambiguously identify a party for receiving messages from the
executing system.
TechnicalAddress <TechAdr> contains one of the following TechnicalIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 13
Or}   TechnicalAddress <TechAdr> [1..1] Text 13
2.4.2.7.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 185
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
2.4.2.7.2  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Technical address of the party is defined in a free text format.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.014.001.02 PartyCreationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
13 March 2024
```

