---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.10 StandingSettlementInstruction13", "7.1.19.10.1 SettlementStandingInstructionDatabase <SttlmStgInstrDB>"]
file_pages: [296]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.10.1 SettlementStandingInstructionDatabase <SttlmStgInstrDB>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 296 to 296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 296

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 296
   Vendor <Vndr> [0..1] ± 296
   OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C36,
C37,
C38,
C39,
C18
297
   OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C36,
C37,
C38,
C39,
C18
299
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Following Must be True
    /Vendor Must be present
7.1.19.10.1  SettlementStandingInstructionDatabase <SttlmStgInstrDB>
Presence: [1..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
SettlementStandingInstructionDatabase <SttlmStgInstrDB> contains one of the following elements
(see "SettlementStandingInstructionDatabase4Choice" on page 334 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 334
Or}   Proprietary <Prtry> [1..1] ± 335
7.1.19.10.2  Vendor <Vndr>
Presence: [0..1]
Definition: Vendor of the Settlement Standing Instruction database requested to be consulted.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 296 February 2025
```

