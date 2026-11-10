---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.7 StandingSettlementInstructionDetails <StgSttlmInstrDtls>"]
file_pages: [1233]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.7 StandingSettlementInstructionDetails <StgSttlmInstrDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1233 to 1233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1233

```text
Collateral (taker) In Return
ReceiveDelivery: Delivery (DELI)
SettlementTransactionType: CollateralIn (COLI).
• SettlementDetailsElementsUsageRule
Conditions of use of the codes for the SettlementDetails field must be pre-agreed between account
owner and account servicer.
32.4.2.2.7  StandingSettlementInstructionDetails <StgSttlmInstrDtls>
Presence: [0..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Impacted by: C84 "VendorPresenceRule"
StandingSettlementInstructionDetails <StgSttlmInstrDtls> contains the following
StandingSettlementInstruction20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 1233
   Counterparty <CtrPty> [1..1] ± 1234
   Vendor <Vndr> [0..1] ± 1234
   OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1234
   OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1236
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Following Must be True
    /Vendor Must be present
32.4.2.2.7.1  SettlementStandingInstructionDatabase <SttlmStgInstrDB>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1233 March 2026
```

