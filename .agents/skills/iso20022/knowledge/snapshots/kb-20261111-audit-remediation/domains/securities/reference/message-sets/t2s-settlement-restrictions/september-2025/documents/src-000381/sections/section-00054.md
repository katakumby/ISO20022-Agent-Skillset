---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.3 StatusAndReason <StsAndRsn>", "3.4.3.4.3.3 Settled <Sttld>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.3.3 Settled <Sttld>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus34Choice" on page 308 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  308
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 308
Or}     Reason <Rsn> [1..*] ± 308
Or   Failing <Flng> [1..1]  309
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 309
Or}     Reason <Rsn> [1..*] ± 309
Or}   Proprietary <Prtry> [1..1] ± 309
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
3.4.3.4.3.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 273
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 273
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
3.4.3.4.4  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 345
3.4.3.4.5  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 73 September 2025
```

