---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.3 StatusAndReason <StsAndRsn>", "4.4.3.4.3.1 InferredMatchingStatus <IfrrdMtchgSts>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.3.1 InferredMatchingStatus <IfrrdMtchgSts>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
• SettlementStatusAndMatchedRule
If SettlementStatus/Reason is used alone, then it means that the transaction is matched (if a
matching process exists in the concerned market or at the concerned account servicer).
4.4.3.4.3.1  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [0..1]
Definition: Provides the matching status of an instruction as known by the account servicer based on an
allegement. At this time no matching took place on the market (at the CSD/ICSD).
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus24Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C6 477
Or   Unmatched <Umtchd> [1..1]  477
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 478
Or}     Reason <Rsn> [1..*]  478
       Code <Cd> [1..1]  478
{Or         Code <Cd> [1..1] CodeSet 479
Or}         Proprietary <Prtry> [1..1] ± 481
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 481
Or}   Proprietary <Prtry> [1..1] ± 481
4.4.3.4.3.2  MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 121 March 2026
```

