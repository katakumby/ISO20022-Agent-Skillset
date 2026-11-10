---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.8 SettlementParameters <SttlmParams>", "20.4.9.1 SettlementStandingInstructionDatabase <SttlmStgInstrDB>"]
file_pages: [684]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.9.1 SettlementStandingInstructionDatabase <SttlmStgInstrDB>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 684 to 684.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 684

```text
20.4.9 StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
Presence: [0..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Impacted by: C60 "VendorPresenceRule"
StandingSettlementInstructionDetails <StgSttlmInstrDtls> contains the following
StandingSettlementInstruction20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 684
   Counterparty <CtrPty> [1..1] ± 685
   Vendor <Vndr> [0..1] ± 685
   OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C9, C17,
C33,
C34,
C35,
C36,
C55
685
   OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C9, C17,
C33,
C34,
C35,
C36,
C55
687
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Following Must be True
    /Vendor Must be present
20.4.9.1  SettlementStandingInstructionDatabase <SttlmStgInstrDB>
Presence: [1..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 684 March 2026
```

