---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "3.4 Message Building Blocks", "3.4.4 SettlementStatus <SttlmSts>"]
file_pages: [39]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 3.4.4 SettlementStatus <SttlmSts>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 39 to 39.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
3.4.4 SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the settlement status of a transaction.
Impacted by: C14 "PendingToFailingRule"
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus16Choice" on page 459 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  460
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 460
Or}     Reason <Rsn> [1..*] ± 460
Or   Failing <Flng> [1..1]  461
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 461
Or}     Reason <Rsn> [1..*] ± 461
Or}   Proprietary <Prtry> [1..1] ± 461
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
3.4.5 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which an entry is made.
Impacted by: C12 "IdentificationOrProxyPresenceRule", C11 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 387 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 388
   Type <Tp> [0..1] ± 388
   Currency <Ccy> [0..1] CodeSet C2 388
   Name <Nm> [0..1] Text 389
   Proxy <Prxy> [0..1] ± 389
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
39 March 2024
```

