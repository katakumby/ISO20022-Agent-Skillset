---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.5 InferredMatchingStatus <IfrrdMtchgSts>"]
file_pages: [448]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.5 InferredMatchingStatus <IfrrdMtchgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 448 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 448

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
13.4.7.5  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [0..1]
Definition: Provides the matching status of an instruction as per the account servicer or the Market
Infrastructure based on an allegement. At this time no matching took place on the market (at the CSD/
ICSD/MI).
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus25Choice" on page 1954 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1954
Or   Unmatched <Umtchd> [1..1]  1955
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1955
Or}     Reason <Rsn> [1..*]  1955
       Code <Cd> [1..1] ± 1956
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1956
Or}   Proprietary <Prtry> [1..1] ± 1956
13.4.7.6  MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus25Choice"
on page 1954 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1954
Or   Unmatched <Umtchd> [1..1]  1955
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1955
Or}     Reason <Rsn> [1..*]  1955
       Code <Cd> [1..1] ± 1956
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1956
Or}   Proprietary <Prtry> [1..1] ± 1956
13.4.7.7  SettlementStatus <SttlmSts>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 448 March 2026
```

