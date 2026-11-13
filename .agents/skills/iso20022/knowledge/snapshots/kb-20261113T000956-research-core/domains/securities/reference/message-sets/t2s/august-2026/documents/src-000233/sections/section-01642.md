---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.6 TechnicalAddress <TechAdr>", "58.4.2.2.2.6.1 Old <Od>"]
file_pages: [2276]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.6.1 Old <Od>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2276 to 2276.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2276

```text
TechnicalAddress <TechAdr> contains the following UpdateLogTechnicalAddress1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2276
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 2276
Or}     TechnicalAddress <TechAdr> [1..1] Text 2276
   New <New> [1..1]  2276
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 2277
Or}     TechnicalAddress <TechAdr> [1..1] Text 2277
58.4.2.2.2.6.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains one of the following TechnicalIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C2 2276
Or}   TechnicalAddress <TechAdr> [1..1] Text 2276
58.4.2.2.2.6.1.1  BICFI <BICFI>
Presence: [1..1]
Definition: Technical address of the party is defined as a financial institution business identifier code.
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 3320
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
58.4.2.2.2.6.1.2  TechnicalAddress <TechAdr>
Presence: [1..1]
Definition: Technical address of the party is defined in a free text format.
Datatype: "Max256Text" on page 3327
58.4.2.2.2.6.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2276 August 2026
```

