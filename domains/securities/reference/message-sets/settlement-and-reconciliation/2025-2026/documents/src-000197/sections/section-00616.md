---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.10 SettlementParameters <SttlmParams>", "27.4.10.20 EligibleForCollateral <ElgblForColl>"]
file_pages: [930]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.10.20 EligibleForCollateral <ElgblForColl>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 930 to 930.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 930

```text
27.4.10.20  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
27.4.11 StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
Presence: [0..1]
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
Impacted by: C69 "VendorPresenceRule"
StandingSettlementInstructionDetails <StgSttlmInstrDtls> contains the following
StandingSettlementInstruction20 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 931
   Counterparty <CtrPty> [1..1] ± 931
   Vendor <Vndr> [0..1] ± 931
   OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C10,
C23,
C38,
C39,
C40,
C41,
C63
931
   OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C10,
C23,
C38,
C39,
C40,
C41,
C63
933
Constraints
• VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
On Condition
    /SettlementStandingInstructionDatabase/Code is equal to value 'VendorDatabase'
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 930 March 2026
```

