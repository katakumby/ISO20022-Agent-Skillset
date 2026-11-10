---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.3 StatusAndReason <StsAndRsn>", "72.4.3.3.1 InferredMatchingStatus <IfrrdMtchgSts>"]
file_pages: [2497]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.3.1 InferredMatchingStatus <IfrrdMtchgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2497 to 2497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2497

```text
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
• SettlementStatusAndMatchedRule
If SettlementStatus/Reason is used alone, then it means that the transaction is matched (if a
matching process exists in the concerned market or at the concerned account servicer).
72.4.3.3.1  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [0..1]
Definition: Provides the matching status of an instruction as known by the account servicer based on an
allegement. At this time no matching took place on the market (at the CSD/ICSD).
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus24Choice" on page 3168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C6 3168
Or   Unmatched <Umtchd> [1..1]  3169
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3169
Or}     Reason <Rsn> [1..*]  3169
       Code <Cd> [1..1]  3169
{Or         Code <Cd> [1..1] CodeSet 3170
Or}         Proprietary <Prtry> [1..1] ± 3172
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3172
Or}   Proprietary <Prtry> [1..1] ± 3172
72.4.3.3.2  MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2497 August 2026
```

