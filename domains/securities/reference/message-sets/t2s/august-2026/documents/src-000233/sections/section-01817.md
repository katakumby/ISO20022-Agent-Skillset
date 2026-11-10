---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.3 StatusAndReason <StsAndRsn>", "72.4.3.3.3 SettlementStatus <SttlmSts>"]
file_pages: [2498]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.3.3 SettlementStatus <SttlmSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2498 to 2498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2498

```text
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus24Choice"
on page 3168 for details)
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
72.4.3.3.3  SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C26 "PendingToFailingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2498 August 2026
```

