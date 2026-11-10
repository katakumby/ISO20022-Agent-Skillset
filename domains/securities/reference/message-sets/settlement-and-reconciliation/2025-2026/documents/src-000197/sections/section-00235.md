---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.7.16 StatusAndReason <StsAndRsn>", "9.4.7.16.1 Proprietary <Prtry>"]
file_pages: [350]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.7.16.1 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 350 to 350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 350

```text
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
• SettlementStatusAndMatchedRule
If settlement status/reason is used alone, then it means that the transaction is matched (if a matching
process exists in the concerned market or at the concerned account servicer).
9.4.7.16.1  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 1877
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
9.4.7.16.2  MatchingStatus <MtchgSts>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus24Choice"
on page 1963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
9.4.7.16.3  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [1..1]
Definition: Provides the matching status of an instruction as known by the account servicer based on an
allegement. At this time no matching took place on the market (at the CSD/ICSD).
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 350 March 2026
```

