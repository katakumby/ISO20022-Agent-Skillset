---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.4 Message Building Blocks", "5.4.5 TransactionDetails <TxDtls>"]
file_pages: [156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.4.5 TransactionDetails <TxDtls>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 156 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 156

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus34Choice" on page 2027 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  2027
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2027
Or}     Reason <Rsn> [1..*] ± 2027
Or   Failing <Flng> [1..1]  2028
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2028
Or}     Reason <Rsn> [1..*] ± 2028
Or}   Proprietary <Prtry> [1..1] ± 2028
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
5.4.5 TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C11 "SafekeepingAccountOrBlockChainAddress1Rule", C12
"SafekeepingAccountOrBlockChainAddress2Rule", C13
"SafekeepingAccountOrBlockChainAddress3Rule"
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 156 March 2026
```

