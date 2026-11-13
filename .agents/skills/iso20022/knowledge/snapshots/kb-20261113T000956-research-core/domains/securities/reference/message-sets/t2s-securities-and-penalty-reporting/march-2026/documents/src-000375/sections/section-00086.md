---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.3 StatusAndReason <StsAndRsn>", "4.4.3.4.3.3 SettlementStatus <SttlmSts>"]
file_pages: [122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.3.3 SettlementStatus <SttlmSts>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 122 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 122

```text
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus24Choice"
on page 476 for details)
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
4.4.3.4.3.3  SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C26 "PendingToFailingRule"
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 122 March 2026
```

