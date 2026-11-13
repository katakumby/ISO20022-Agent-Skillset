---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.8 StandingSettlementInstructionDetails <StgSttlmInstrDtls>", "29.4.8.1 SettlementStandingInstructionDatabase <SttlmStgInstrDB>"]
file_pages: [1033]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.8.1 SettlementStandingInstructionDatabase <SttlmStgInstrDB>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1033 to 1033.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1033

```text
StandingSettlementInstructionDetails <StgSttlmInstrDtls> contains the following
StandingSettlementInstruction20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 1033
   Counterparty <CtrPty> [1..1] ± 1033
   Vendor <Vndr> [0..1] ± 1034
   OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C9, C17,
C31,
C32,
C33,
C34,
C51
1034
   OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C9, C17,
C31,
C32,
C33,
C34,
C51
1036
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Following Must be True
    /Vendor Must be present
29.4.8.1  SettlementStandingInstructionDatabase <SttlmStgInstrDB>
Presence: [1..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
SettlementStandingInstructionDatabase <SttlmStgInstrDB> contains one of the following elements
(see "SettlementStandingInstructionDatabase4Choice" on page 1583 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1583
Or}   Proprietary <Prtry> [1..1] ± 1583
29.4.8.2  Counterparty <CtrPty>
Presence: [1..1]
Definition: Identification of the buyer or seller in a standing settlement instruction enabling to derive the
Standing Settlement Instruction.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1033 March 2026
```

